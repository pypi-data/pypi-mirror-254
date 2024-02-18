#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: duanliangcong
# Mail: 137562703@qq.com
# Created Time:  2022-11-02 15:00:00
#############################################

# pip install twine
# python setup.py sdist
# twine upload dist/*

#############################################
#################使用方法#####################
#############################################
'''
目录结构
UPSDIST
    ddreport        库文件夹
    MANIFEST.in     配置
    setup.py        当前文件

1.cmd进入UPSDIST目录
2.执行命令：python setup.py sdist
3.执行命令：twine upload dist/*
'''



#### 每次更新需要修改 version 字段

from setuptools import setup, find_packages, find_namespace_packages

setup(
    name = "ddreport",
    version = "4.5",
    # keywords = ("pip", "pytest","testReport"),
    description = "pytest测试报告",
    long_description = "1.当请求成功时，编辑信息头将不会再覆盖请求时设置的信息头内容; 2.关键字改为小写（API->api, GVALUE->gval, FC->fc, MYSQL->mysql）; 3.一条用例支持多个参数化; 4.重写动态参数化实现逻辑",
    license = "MIT Licence",

    url = "https://blog.csdn.net/weixin_43975720/article/details/130559489",
    author = "duanliangcong",
    author_email = "137562703@qq.com",
    entry_points={"pytest11": ["test_report=ddreport.testReport"]},

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["pytest", "requests", "sshtunnel", "pymysql", "jsonpath", 'openpyxl', 'deepdiff'],
)
