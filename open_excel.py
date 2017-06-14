#!/usr/bin/python
# -*- coding: utf-8 -*-


from openpyxl import load_workbook


G_saved_numbers = []


def load():
    wb = load_workbook('recipe.xlsx', read_only=True)
    ws = wb["Sheet"]
    for row in ws.rows:
        for cell in row:
            G_saved_numbers.append(cell.value)

    wb.close()
