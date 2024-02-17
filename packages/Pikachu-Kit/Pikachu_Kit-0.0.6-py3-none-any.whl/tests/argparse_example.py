# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: argparse_example.py
@time: 2023/11/8 20:38
@desc:

"""
import argparse

# 定义一个函数，接收 xlsx 路径和输出文件夹路径作为参数


def process_data(xlsx_path, output_folder):
    # 在这里编写处理数据的代码，使用 xlsx_path 和 output_folder 参数
    print(xlsx_path, output_folder)


if __name__ == '__main__':

    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='Process xlsx file and specify output folder')

    # 添加参数
    parser.add_argument('-x', dest='xlsx_path', help='path to the xlsx file')
    parser.add_argument('-o', dest='output_folder', help='path to the output folder')

    # 解析命令行参数
    args = parser.parse_args()

    # 调用函数并传递参数
    if args.xlsx_path and args.output_folder:
        process_data(args.xlsx_path, args.output_folder)
    else:
        print("Please provide both -x and -o arguments")
