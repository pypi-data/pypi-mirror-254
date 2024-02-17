# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: test.py
@time: 2023/11/25 10:35
@desc:

"""
import cv2
import os
import numpy as np


class ModelFaceCheck(object):
    """

    """

    def __init__(self, train_path):
        """

        :param train_path:
        """
        self.train_path = train_path
        self.label_to_name = {}
        self.train_date()

    def train_date(self):
        """

        :return:
        """
        known_images = []
        known_labels = []
        current_label = 0
        for filename in os.listdir(known_images_dir):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(known_images_dir, filename)
                image = cv2.imread(image_path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                known_images.append(gray)
                self.label_to_name[current_label] = os.path.splitext(filename)[
                    0]
                known_labels.append(current_label)
                current_label += 1

        self.face_recognizer = cv2.face_LBPHFaceRecognizer.create()
        self.face_recognizer.train(
            known_images, np.array(
                known_labels))
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def scan_unknown_images(self, file):
        unknown_image = cv2.imread(unknown_image_path)
        unknown_gray = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            unknown_gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            face_roi = unknown_gray[y:y + h, x:x + w]
            label, confidence = self.face_recognizer.predict(face_roi)

            if confidence > 50:  # 设置一个阈值来判断识别的准确度
                recognized_name = self.label_to_name[label]
                print(f"识别出的人物是 {recognized_name}，置信度: {confidence}")
                return recognized_name, confidence
            else:
                print("未能识别出人物")
                return "未能识别出人物", 0


if __name__ == '__main__':
    # 已知图像文件所在的目录路径
    known_images_dir = R"F:\Project\GIT\pythondevelopmenttools\tests\faces-check\images"
    unknown_image_path = R"E:\Desktop\linjunjie.jpg"
    # unknown_image_path = R"E:\Desktop\zhoujielun.jpeg"
    mfc = ModelFaceCheck(known_images_dir)
    print(mfc.scan_unknown_images(unknown_image_path))
