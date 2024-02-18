#!/usr/bin/env python
# coding: utf-8
from intelliw.interface.controller import FrameworkArgs, __parse_args
from intelliw.config import config
from intelliw.utils.logger import _get_framework_logger
from intelliw.interface.apihandler import ApiService

logger = _get_framework_logger()


framework_args = FrameworkArgs(__parse_args())
config.update_by_env()
config.FRAMEWORK_MODE = "infer"
api_service = ApiService(framework_args.port, framework_args.path, framework_args.response)


if __name__ == '__main__':
    api_service.run()
