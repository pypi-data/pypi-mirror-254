# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: start.py
@time: 2024/1/28 14:35
@desc:

"""
import nmap


import socket

def get_local_ip_address():
    try:
        # 创建一个socket连接
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # 连接到一个公共的IP地址和端口，这里我们使用了Google的DNS服务器地址
        local_ip_address = s.getsockname()[0]  # 获取本地IP地址
        s.close()  # 关闭socket连接
        return local_ip_address
    except Exception as e:
        print("获取本地IP地址失败：", e)


def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        try:
            # 创建一个socket连接
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)  # 设置超时时间为1秒钟
            result = sock.connect_ex((ip, port))  # 尝试连接到指定IP地址和端口
            if result == 0:
                open_ports.append(port)
            sock.close()  # 关闭socket连接
        except Exception as e:
            print("端口扫描出错：", e)

    return open_ports

# 调用函数获取本地IP地址
local_ip = get_local_ip_address()
ip_address = local_ip.split(".")[-2]


# 创建一个nmap扫描对象
nm = nmap.PortScanner()

# 使用nmap扫描局域网
nm.scan(hosts=f'192.168.{ip_address}.0/24', arguments='-sn')


start_port = 1
end_port = 100


# 遍历扫描结果并打印设备的IP地址
for host in nm.all_hosts():
    msg = "发现设备" if host != local_ip else "本机局域网ip"
    print(f'{msg}: {host}')
    # # 执行端口扫描
    # open_ports = scan_ports(local_ip, range(start_port, end_port + 1))
    # print("开放的端口: ", open_ports)


