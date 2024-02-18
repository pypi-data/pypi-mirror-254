# coding: utf8
"""
@ File: tools.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubunut 22.04.4 Kernel 6.2.0-36-generic 
@ CreatedTime: 2023/12/21
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

from typing import Union


class SQLStatement:
    def __init__(
        self,
        database_name: Union[str, None] = None,
        schema_name: Union[str, None] = None,
        table_name: Union[str, None] = None,
    ):
        self.__database_name = database_name
        self.__schema_name = schema_name
        self.__table_name = table_name
        __check_state, __check_db_name = self.__check_initialization()
        if not __check_state:
            raise ValueError("Initialization failure, parameter error.")
        else:
            self.__db_name = __check_db_name

    @property
    def database_name(self):
        return self.__db_name

    @property
    def schema_name(self):
        return self.__db_name

    def __check_initialization(self):
        state, db_name = False, None
        if not self.__database_name:
            if not self.__schema_name:
                state = False
                db_name = None
            else:
                state = True
                db_name = self.__schema_name
        else:
            if not self.__schema_name:
                state = True
                db_name = self.__database_name
            else:
                state = False
                db_name = None
        return state, db_name

    def __select_clause(
        self,
        table_name: Union[str, None] = None,
        field: Union[str, list[str], tuple[str], set[str], None] = None,
    ) -> str:
        if self.__table_name:
            table_name = self.__table_name
        else:
            if not table_name:
                raise ValueError
        if not field:
            field = "*"
        else:
            if not isinstance(field, (list, tuple, set)):
                if not isinstance(field, str):
                    raise TypeError
            else:
                field = " ".join(field)
        select_str = "{}.{}.{}".format(self.database_name, table_name, field)
        results = " ".join(("select", select_str))
        return results

    def select_clause_example(self):
        return self.__select_clause

    @staticmethod
    def select_clause(field_iterable: Union[str, list[str], tuple[str], set[str], None] = None) -> str:
        if not field_iterable:
            results = "select *"
        else:
            if not isinstance(field_iterable, (list, tuple, set)):
                results = "select {}".format(field_iterable)
            else:
                if not isinstance(field_iterable, str):
                    raise TypeError
                field_str = " ".join(field_iterable)
                results = " ".join(("select", field_str))
        return results

    @staticmethod
    def from_clause(table: str, database: Union[str, None] = None, schema: Union[str, None] = None) -> str:
        if not database and not schema:
            raise ValueError
        if database and schema:
            raise ValueError
        if not table:
            raise ValueError
        if not isinstance(table, str):
            raise TypeError
        if database:
            if not isinstance(database, str):
                raise TypeError
            else:
                results = "from {}.{}".format(database, table)
        elif schema:
            if not isinstance(schema, str):
                raise TypeError
            else:
                results = "from {}.{}".format(schema, table)
        return results

    @staticmethod
    def filter_join(
        filter_name: str,
        field_name: str,
        field_value: Union[int, str, tuple[str, int, float]],
        field_operation: str,
    ) -> str:
        if not isinstance(field_name, str):
            raise TypeError
        if isinstance(field_value, str):
            if field_operation in ("like", "ilike"):
                results = "{} {} {} '%{}%'".format(filter_name, field_name, field_operation, field_value)
            else:
                results = "{} {} {} '{}'".format(filter_name, field_name, field_operation, field_value)
        else:
            if field_operation in ("like", "ilike"):
                raise SyntaxError
            else:
                results = "{} {} {} {}".format(filter_name, field_name, field_operation, field_value)
        return results

    @staticmethod
    def where_clause(filter_iterable: Union[list[str], tuple[str], set[str], None] = None) -> str:
        if not filter_iterable:
            return str()
        if not isinstance(filter_iterable, (list, tuple, set)):
            raise TypeError
        else:
            split_list = " ".join(filter_iterable).split()
            if split_list[0] in ("not", "and", "or"):
                filter_str = " ".join(split_list[1:])
                results = " ".join(("where", filter_str))
            else:
                raise ValueError
        return results

    @staticmethod
    def group_by_clause(field: Union[str, list[str], tuple[str], set[str], None] = None) -> str:
        if not field:
            return str()
        if not isinstance(field, (list, tuple, set)):
            if not isinstance(field, str):
                raise TypeError
            else:
                results = "group by {}".format(field)
        else:
            field_str = ", ".join(field)
            results = " ".join(("group by", field_str))
        return results

    @staticmethod
    def having_clause(field: Union[str, list[str], tuple[str], set[str], None] = None) -> str:
        if not field:
            return str()
        if not isinstance(field, (list, tuple, set)):
            if not isinstance(field, str):
                raise TypeError
            else:
                results = "having {}".format(field)
        else:
            field_str = ", ".join(field)
            results = " ".join(("having", field_str))
        return results
