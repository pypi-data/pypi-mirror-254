#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: util_bos.py
@time: 2023/5/27 21:12
@desc:
"""
import time
import baidubce
from baidubce.services.sts.sts_client import StsClient
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.services.bos.bos_client import BosClient
from sdk.base.base_bos import BaseBos


class BosAkSk(BaseBos):

    def __init__(self, ):
        super(BosAkSk, self).__init__()
        self.bos_client = None

    def init_bos_client(self):
        """
        初始化 bosclient
        :return:
        """
        if not self.bos_client:
            config = BceClientConfiguration(
                credentials=BceCredentials(
                    self.ak,
                    self.sk
                ),
                protocol=baidubce.protocol.HTTPS,
                endpoint=self.bos_host)
            config = self.Config(config)
            self.bos_client = BosClient(config)

    def upload(self, url, file, status=0):
        """
        上传
        :param url:
        :param file:
        :param status:
        :return:
        """
        bucket_name, key = self.GetBucketKey(url)
        self.init_bos_client()
        return self._upload(self.bos_client, file, bucket_name, key, status)

    def download(self, url, file):
        """
        下载
        :param url:
        :param file:
        :return:
        """
        bucket_name, key = self.GetBucketKey(url)
        self.init_bos_client()
        return self._download(self.bos_client, file, bucket_name, key)

    def get_download_url(self, url):
        """

        """
        bucket_name, key = self.GetBucketKey(url)
        self.init_bos_client()
        return self.bos_client.generate_pre_signed_url(
            bucket_name, key, time.time(), -1).decode("utf-8")


class BosSTS(BaseBos):
    """
    获取 sts
    """

    def __init__(self):
        super(BosSTS, self).__init__()
        self.sts_client = None
        self.bos_client = None
        self.register_time = 0

    def init_sts_client(self):
        """
        初始化 stsclient
        :return:
        """
        def __init():
            config = BceClientConfiguration(
                credentials=BceCredentials(
                    self.ak,
                    self.sk
                ),
                protocol=baidubce.protocol.HTTPS,
                endpoint=self.sts_host)
            self.sts_client = StsClient(config)
            self.register_time = time.time()

        if not self.sts_client:
            __init()
        else:
            now_time = time.time()
            # token 超时 重新初始化
            if now_time - self.register_time >= self.duration_seconds:
                __init()

    def get_sts(self):
        access_dict = {}
        access_dict["service"] = "*"
        access_dict["region"] = "bj"
        access_dict["effect"] = "Allow"
        access_dict["resource"] = ["*"]
        access_dict["permission"] = ["READ", "WRITE"]
        access_control_list = {"accessControlList": [access_dict]}
        # 获取token
        response = self.sts_client.get_session_token(
            acl=access_control_list,
            duration_seconds=self.duration_seconds
        )
        sts_ak = str(response.access_key_id)
        sts_sk = str(response.secret_access_key)
        token = response.session_token
        return (sts_ak, sts_sk, token)

    def init_bos_client(self):
        """
        初始化 bosclient
        :param sts_client:
        :return:
        """
        self.init_sts_client()
        if not self.bos_client:
            sts_ak, sts_sk, token = self.get_sts()
            # 配置BceClientConfiguration
            config = BceClientConfiguration(
                credentials=BceCredentials(sts_ak, sts_sk),
                endpoint=self.bos_host,
                security_token=token
            )
            config = self.Config(config)
            self.bos_client = BosClient(config)

    def download(self, url, file):
        """
        下载
        :param url:
        :param file:
        :return:
        """
        bucket_name, key = self.GetBucketKey(url)
        self.init_bos_client()
        return self._download(self.bos_client, file, bucket_name, key)

    def upload(self, url, file, status=0):
        """
        上传
        :param url:
        :param file:
        :param status:
        :return:
        """
        bucket_name, key = self.GetBucketKey(url)
        self.init_bos_client()
        return self._upload(self.bos_client, file, bucket_name, key, status)

    def get_download_url(self, url):
        """

        """
        bucket_name, key = self.GetBucketKey(url)
        self.init_bos_client()
        return self.bos_client.generate_pre_signed_url(
            bucket_name, key, time.time(), -1).decode("utf-8")
