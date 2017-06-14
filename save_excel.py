#!/usr/bin/python
# -*- coding: utf-8 -*-


import open_excel


def save(num):
    print "before", open_excel.G_saved_numbers
    open_excel.G_saved_numbers.append(num)
    print "after", open_excel.G_saved_numbers