#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: util_single.py
@time: 2023/6/13 23:26
@desc: 单例实现
"""
from functools import wraps


def single(cls):
    """
    装饰类
    :param cls:
    :return:
    """
    instance = {}

    @wraps(cls)
    def decorate(*args, **kwargs):
        if instance.get(cls) is None:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return decorate


def single_params(**params):
    """
    带参装饰器
    :param params:
    :return:
    """
    instance = {}

    def decorate(cls):
        @wraps(cls)
        def dec(*args, **kwargs):
            if instance.get(cls) is None:
                instance[cls] = cls(*args, **kwargs)
            print("params", params)
            return instance[cls]
        return dec
    return decorate
