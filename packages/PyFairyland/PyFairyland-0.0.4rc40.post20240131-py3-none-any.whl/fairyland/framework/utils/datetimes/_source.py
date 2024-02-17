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

from datetime import datetime, timedelta
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
            raise TypeError("The n argument must be of type int.")
        timestamp_str = time.time().__str__().replace(".", "")
        if n <= 16:
            result = timestamp_str[:n]
        else:
            result = "".join((timestamp_str, (n - len(timestamp_str)) * "0"))
        return result

    @staticmethod
    def timestamp_dt(normdatetime: Union[str, None] = None) -> int:
        """
        Datetime to timestamps
        @param normdatetime: At least 14-bits of time and date: String
        @return: Standard 10-bit timestamp: Integer
        """
        if normdatetime:
            data_string = "".join(re.findall(r"\d+", normdatetime))
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
                raise ParameterError(
                    "The parameter length should be 14 digits. "
                    "With the first four digits representing the year and "
                    "the next two digits representing the month, day, hour, minute, and second."
                )
        else:
            results = time.time().__int__()
        return results

    @staticmethod
    def datetime_ts(timestamp: Union[int, str, float, None] = None, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
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

    @staticmethod
    def datetimedelta_days(normdatetime: str) -> int:
        """
        Calculate the difference in days between the given date and the current date.
        @param normdatetime: The normalized date in the format 'YYYY-MM-DD'.
        @type normdatetime: str
        @return: The difference in days.
        @rtype: int
        """
        if not isinstance(normdatetime, str):
            raise TypeError("The normdatetime argument must be of type str.")
        try:
            given_date = datetime.strptime(normdatetime, "%Y-%m-%d")
        except Exception:
            raise ValueError("Invalid date format. The date should be in the format 'YYYY-MM-DD'.")
        delta = datetime.now() - given_date
        return delta.days

    @staticmethod
    def datetimerelative(days: int):
        """
        Calculate the date that is 'days' days away from the current date.
        @param days: The number of days, positive or negative.
        @type days: int
        @return: The calculated date.
        @rtype: datetime
        """
        if not isinstance(days, int):
            raise TypeError("The days argument must be of type int.")
        current_date = datetime.now()
        delta = timedelta(days=days)
        relative_date = current_date + delta
        return relative_date
