# coding: utf8
"""
@ File: _source.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubunut 22.04.4 Kernel 6.2.0-36-generic 
@ CreatedTime: 2023/11/26
"""
from __future__ import annotations


import sys
import warnings
import platform
import asyncio


sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from typing import Union, Any, Callable
from types import FunctionType, MethodType

from datetime import datetime
import time
import re

from fairyland.framework.utils.abnormal import ParameterError


class DateTimeUtils:
    """Date Time"""

    @staticmethod
    def normtimestamp():
        """
        Standard 10-bit timestamps
        @return: 10-bit timestamps: Integer
        """
        return time.time().__int__()

    @staticmethod
    def normdatetime():
        """
        Formatting Date Time : fmt: "%Y-%m-%d %H:%M:%S"
        @return: Fmt datetime: String
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def timestamp_nbit(n: int) -> str:
        """
        n-bit timestamps
        @param n: n-bit: Integer
        @return: n-bit timestamps: String
        """
        if not isinstance(n, int):
            raise TypeError
        timestamp_str = time.time().__str__().replace(".", "")
        if n <= 16:
            result = timestamp_str[:n]
        else:
            result = "".join(
                (
                    timestamp_str,
                    (n - len(timestamp_str)) * "0",
                )
            )
        return result

    @staticmethod
    def timestamp_dt(fmt: Union[str, None] = None) -> int:
        """
        Datetime to timestamps
        @param fmt: At least 14-bits of time and date: String
        @return: Standard 10-bit timestamp: Integer
        """
        if fmt:
            data_string = "".join(re.findall(r"\d+", fmt))
            if data_string.__len__() == 14:
                fmt = "{}-{}-{} {}:{}:{}".format(
                    data_string[:4],
                    data_string[4:6],
                    data_string[6:8],
                    data_string[8:10],
                    data_string[10:12],
                    data_string[12:14],
                )
                results = datetime.strptime(fmt, "%Y-%m-%d %H:%M:%S").timestamp().__int__()
            else:
                raise ParameterError
        else:
            results = time.time().__int__()
        return results

    @staticmethod
    def datetime_ts(timestamp: Union[int, str, float, None] = None, fmt: str = "%Y-%m-%d %H:%M:%S"):
        """
        Timestamps to fmt datetime
        @param timestamp: timestamps: Integer | String
        @param fmt: Fmt datetime, default: %Y-%m-%d %H:%M:%S: String
        @return: Fmt datetime: String
        """
        if timestamp:
            results = datetime.fromtimestamp(timestamp).strftime(fmt)
        else:
            results = datetime.now().strftime(fmt)
        return results
