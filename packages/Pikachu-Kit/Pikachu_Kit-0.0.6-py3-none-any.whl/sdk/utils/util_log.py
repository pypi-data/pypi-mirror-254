# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@contact: JHC000abc@gmail.com
@time: 2023/2/11 17:41 $
@desc:

"""
import os
import logging
import datetime
from logging.handlers import TimedRotatingFileHandler, BaseRotatingHandler
import time
from nb_log import get_logger


class BiuLog():
    """
    nblog 实现，支持多进程安全
    """

    def __init__(self, normal="debug", file="file", email="email"):
        self.normal = normal
        self.file = file
        self.email = email

    @staticmethod
    def get_logger():
        """
            logger_debug 仅控制台输出
            logger_file 仅文件输出
            logger_email 仅邮件输出
            logger_recode 文件,控制台输出
        """

        biulog = BiuLog()
        logger_debug = get_logger(name=biulog.normal, formatter_template=1, log_file_handler_type=2)
        logger_recode = get_logger(name=biulog.file, is_add_stream_handler=True, log_path="./log", log_filename="file_{}.log".format(biulog.file),
                                   log_file_handler_type=2)
        logger_file = get_logger(name=biulog.file, is_add_stream_handler=False, log_path="./log", log_filename="file_{}.log".format(biulog.file),
                                 log_file_handler_type=2)
        logger_email = get_logger(name=biulog.email, is_add_stream_handler=False, is_add_mail_handler=True)

        return logger_debug, logger_recode, logger_file, logger_email


class MultiTimedRotatingFileHandler(TimedRotatingFileHandler):
    """
    重写TimedRotatingFileHandler下的doRollover()方法
    支持 多线程 写入，切割日志不冲突
    """

    def doRollover(self) -> None:
        if self.stream:
            self.stream.close()
            self.stream = None
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
        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, timeTuple))
        if os.path.exists(dfn):
            os.remove(dfn)
        # self.rotate(self.baseFilename, dfn)
        single = False
        while not single:
            try:
                self.rotate(self.baseFilename, dfn)
                single = True
            except BaseException:
                pass
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'M' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:           # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt


class ProTimeRotatingFileHandler(BaseRotatingHandler):
    def __init__(self, filename, encoding=None, when="D"):
        """
        支持按天，小时，分钟，秒切割
        :param filename:
        :param encoding:
        :param when:
        """
        if when == "D":
            self.suffix = "%Y-%m-%d"
        elif when == "H":
            self.suffix = "%Y-%m-%d %H"
        elif when == "M":
            self.suffix = "%Y-%m-%d %H-%M"
        elif when == "S":
            self.suffix = "%Y-%m-%d %H-%M-%S"

        self.date = datetime.datetime.now()
        super(
            ProTimeRotatingFileHandler,
            self).__init__(
            filename,
            mode="a",
            encoding=encoding,
            delay=False)

    def shouldRollover(self, record):
        return self.date != datetime.datetime.now()

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        self.date = datetime.datetime.now()

    def _open(self):
        filename = '%s.%s' % (self.baseFilename,
                              self.date.strftime(self.suffix))
        stream = open(file=filename, mode=self.mode, encoding=self.encoding)
        if os.path.exists(self.baseFilename):
            try:
                os.remove(self.baseFilename)
            except OSError:
                pass
        try:
            os.symlink(filename, self.baseFilename)
        except OSError:
            pass
        return stream


class LoggingProcess():
    """

    """

    def __init__(self, file="./log/log.log", sign="default"):
        super(LoggingProcess, self).__init__()
        os.makedirs(os.path.split(file)[0], exist_ok=True)
        self.sign = sign
        self.file = file
        self.when = "D"
        self.backupCount = 7
        self.logger = None

    def get_logger(self, mode="T"):
        """

        :param mode:
        :return:
        """

        if not self.logger:
            if mode == "T":
                self._init_logger()
            elif mode == "M":
                self._init_logger_m()
        return self.logger

    def _init_logger_m(self):
        """

        :return:
        """
        logger = logging.getLogger(self.sign)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        console_handler = logging.StreamHandler()
        file_handler = ProTimeRotatingFileHandler(
            filename=self.file,
            encoding="utf-8",
            when=self.when
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        self.logger = logger
        return logger

    def _init_logger(self):
        """

        :return:
        """
        logger = logging.getLogger(self.sign)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        console_handler = logging.StreamHandler()
        file_handler = MultiTimedRotatingFileHandler(
            filename=self.file,
            when=self.when,
            encoding="utf-8",
            backupCount=self.backupCount,
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        self.logger = logger
        return logger
