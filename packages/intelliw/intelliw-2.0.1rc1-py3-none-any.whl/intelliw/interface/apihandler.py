'''
Author: hexu
Date: 2021-10-25 15:20:34
LastEditTime: 2023-05-24 15:15:48
LastEditors: Hexu
Description: api处理函数
FilePath: /iw-algo-fx/intelliw/interface/apihandler.py
'''
import asyncio
import os
import types
from concurrent.futures import ThreadPoolExecutor

import starlette.datastructures
from fastapi import FastAPI, Request as FARequest, Response as FAResponse
from fastapi.responses import StreamingResponse

import json
import traceback
import threading

from intelliw.utils import message, util
from intelliw.config import config
from intelliw.core.infer import Infer
from intelliw.utils.logger import _get_framework_logger
from intelliw.utils.util import get_json_encoder
from intelliw.utils.fastapi import request as my_request, gunicorn_server
from intelliw.utils import health_check

logger = _get_framework_logger()


class _CONTEXT_OBJECT:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def run(self):
        return self.func(*self.args)


class Application:
    """推理服务路由类
    example:
        @Application.route("/infer-api", method='get', need_feature=True)
        def infer(self, test_data):
            pass
    args:
        path           访问路由   /infer-api
        method         访问方式，支持 get post push delete head patch options
        need_feature   是否需要使用特征工程, 如果是自定义与推理无关的函数, 请设置False
    """

    # Set URL handlers
    HANDLERS = []

    def __init__(self, custom_router):
        self.app = FastAPI(
            json_encoder=get_json_encoder()
        )
        self.app.intelliw_setting = {}

        self.handler_process(custom_router)

    def __call__(self):
        return self.app

    @classmethod
    def route(cls, path, **options):
        """
        register api route
        """

        def decorator(function):
            cls.HANDLERS.append((
                path,
                {'func': function.__name__,
                 'method': options.pop('method', 'post').lower(),
                 'need_feature': options.pop('need_feature', True)}))
            return function

        return decorator

    def handler_process(self, routers):
        # 加载自定义api, 配置在algorithm.yaml中
        for router in routers:
            Application.HANDLERS.append((
                router["path"],
                {'func': router["func"],
                 'method': router.get("method", "post").lower(),
                 'need_feature': router.get("need_feature", True)}))

        # 检查用户是否完全没有配置路由
        if len(Application.HANDLERS) == 0:
            Application.HANDLERS.append((
                '/predict',
                {'func': 'infer', 'method': 'post', 'need_feature': True}))  # 默认值

        # 集中绑定路由
        _route_cache = {}
        for router, info in Application.HANDLERS:
            func, method, need_feature = info.get('func'), info.get(
                'method'), info.get('need_feature')
            if _route_cache.get(router + func, None):
                continue
            _route_cache[router + func] = True
            self.app.intelliw_setting[f'api-{router}'] = info
            self.app.add_api_route(
                router, endpoint=api_handler, methods=[method])
            logger.info("方法: %s 加载成功, 访问路径：%s, 访问方法: %s, 是否需要特征处理: %s",
                        func, router, method, need_feature)

        # healthcheck
        # gateway
        self.app.add_api_route(
            '/healthcheck',
            endpoint=health_check_handler, methods=['get', 'post'])

        # eureka
        self.app.add_api_route(
            '/CloudRemoteCall/',
            endpoint=eureka_health_check_handler, methods=['get', 'post'])


def set_context(func, *args):
    ApiService.CONTEXT_OBJECT = _CONTEXT_OBJECT(func, *args)


# get_router_config

