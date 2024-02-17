#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: load_env.py
@time: 2023/6/11 21:33
@desc:
"""
import os
from dotenv import load_dotenv


class LoadEnv():
    def __init__(self):
        pass

    def load_env(self, key):
        load_dotenv()
        args = os.getenv(key)
        if not args:
            raise ValueError("Not Found .env")
        else:
            return args
