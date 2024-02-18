#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: ZhiLin Zhang
# Created on: 2023/10/21

from setuptools import setup, find_packages

setup(
    name="tbthematic",  # 这里是pip项目发布的名称
    version="1.2.0",  # 版本号，数值大的会优先被pip
    keywords=("pip", "tbthematic"),
    description="tbthematic",
    license="MIT Licence",
    author="ZhiLin Zhang",
    packages=find_packages(),
    include_package_data=True,
    package_data={},
    install_requires=[],  # 这个项目需要的第三方库
    zip_safe=False
)
