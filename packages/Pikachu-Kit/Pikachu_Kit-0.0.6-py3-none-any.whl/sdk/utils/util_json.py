#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: util_json.py
@time: 2023/5/27 22:41
@desc:
"""
import json


class JsonProcess():
    """
    json 序列化 反序列化
    """

    def loads(self, data: str) -> dict:
        """
        str - dict
        :param data:
        :return:
        """
        return json.loads(data, strict=False)

    def dumps(self, data: dict, indent: None = 4,
              ensure_ascii: bool = False) -> str:
        """
        dict-str
        :param data:
        :param indent:
        :param ensure_ascii:
        :return:
        """
        return json.dumps(data, indent=indent, ensure_ascii=ensure_ascii)
