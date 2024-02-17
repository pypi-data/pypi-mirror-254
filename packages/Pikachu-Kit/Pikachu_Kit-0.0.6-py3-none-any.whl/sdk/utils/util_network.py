# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: util_network.py
@time: 2023/7/30 22:37
@desc:

"""
import requests
from .util_decorate import retry
from urllib3.exceptions import InsecureRequestWarning


# 禁用 InsecureRequestWarning 警告
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class NetWorkRequests(object):
    """

    """
    @retry(retry=3)
    def _requests(self, url, headers=None, params=None, cookies=None, timeout=5,
                  data=None, json=None, method="POST", stream=False, proxies=None):
        """

        :param url:
        :param headers:
        :param params:
        :param cookies:
        :param timeout:
        :param data:
        :param json:
        :param method:
        :param stream:
        :param proxies:
        :return:
        """
        if method == "POST":
            response = requests.post(
                url=url,
                data=data,
                json=json,
                stream=stream,
                cookies=cookies,
                headers=headers,
                proxies=proxies,
                timeout=timeout,
                verify=False
            )
        elif method == "GET":
            response = requests.get(
                url=url,
                params=params,
                stream=stream,
                cookies=cookies,
                headers=headers,
                proxies=proxies,
                timeout=timeout,
                verify=False
            )
        else:
            raise ValueError("ERROR Methods {}".format(method))
        return response

    def download_videos(self, url, file, max_size=102400, method="GET"):
        """

        :param url:
        :param file:
        :param max_size:
        :param method:
        :return:
        """
        res = {
            "status": -1,
            "url": url,
            "msg": "Failed",
            "result": []
        }
        response = self._requests(url, method=method)
        if response["status"] == -1:
            msg = "Failed"
        else:
            download_status_all = True
            content_len = int(response["msg"].headers["Content-Length"])
            nums = content_len // max_size if content_len % max_size == 0 else content_len // max_size + 1
            res["content_len"] = content_len
            res["split_nums"] = nums
            with open(file, "ab+")as fp:
                for i in range(nums):
                    start, end = i * max_size, (i + 1) * max_size
                    headers = {
                        "Range": "bytes={}-{}".format(start, end)
                    }
                    response = self._requests(
                        url, headers=headers, stream=True, method=method)
                    chunk_status = response["status"]
                    if chunk_status == -1:
                        download_status_all = False
                    else:
                        for chunk in response["msg"].iter_content(
                                chunk_size=max_size):
                            fp.seek(start)
                            fp.write(chunk)
                    res["result"].append({
                        "status": chunk_status,
                        "during": [start, end],
                    })
            if download_status_all:
                msg = "Success"
                res["status"] = 0
            else:
                msg = "Failed"

        res["msg"] = msg

        return res
