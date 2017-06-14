#!/usr/bin/python
# -*- coding: utf-8 -*-


import check_duplication
import save_excel
import open_excel


def main():
    # 1. load已添加Excel表格

    # 2. 输入字符串 && 检查是否重复
    while True:
        message = raw_input()
        if message == "stop":
            break

        if check_duplication.check(message):
            print "发票序号重复输入！序号在第%d次前已输入" \
                  % (len(open_excel.G_saved_numbers)-open_excel.G_saved_numbers.index(message)-1)
            return -1

        save_excel.save(message)

    # 3. 保存到Excel表格

    return 0

if __name__ == "__main__":
    main()
