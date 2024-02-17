# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: get_coogle_translate_results.py
@time: 2022/11/12/ 22:12
@desc:
"""
import os
import requests
import json
import xlsxwriter
import xlrd
import time
import random


class Translation():
    """

    """

    def parse_streaming_data(self, data, question):
        for line in data.split('\n'):
            if line.strip():
                if line.startswith("data: "):
                    message = json.loads(line.replace("data: ", ""))
                    event = message["data"]["event"]
                    if event == "Translating":
                        question = message["data"]["list"][0]["src"]
                        answer = message["data"]["list"][0]["dst"]
                        # print("{} : {}".format(question,answer))
                        return {
                            "question": question,
                            "answer": answer
                        }

        return {
            "question": question,
            "answer": "翻译失败"
        }

    def translate(self, question):
        tran_result = {
            "question": question,
            "answer": "翻译失败"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

        url = "https://fanyi.baidu.com/ait/text/translate"
        data = {
            "query": "{}".format(question),
            "from": "en",
            "to": "zh",

        }
        try:
            response = requests.post(url, headers=headers, json=data)
            # print(response.text)
            tran_result = self.parse_streaming_data(response.text, question)
        except BaseException:
            pass

        time.sleep(random.randint(10, 20))
        return tran_result

    def read_yield(self, file: str, headers: list = None, sheets: list = None):
        """
        按行读取excel
        :param file:
        :param headers:[[],[]]每个sheet对应一个header
        :param encoding:
        :param spliter:
        :param sheets:
        :return:
        """
        data = xlrd.open_workbook(file)
        if not sheets:
            sheets = data.sheet_names()
        for index, sheet in enumerate(sheets):
            table = data.sheet_by_name(sheet)
            nrows = table.nrows
            # 传headers进来从第1行开始算，不传从第2行开始算
            if not headers:
                header = table.row_values(0)
                start = 1
            else:
                header = headers[index]
                start = 0
            num = 0
            for row in range(start, nrows):
                info = []
                for i in table.row_values(row):
                    if isinstance(i, str):
                        info.append(i)
                    else:
                        if str(i).endswith(".0"):
                            info.append(str(int(i)))
                        else:
                            info.append(str(i))
                num += 1

                yield {
                    "sheet": sheet,
                    "headers": header,
                    "num": num,
                    "line": info,
                }

    def write(self, file: str, data, headers, sheets):
        workbook = xlsxwriter.Workbook(file)
        for index, sheet in enumerate(sheets):
            worksheet = workbook.add_worksheet(sheet)
            data.insert(0, headers[0])
            for row, lis in enumerate(data):
                for col, val in enumerate(lis):
                    # header 样式
                    worksheet.write_string(
                        row=row,
                        col=col,
                        string=str(val)
                    )
        workbook.close()

    def process(self, **kwargs):
        in_file = kwargs["in_file"]
        name = in_file.split(os.sep)[-1].split(".")[0]
        out_lis = []
        headers = [["内容", "序号", "翻译"]]
        num = 0
        for args in self.read_yield(in_file):
            chinese_col = args["line"][args["headers"].index("内容")]
            if chinese_col:
                num += 1
                tran_result = self.translate(chinese_col)
                question = tran_result["question"]
                answer = tran_result["answer"]
                print(question, answer)
                out_lis.append([question, str(num), answer])

        self.write("{}_result.xlsx".format(name), data=out_lis, headers=headers, sheets=["Sheet1"])


if __name__ == '__main__':
    t = Translation()
    # in_file = R"D:\Desktop\4\图片映射表 .xlsx"
    in_file = input("输入待处理文件路径:")
    t.process(in_file=in_file)
