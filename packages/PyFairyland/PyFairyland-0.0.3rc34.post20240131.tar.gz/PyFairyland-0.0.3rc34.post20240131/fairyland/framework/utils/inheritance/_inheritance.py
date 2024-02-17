# coding: utf8
""" 
@File: _inheritance.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-27
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Inheritance:
    def __init__(self, root_path: str):
        self.__root_path = root_path

    @property
    def root_path(self):
        return self.__root_path

    @root_path.setter
    def root_path(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__root_path = value
