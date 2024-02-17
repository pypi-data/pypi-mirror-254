# coding: utf8
""" 
@File: __init__.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-12
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


from ._database import BaseDataSourceUtils
from ._database import MySQLUtils
from ._database import PostgreSQLUtils

__all__ = [
    "BaseDataSourceUtils",
    "MySQLUtils",
    "PostgreSQLUtils",
]
