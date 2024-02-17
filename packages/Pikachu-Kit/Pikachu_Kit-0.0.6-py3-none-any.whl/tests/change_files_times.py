# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: change_files_times.py
@time: 2023/11/22 11:55
@desc:

"""

import os
import time
import ctypes


def parse_date(date):
    """
    2023-12-12 12:12:12
    """
    head, tail = date.split(" ")
    year, month, day = head.split("-")
    hour, min, sec = tail.split(":")
    return year, month, day, hour, min, sec


def change_file_creation_time(file_path, year, month, day, hour, min, sec):
    """

    """
    new_creation_time = time.mktime((int(year), int(month), int(day), int(hour), int(min), int(sec), 0, 0, 0))
    # 获取文件的修改时间和访问时间
    access_time = os.path.getatime(file_path)
    modified_time = os.path.getmtime(file_path)

    # 修改文件的创建时间
    os.utime(file_path, (access_time, new_creation_time))

    # 如果你还想修改文件的修改时间，可以取消下一行的注释
    # os.utime(file_path, (new_creation_time, new_creation_time))


def change_system_times(year, month, day, hour, min, sec, msec="0"):
    """

    """
    # 定义 SYSTEMTIME 结构体
    class SYSTEMTIME(ctypes.Structure):
        _fields_ = [
            ('wYear', ctypes.c_ushort),
            ('wMonth', ctypes.c_ushort),
            ('wDayOfWeek', ctypes.c_ushort),
            ('wDay', ctypes.c_ushort),
            ('wHour', ctypes.c_ushort),
            ('wMinute', ctypes.c_ushort),
            ('wSecond', ctypes.c_ushort),
            ('wMilliseconds', ctypes.c_ushort)
        ]

    # 设置目标日期
    target_date = SYSTEMTIME(
        wYear=int(year),
        wMonth=int(month),
        wDayOfWeek=0,  # 这里可以忽略，程序会自动填充正确的值
        wDay=int(day),
        wHour=int(hour) - 8,
        wMinute=int(min),
        wSecond=int(sec),
        wMilliseconds=int(msec)
    )

    # 调用 SetSystemTime 函数设置系统日期
    ctypes.windll.kernel32.SetSystemTime(ctypes.byref(target_date))


def cp_files(file, out_path):
    """

    """
    name = os.path.split(file)[-1]
    save_file = os.path.join(out_path, name)
    with open(file, "rb")as fp, \
            open(save_file, "wb")as fp2:
        fp2.write(fp.read())
    return save_file


def main(create_time, change_time, in_file, out_path):
    year, month, day, hour, min, sec = parse_date(create_time)
    change_system_times(year, month, day, hour, min, sec)
    save_file = cp_files(in_file, out_path)
    year, month, day, hour, min, sec = parse_date(change_time)
    change_file_creation_time(save_file, year, month, day, hour, min, sec)


if __name__ == '__main__':
    in_file = input("请输入要修改文件路径：")
    out_path = input("请输入更改时间后文件保存路径:")
    create_time = input("请输入文件创建时间：[2023-12-12 12:12:12]")
    change_time = input("请输入文件修改时间：[2023-12-12 12:12:12]")

    # in_file = R"D:\Desktop\miniblink-20230412\更新日志.txt"
    # out_path = R"D:\Desktop"
    # create_time = "2020-12-12 12:12:12"
    # change_time = "2021-12-12 12:12:12"

    main(create_time, change_time, in_file, out_path)
