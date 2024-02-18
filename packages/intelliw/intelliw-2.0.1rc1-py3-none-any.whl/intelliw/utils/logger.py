#!/usr/bin/env python
# coding: utf-8
import time

from intelliw.config import config
import threading
import logging
import logging.handlers
import os
from intelliw.utils.colorlog import ColoredFormatter

framework_logger = None
user_logger = None

default_level = logging.DEBUG
if config.is_server_mode():
    default_level = os.environ.get("intelliw.logger.level", logging.INFO)

default_format = ('[%(process)d] -%(name)s- %(asctime)s '
                  '| %(levelname)4s | %(filename)s:%(lineno)s: %(message)s')

colorful_format = ('%(log_color)s[%(process)d] -%(name)s- %(asctime)s '
                   '| %(levelname)4s | %(filename)s:%(lineno)s: %(message)s')

default_data_format = '%Y-%m-%d %H:%M:%S'
log_path = './logs/'


class EnhancedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=0, utc=0, maxBytes=0):
        """
        This is just a combination of TimedRotatingFileHandler
        and
        RotatingFileHandler (adds maxBytes to TimedRotatingFileHandler)
        """
        logging.handlers.TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay,
                                                           utc)
        self.maxBytes = maxBytes

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        Basically, see if the supplied record would cause the file to exceed
        the size limit we have.

        we are also comparing times
        """
        if self.stream is None:  # delay was set...
            self.stream = self._open()
        if self.maxBytes > 0:  # are we rolling over?
            msg = "%s\n" % self.format(record)
            self.stream.seek(0, 2)  # due to non-posix-compliant Windows feature
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return 1
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        # print "No need to rollover: %d, %d" % (t, self.rolloverAt)
        return 0

    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        if self.stream:
            self.stream.close()
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.baseFilename + "." + time.strftime(self.suffix, timeTuple)
        if self.backupCount > 0:
            cnt = 1
            dfn2 = "%s.%03d" % (dfn, cnt)
            while os.path.exists(dfn2):
                dfn2 = "%s.%03d" % (dfn, cnt)
                cnt += 1
            os.rename(self.baseFilename, dfn2)
            for s in self.getFilesToDelete():
                os.remove(s)
        else:
            if os.path.exists(dfn):
                os.remove(dfn)
            os.rename(self.baseFilename, dfn)
        # print "%s -> %s" % (self.baseFilename, dfn)
        self.mode = 'w'
        self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt

    def getFilesToDelete(self):
        """
        Determine the files to delete when rolling over.

        More specific than the earlier method, which just used glob.glob().
        """
        dirName, baseName = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []
        prefix = baseName + "."
        plen = len(prefix)
        for fileName in fileNames:
            if fileName[:plen] == prefix:
                suffix = fileName[plen:-4]
                if self.extMatch.match(suffix):
                    result.append(os.path.join(dirName, fileName))
        result.sort()
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result


class Logger:
    _instance_lock = threading.Lock()

    def __new__(cls):
        """ 单例,防止调用生成更多 """
        if not hasattr(Logger, "_instance"):
            with Logger._instance_lock:
                if not hasattr(Logger, "_instance"):
                    if not os.path.exists(log_path):
                        os.makedirs(log_path)
                    Logger._instance = object.__new__(cls)
                    Logger.__global_logger(cls)
        return Logger._instance

    def __global_logger(cls):
        root_logger = logging.getLogger()
        root_logger.setLevel(default_level)

        # set up the logger to write into file
        if os.access(log_path, os.W_OK):
            time_file_handler = EnhancedRotatingFileHandler(
                os.path.join(log_path, 'iw-algo-fx.log'),
                when='MIDNIGHT',
                backupCount=15,
                maxBytes=1024 * 1024 * 200  # 300M
            )
            time_file_handler.suffix = '%Y-%m-%d.log'
            time_file_handler.setLevel(default_level)
            time_file_handler.setFormatter(
                logging.Formatter(default_format)
            )
            root_logger.addHandler(time_file_handler)

        # Setup the logger to write into stdout
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(ColoredFormatter(colorful_format))
        root_logger.addHandler(consoleHandler)

        logging.Logger.root = root_logger
        logging.root = logging.Logger.root
        logging.Logger.manager = logging.Manager(logging.Logger.root)

    def __init__(self):
        self.framework_logger = self._get_logger(
            "Framework Log", level=default_level, filename="iw-algo-fx-framework.log")
        self.user_logger = self._get_logger(
            "Algorithm Log", level=default_level, filename="iw-algo-fx-user.log")

    @staticmethod
    def _get_logger(logger_type, level=logging.INFO, format=None, filename=None):
        logger = logging.getLogger(logger_type)
        if logger.handlers:
            return logger

        format = format or default_format
        if filename is not None:
            if os.access(log_path, os.W_OK):
                logging.handlers.RotatingFileHandler
                time_file_handler = EnhancedRotatingFileHandler(
                    os.path.join(log_path, filename),
                    when='MIDNIGHT',
                    backupCount=5,
                    maxBytes=1024 * 1024 * 200  # 300M
                )
                formatter = ColoredFormatter(
                    format, datefmt=default_data_format)
                time_file_handler.suffix = '%Y-%m-%d.log'
                time_file_handler.setLevel(level)
                time_file_handler.setFormatter(formatter)
                logger.addHandler(time_file_handler)
        return logger


def _get_framework_logger():
    global framework_logger
    if framework_logger is None:
        framework_logger = Logger().framework_logger
    return framework_logger


def _get_algorithm_logger():
    global user_logger
    if user_logger is None:
        user_logger = Logger().user_logger
    return user_logger


def get_logger(name: str = "user", level: str = "INFO", format: str = None, filename: str = None):
    """get custom logs

    Args:
        name (str, optional): Logger unique name. Defaults to "user".
        level (str, optional): Logger level. Defaults to "INFO".
        format (str, optional): Format the specified record. Defaults to None.
        filename (str, optional): Save the name of the log file. Defaults to None.

    Returns:
        logger
    """
    return Logger()._get_logger(name, level, format, filename)
