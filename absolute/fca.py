#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : fca.py
import util.CL as CL
import util.IO as IO


def fca():
    io = IO.io()
    # cur1 = dt.datetime.now()
    adjMat = io.__getitem__(0)
    adjMatC = io.__getitem__(1)
    obj = io.__getitem__(2)
    attr = io.__getitem__(3)

    # 计算原形式背景和补形式背景下的概念格cl,clC
    cl = CL.cl(adjMat, obj, attr)
    bp = cl.__getitem__(2)

    outFile = input("请输入写出结果的文件路径：")
    # outFile = '/Users/yxyang/Desktop/rs.txt'
    with open(outFile, 'w') as fi:
        for i in bp:
            # print(i.getL(), i.getR())
            fi.write(str(i.getR()) + "#" + str(i.getL()) + "\n")

    return adjMat,obj,attr,cl,bp


fca()