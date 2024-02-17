# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author  : v_jiaohaicheng@baidu.com
@des     :

"""
import copy
import random
import time
import datetime
import traceback
import uuid
from functools import wraps
from cup.util import ThreadPool


class SingletonDecorator:
    def __init__(self, cls):
        self._cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self._cls(*args, **kwargs)
        return self.instance


@SingletonDecorator
class DecorateMutithread(object):
    """
    多线程装饰器(线程池实现)
    """

    def __init__(self, maxthreads=10):
        """
        初始化线程池
        """
        self.pool = ThreadPool(minthreads=3, maxthreads=maxthreads, daemon_threads=True)
        self.pool.start()

    def callback(self, status, result):
        """
        默认回调函数
        :param status:
        :param result:
        :return:
        """
        print(status, result)

    def add_project(self):
        """
        装饰器函数
        :return:
        """
        def decorate(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return self.pool.add_1job_with_callback(self.callback, func, *args, **kwargs)
            return wrapper
        return decorate

    def get_pool_status(self):
        """
        获取线程池状态
        :return:
        """
        return self.pool.get_stats()

    def start_pool(self):
        """
        开始 pool
        :return:
        """
        self.pool.start()

    def close_pool(self):
        """
        关闭 pool
        :return:
        """
        self.pool.stop()


class DecorateFunction(object):
    """
    函数运行装饰器
    """

    def __init__(self, **kwargs):
        self.__dict__.update({k: v for k, v in [
                             i for i in locals().values() if isinstance(i, dict)][0].items()})

    def __call__(self, func):
        """
        计算程序运行时间，及记录程序开始和结束状态，装饰器
        :param func:
        :return:
        """
        @wraps(func)
        def decorate(*args, **kwargs):
            func_single = uuid.uuid4()
            func_name = func.__name__
            start_time = self.func_start(func_single, func_name)
            result = func(*args, **kwargs)
            end_time = self.func_start(func_single, func_name)
            self.diff_start_end(func_name, start_time, end_time)
            return result
        return decorate

    def func_start(self, single, name):
        """
        程序开始
        :param single:
        :param name:
        :return:
        """
        start_time = time.time()
        print("{}-{}-{}-函数开始".format(single, datetime.datetime.now(), name))
        return start_time

    def func_end(self, single, name):
        """
        程序开始
        :param single:
        :param name:
        :return:
        """
        func_end = time.time()
        print("{}-{}-{}-函数结束".format(single, datetime.datetime.now(), name))
        return func_end

    def diff_start_end(self, name, start, end):
        """

        :param start:
        :param end:
        :return:
        """
        print("函数{}总执行时间:{}".format(name, end - start))


def retry(**params):
    """
    重试装饰器
    :param retry: 重试次数，默认为3
    :param sleep: 重试之间的最大等待时间，默认为3秒
    :return:
    """
    def _get_args(params):
        """
        解析参数
        :param params:
        :return:
        """
        if params.get("retry") is None:
            retry = 3
        else:
            retry = params["retry"]
        result = f"重试次数:{retry} 用尽"
        if params.get("sleep") is None:
            sleep = 3
        else:
            sleep = params.get("sleep")
        # 复制重试次数以便输出剩余重试次数
        _retry = copy.deepcopy(retry)
        return retry, sleep, _retry, result

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            flag = False
            retry, sleep, _retry, result = _get_args(params)
            while retry > 0:
                try:
                    result = func(*args, **kwargs)
                    flag = True
                    return flag, result  # 直接返回原函数的执行结果
                except BaseException:  # 捕获所有异常
                    #
                    retry -= 1
                    # print("重试:{}".format(_retry - retry))
                    if retry == 0:
                        # raise e  # 如果重试次数用尽，则抛出异常
                        print(traceback.format_exc())
                        return flag, result
                finally:
                    time.sleep(random.randint(1, sleep))  # 重试间隔随机等待
        return wrapper
    return decorate
