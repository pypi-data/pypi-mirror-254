# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: daili.py
@time: 2023/11/30 13:13
@desc:

"""
# http://api.dmdaili.com/dmgetip.asp?apikey=1e616471&pwd=b903cfc18460e22fcf5c55414487f8b6&getnum=200&httptype=1&geshi=2&fenge=4&fengefu=&Contenttype=1&operate=all

import requests


url = "http://api.dmdaili.com/dmgetip.asp?apikey=1e616471&pwd=b903cfc18460e22fcf5c55414487f8b6&getnum=200&httptype=2&geshi=2&fenge=4&fengefu=&Contenttype=1&operate=all"
req_url = "https://spidertools.cn/#/formatJSON"
while True:

    res = requests.get(url)
    data = res.json()
    for i in data["data"]:
        print(i["ip"], i["port"])

        proxies = {
            "http": "http://" + i["ip"] + ":" + str(i["port"]),
            "https": "http://" + i["ip"] + ":" + str(i["port"])
        }
        try:
            res = requests.get(req_url, proxies=proxies, timeout=(0.5, 0.1))
            res.encoding = "utf-8"
            print(res.text)
        except Exception as e:
            print(e)
