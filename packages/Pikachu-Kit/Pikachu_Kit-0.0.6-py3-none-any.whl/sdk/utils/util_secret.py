# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: util_secret.py
@time: 2024/1/27 23:49
@desc:

"""
# pyotp 2.9.0
import pyotp
import secrets
# python-jose 3.3.0
from jose import jwt, ExpiredSignatureError
from datetime import datetime, timedelta
# passlib 1.7.4
from passlib.context import CryptContext
from sdk.utils.util_encrtpt import EncryptProcess


class TotpHandler(object):
    """
    Totp 验证
    """

    def __init__(self, interval=30):
        """

        """
        # 密钥
        self.secret = "fb565ca799a431a5a4102d10ff84cb3661bb0cf0f415e7" \
                      "8cc389ad42ced61fa4dcb3c635a4f5568697526549ed5dee3" \
                      "a5e791d100ce4f9a95c0728e3b617dc07f575edea41ee6152f08" \
                      "6651719606abba2806ea8845ea4d53a2a91e14c31f1ae825a8c00" \
                      "47b05bf580108cb9af7db40a6ed9f0fb2a1802b6eb1823528b68706b"
        # 过期时间
        self.interval = interval
        # 加密类
        self.ep = EncryptProcess()

    def create_secret(self):
        """
        生成128位随机密钥
        :return:
        """
        return secrets.token_hex(128)

    def create_totp(self):
        """

        :return:
        """
        totp = pyotp.TOTP(self.ep.encode_base32(self.ep.tran_byte_str(self.secret)), interval=self.interval)
        return totp, totp.now()

    def verify(self, totp, key):
        """
        验证
        :param totp:
        :param key:
        :return:
        """
        return totp.verify(key)


class JwtHandler(object):
    """
    JWT 验证
    """

    def __init__(self, interval=30):
        """

        """
        # 密钥
        self.secret = "fb565ca799a431a5a4102d10ff84cb3661bb0cf0f415e7" \
                      "8cc389ad42ced61fa4dcb3c635a4f5568697526549ed5dee3" \
                      "a5e791d100ce4f9a95c0728e3b617dc07f575edea41ee6152f08" \
                      "6651719606abba2806ea8845ea4d53a2a91e14c31f1ae825a8c00" \
                      "47b05bf580108cb9af7db40a6ed9f0fb2a1802b6eb1823528b68706b"
        # 加密算法
        self.algorithm = "HS256"
        # 默认30秒过期
        self.interval = interval
        # 密钥对象
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_hash_code(self, pwd):
        """
        获取密码对应的 hash 值
        :param pwd:
        :return:
        """
        return self.pwd_context.hash(pwd)

    def verify_hash_code(self, pwd, hash_code):
        """
        验证密码和hash是否匹配
        :param pwd:
        :param hash_code:
        :return:
        """
        return self.pwd_context.verify(pwd, hash_code)

    def create_token(self, key: str = None, data: dict = None):
        """
        创建带exp字段的JWT字符串
        :param data:
        :param expires_delta:
        :return:
        """
        if key or data:
            if key:
                to_encode = {"key": key}.copy()
            else:
                to_encode = data.copy()
        else:
            raise ValueError("key or data must exists any")

        expires_delta = timedelta(seconds=self.interval)
        # 这里是utc时间，不是东八区时间
        expire = datetime.utcnow() + expires_delta
        '''
        JWT 是一种跨网络系统之间进行身份验证和授权的标准，它使用的时间默认是 UTC 时间。

        使用 UTC 时间的主要原因是确保在不同的时区和系统之间保持一致性。UTC 时间是一种标准时间，不受时区影响，可以确保在不同的系统和地理位置上都能正确解释和比较时间。

        当生成 JWT 字符串时，将过期时间设定为 UTC 时间可以提供更好的可移植性和一致性。无论何时使用 JWT 进行验证，无论系统所在的时区如何，都可以使用 UTC 时间来检查是否过期。
        '''
        to_encode.update({"expire": expire})
        # SECRET_KEY对声明集进行签名的密钥
        # jwt.encode()对声明集进行编码并返回 JWT 字符串。
        return jwt.encode(to_encode, self.secret, algorithm=self.algorithm)

    def decrypt_token(self, token):
        """
        解析 token
        :param token:
        :return:
        """
        try:
            data = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return data["key"]
        except ExpiredSignatureError:
            return "token time out"
        except KeyError:
            return f"parse error for : {data}"


# if __name__ == '__main__':
#     totp = Totp()
#     t_o,t = totp.create_totp()
#     print(totp.verify(t_o, t))
#     time.sleep(30)
#     print(totp.verify(t_o, t))
#     time.sleep(30)
#     print(totp.verify(t_o, t))
#     time.sleep(30)
#     print(totp.verify(t_o, t))
#
#     form_data = {
#         "username": "johndoe",
#         "password": "Abc123."
#     }
#     jh = JwtHandler()
#     hash_code = jh.get_hash_code(form_data.get("password"))
#     print("hash_code", hash_code)
#     verify = jh.verify_hash_code('asdas', "$2b$12$O42GheSX6NPv/l0A7gb3xeSYn/CG/h9lIX83y9zjTj5.SE1UhNQne")
#     print("verify", verify)
#     token = jh.create_token(form_data.get("username"))
#     print("token", token)
#     print(jh.decrypt_token(token))
#     time.sleep(3)
#     print(jh.decrypt_token(token))
#     time.sleep(35)
#     print(jh.decrypt_token(token))
