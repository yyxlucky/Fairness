#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : findMaximalClique.py
import util.IO as IO
import util.CL as CL
import numpy as np

def findMaximal():
    io = IO.io()
    adjMat = io.__getitem__(0)
    obj = io.__getitem__(2)
    attr = io.__getitem__(3)

    # 计算原形式背景下的概念格cl,clC
    cl = CL.cl(adjMat, obj, attr)
    bp = cl.__getitem__(2)

    ot = []
    for i in bp:
        if i.getL().__eq__(i.getR()):
            ot.append(i)

    for i in ot:
        print(i.getL(), i.getR())

    '''
    outFile = input("请输入写出结果的文件路径：")
    # outFile = '/Users/yxyang/Desktop/rs.txt'
    with open(outFile, 'w') as fi:


        fi.write("MC:\n")

        mset = set()
        mbc = []

        for i in ot:
            # print(i.getL(), i.getR())
            fi.write(str(i.getR()) + "#" + str(i.getL()) + "\n")

        fi.write("len(MC):" + str(len(ot)))
    '''








findMaximal()