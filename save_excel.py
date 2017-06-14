#!/usr/bin/python
# -*- coding: utf-8 -*-


import open_excel
from openpyxl import Workbook


def save(num):
    open_excel.G_saved_numbers.append(num)


def save_to_excel():
    wb = Workbook()

    ws = wb.active

    for num in open_excel.G_saved_numbers:
        ws.cell(row=(open_excel.G_saved_numbers.index(num)+1), column=1, value=num)

    wb.save("recipe.xlsx")
