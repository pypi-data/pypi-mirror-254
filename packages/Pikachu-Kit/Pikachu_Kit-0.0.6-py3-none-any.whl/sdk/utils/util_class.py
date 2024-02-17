# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: util_class.py
@time: 2024/1/16 17:06
@desc:

"""
import os


class PathParser(object):
    """
    path 解析相关类
    """

    def __init__(self, path):
        """

        :param path:
        """
        self.path = os.path.abspath(path)
        self.tail = os.path.splitext(self.path)[-1][1:]
        self.name = os.path.basename(self.path).split(".")[0]
        self.header = os.path.dirname(self.path)

    def __str__(self):
        """
        print() 自动调用
        :return:
        """
        return f"Path: {self.path}\nTail: {self.tail}\nName: {self.name}\nHeader: {self.header}"


class PathMerge(object):
    """
    path 合并类
    """

    def __init__(self, path: PathParser = None, header=None, name=None, tail=None, create=False):
        """

        :param path:
        :param header:
        :param name:
        :param tail:
        :param create:
        """
        if path:
            self.header = path.header
            self.name = path.name
            self.tail = path.tail
        else:
            if header and name and tail:
                self.header = header
                self.name = name
                self.tail = tail
            else:
                raise ValueError("PathParser: 参数不完整 header, tail, name")
        if create:
            os.makedirs(self.header, exist_ok=True)
        self.path = f"{self.header}{os.sep}{self.name}.{self.tail}"

    def __str__(self):
        """
        print() 自动调用
        :return:
        """
        return f"Path: {self.path}"


class URLParser(object):
    """
    URL 解析相关类
    """

    def __init__(self, url):
        """

        :param url:
        """
        self.url = url
        url_split_double = url.split("://")
        url_split_single = url_split_double[1].split("/")
        self.protocol = url_split_double[0]
        self.host = url_split_single[0]
        self.path_lis = url_split_single[1:-1]
        self.path = "/".join(self.path_lis)
        try:
            self.name, self.tail = url_split_single[-1].split(".")
        except BaseException:
            self.name = url_split_single[-1].split(".")[0]
            self.tail = ""

    def __str__(self):
        """
        print() 自动调用
        :return:
        """
        return f"URL: {self.url}\nPROTOCOL: {self.protocol}\nHOST: {self.host}\nPATH: {self.path}\nPATH_LIS: {self.path_lis}\nNAME: {self.name}\nTAIL: {self.tail}"


class UrlMerge(object):
    """
    URL 合并类
    """

    def __init__(self, protocol=None, host=None, path=None, name=None, tail="", obj: URLParser = None):
        """

        :param protocol:
        :param host:
        :param path:
        :param name:
        :param tail:
        :param obj:
        """
        if obj:
            self.protocol = obj.protocol
            self.host = obj.host
            self.path = obj.path
            self.name = obj.name
            self.tail = obj.tail
        else:
            if protocol and host and path and name:
                self.protocol = protocol
                self.host = host
                self.path = path
                self.name = name
                self.tail = tail
                self.url = f"{self.protocol}://{self.host}/{self.path}/{self.name}.{self.tail}"
            else:
                raise ValueError("URLMERGE: 参数不完整 protocol, host, path, name")
            self.protocol = protocol
            self.host = host
            self.path = path
            self.name = name
            self.tail = tail
        if self.tail:
            self.url = f"{self.protocol}://{self.host}/{self.path}/{self.name}.{self.tail}"
        else:
            self.url = f"{self.protocol}://{self.host}/{self.path}/{self.name}"

    def __str__(self):
        """
        print() 自动调用
        :return:
        """
        return f"URL: {self.url}"
