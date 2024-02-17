# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: demo2.py
@time: 2023/11/22 16:59
@desc:

"""

# 写一段支持win10系统解压zip,rar,gz压缩包的代码，支持各种后缀压缩包嵌套解压，且解压后目录层级不变
import os
import zipfile
import gzip
import shutil
import rarfile
from sdk.utils.util_folder import FolderProcess
from sdk.utils.util_file import FileProcess


class Process():
    def __init__(self):
        self.folder = FolderProcess()
        self.file = FileProcess()
        self.format = [".zip", ".rar", ".gz"]

    def check_zip_files(self, save_folder):
        """

        :return:
        """
        for args in self.folder.get_all_files(save_folder):
            print(args)
            tail = self.file.get_file_tail(args["file"])
            if tail in self.format:
                self.unzip(args["file"], os.sep.join(self.folder.split_path(args["file"])[:-1]))

    def unzip(self, zip_file: str, save_path: str = "./"):
        """
        解压
        :param zip_file:
        :param save_path:可以不存在
        :return:
        """
        file_split = self.folder.split_path(zip_file)
        save_folder = self.folder.merge_path([save_path, file_split[-1].split(".")[0]])
        self.folder.create_folder(save_folder)

        file_name = file_split[-1]
        print("file_name", file_name)

        if zip_file.lower().endswith(".zip"):
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(save_folder)
        elif zip_file.lower().endswith(".rar"):
            with rarfile.RarFile(zip_file) as rar_file:
                rar_file.extractall(save_folder)
        elif zip_file.lower().endswith(".gz"):
            with gzip.open(zip_file, 'rb') as gz_file, \
                    open(self.folder.merge_path([save_folder, file_name]), 'wb') as output_file:
                output_file.write(gz_file.read())
        else:
            print("不支持的格式:{}".format(zip_file))

        self.folder.remove(zip_file)
        self.check_zip_files(save_folder)


p = Process()
p.unzip(R"E:\Desktop\test.zip", R"E:\Desktop\1")
# for i in os.listdir(R"E:\Desktop\test"):
#     print(i)
