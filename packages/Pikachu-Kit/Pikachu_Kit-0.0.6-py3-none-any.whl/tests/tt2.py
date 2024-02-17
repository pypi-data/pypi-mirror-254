# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: tt2.py
@time: 2023/10/31 11:53
@desc:

"""
from dateutil import relativedelta
from datetime import datetime


def get_precis_diff_times(time1, time2):
    """
      2023-12-12 34:56:03
    """
    def split_times(_time):
        date1, date2 = _time.split(" ")
        year, month, day = date1.split("-")
        hour, minute, second = date2.split(":")
        return int(year), int(month), int(day), int(hour), int(minute), int(second)

    year, month, day, hour, minute, second = split_times(time1)
    _time1 = datetime(year, month, day, hour, minute, second)
    year, month, day, hour, minute, second = split_times(time2)
    _time2 = datetime(year, month, day, hour, minute, second)

    delta = relativedelta.relativedelta(_time2, _time1)

    return f"相差:{delta.years}年 {delta.months}月 {delta.days}天 {delta.hours}小时 {delta.minutes}分钟 {delta.seconds}秒"


print(get_precis_diff_times(time1="2023-12-12 04:56:03", time2="2024-12-12 12:56:03"))
