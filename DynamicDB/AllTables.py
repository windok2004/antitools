#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/10
from TabaleSchema import sys_tab


def GetAllTables(schema=None):
    tables = dict()
    for row in sys_tab(sys_tab.COLUMNS.TABLE_SCHEMA == schema).select():
        if tables.get(row.TABLE_NAME):
            tables.get(row.TABLE_NAME).append(
                (row.COLUMN_NAME, row.DATA_TYPE, row.IS_NULLABLE))
        else:
            tables[row.TABLE_NAME] = []
            tables.get(row.TABLE_NAME).append(
                (row.COLUMN_NAME, row.DATA_TYPE, row.IS_NULLABLE))
    return tables


if __name__ == '__main__':
    print GetAllTables(schema="lms_test")
