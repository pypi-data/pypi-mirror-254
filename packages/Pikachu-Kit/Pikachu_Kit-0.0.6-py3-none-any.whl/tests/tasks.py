# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: app.py
@time: 2024/1/13 11:26
@desc:

"""
import time

from celery import Celery
broker = 'redis://:123456@localhost:6379/0'
backend = 'redis://:123456@localhost:6379/1'
app = Celery('tasks', broker=broker,backend=backend)


@app.task
def add(x, y):
    time.sleep(5)     # 模拟耗时操作
    print(x + y)
    return x + y


if __name__ == '__main__':
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))
    print(add.delay(1, 2))

