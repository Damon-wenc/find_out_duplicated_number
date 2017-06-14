#!/usr/bin/python
# -*- coding: utf-8 -*-


import check_duplication
import save_excel
import open_excel


def main():
    print '''
    女王大人，简易操作指南如下：
    1. 输入发票序号，enter结束
    2. 如有重复会提示并退出程序
    3. 所有已输入的数据会保存在'recipe.xlsx'里，请取用
    4. 当前简易版本，日后升级
    跪安了
    
    '''

    print "达康：请开始你的输入："
    # 1. load已添加Excel表格
    open_excel.load()

    # 2. 输入字符串 && 检查是否重复
    while True:
        message = raw_input()
        if message == "stop":
            break

        try:
            serial_num = int(message)
        except:
            print "输入非数字！请重新输入："
            continue

        if check_duplication.check(serial_num):
            print "发票序号重复输入！序号在第%d次前已输入" \
                  % (len(open_excel.G_saved_numbers)-open_excel.G_saved_numbers.index(serial_num)-1)
            break

        save_excel.save(serial_num)

    # 3. 保存到Excel表格
    save_excel.save_to_excel()

    return 0

if __name__ == "__main__":
    main()