class ApiService:
    """
    intelliw api service
    """
    _instance = None
    _init_flag = False

    CONTEXT_OBJECT = None

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空对象，若为空说明第一个对象还没被创建
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, port, path, response_addr):
        if ApiService._init_flag:
            return
        ApiService._init_flag = True
        self.port = port  # 8888
        self.infer = Infer(path, response_addr)
        self.app = Application(self.infer.pipeline.custom_router).app
        self.reporter = self.infer.pipeline.recorder
        self.app.intelliw_setting.update({"infer": self.infer, "reporter": self.reporter})
        self._report_start()

    def _report_start(self):
        """
        report start
        """
        self.reporter.report(message.CommonResponse(
            200, "inferstatus", '',
            json.dumps([{'status': 'start',
                         'inferid': config.INFER_ID,
                         'instanceid': config.INSTANCE_ID,
                         'inferTaskStatus': []}],
                       cls=get_json_encoder(), ensure_ascii=False)
        ))

    @staticmethod
    def _eureka_server():
        if len(config.EUREKA_SERVER) > 0:
            from intelliw.core.linkserver import linkserver
            try:
                should_register = config.EUREKA_APP_NAME != ''
                iports = json.loads(config.REGISTER_CLUSTER_ADDRESS)
                profile = config.EUREKA_ZONE or 'test'
                linkserver.client(
                    config.EUREKA_SERVER, config.EUREKA_PROVIDER_ID,
                    should_register, config.EUREKA_APP_NAME, iports, profile)
                logger.info("eureka server client init success, register:%s, server name: %s",
                            should_register, config.EUREKA_APP_NAME)
            except Exception as e:
                logger.error(
                    f"eureka server client init failed, error massage: {e}")

    def thread_pool_init(self, thread):
        initializer, initargs = None, ()
        if self.CONTEXT_OBJECT is not None:
            def threading_init(pool, func, *args):
                t = threading.currentThread().ident
                pool[t] = func(*args)

            initializer = threading_init
            initargs = (
                self.infer.pipeline.thread_data_pool,
                self.CONTEXT_OBJECT.func,
                *self.CONTEXT_OBJECT.args
            )
        self.infer.pipeline.async_executor = ThreadPoolExecutor(
            thread, initializer=initializer, initargs=initargs, thread_name_prefix="IntelliwServerPool")

    def _fastapi_server(self):
        worker, thread = 1, util.number_of_threads(config.CPU_COUNT)

        # 自定义线程数
        if config.INFER_MULTI_THREAD_COUNT:
            thread = min(32, max(1, config.INFER_MULTI_THREAD_COUNT))

        self.thread_pool_init(thread)

        # 多进程
        if config.INFER_MULTI_PROCESS:
            worker = util.number_of_workers(config.CPU_COUNT)
            setting = gunicorn_server.default_config(
                f'0.0.0.0:{self.port}',
                workers=worker,
            )
            server = gunicorn_server.GunServer(self.app, setting, logger)
        else:
            # 默认模式
            server = gunicorn_server.UvicornServer(
                self.app,
                "0.0.0.0", self.port
            )

        logger.info("\033[34mServer init success, workers: %s, threads: %s \033[0m", worker, thread)
        server.run()

    def run(self):
        """
        start server
        """
        self._eureka_server()
        self._fastapi_server()


class BaseHandler:
    """
    BaseHandler
    """

    def __init__(self, request: FARequest):
        self.infer_request = my_request.Request()
        self.fa_request = request

    async def request_process(self):
        """
        Process incoming request data.

        Returns:
            Tuple[Union[Dict[str, Any], APIResponse], bool]: Parsed request data and success flag.
        """
        is_ok = True
        req_data = {}

        try:
            self.infer_request.header = self.fa_request.headers

            # Query parameters
            self.infer_request.query = self.fa_request.query_params._dict

            # Request body
            self.infer_request.body = await self.fa_request.body()
            content_type = self.infer_request.header.get('Content-Type', "").strip()

            if content_type.startswith('application/x-www-form-urlencoded') or \
                    content_type.startswith('multipart/form-data'):
                form_data = await self.fa_request._get_form()
                self.infer_request.form.get_dict = getattr(form_data, "_dict")
                for k, v in getattr(form_data, "_list"):
                    if isinstance(v, starlette.datastructures.UploadFile):
                        self.infer_request.files[k] = v

                    _data = self.infer_request.form.get(k, [])
                    _data.append(v)
                    self.infer_request.form[k] = _data
                req_data = self.infer_request.form

            elif content_type.startswith('application/json'):
                req_data = await self.fa_request.json()
                self.infer_request.json = req_data

            # If the body is empty, try to get data from query parameters
            if not req_data:
                req_data = self.infer_request.query

        except Exception as e:
            stack = traceback.format_exc()
            req_data = message.APIResponse(
                400, "api", f"API服务请求解析错误: {e}, Body: {str(self.infer_request.body)}, Stack: {stack}")
            is_ok = False

        return req_data, is_ok

    async def response_process(self, data, func, need_feature):
        """
        response process
        """
        # 简单评估下是否为流式请求
        is_stream = isinstance(data, dict) and data.get('stream')

        try:
            result, emsg = await self.fa_request.app.intelliw_setting["infer"].infer(
                data, self.infer_request, func, need_feature, )
            if emsg is None:
                if is_stream and type(result) in (
                        types.GeneratorType, types.AsyncGeneratorType):
                    return result, True
                resp = message.APIResponse(200, "api", '', result)
            else:
                resp = message.APIResponse(500, "api", emsg, result)
        except Exception as e:
            resp = message.APIResponse(
                500, "api", f"API服务处理推理数据错误 {e}")
        return resp, False


async def health_check_handler():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, health_check.health_check_process)
    if result:
        resp = message.HealthCheckResponse(200, "api", 'ok', "")
    else:
        resp = message.HealthCheckResponse(500, "api", 'error', "")
    return FAResponse(content=str(resp), media_type="application/json")


async def eureka_health_check_handler():
    resp = message.HealthCheckResponse(200, "api", 'ok', "")
    return FAResponse(content=str(resp), media_type="application/json")


def get_api_config(request: FARequest):
    api_config = request.app.intelliw_setting[f'api-{request.url.path}']
    return api_config['func'], api_config.get('need_feature', False)


async def api_handler(request: FARequest):
    base = BaseHandler(request)
    result, is_ok = await base.request_process()

    # 进行推理处理
    if is_ok:
        func, need_feature = get_api_config(request)
        result, is_stream = await base.response_process(result, func, need_feature)
        if is_stream:
            return StreamingResponse(result, media_type="text/event-stream")
    return FAResponse(content=str(result), media_type="application/json")
