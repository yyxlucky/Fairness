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

    # for i in ot:
    #     print(str(i))

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

    tra = input("请输入目标用户节点：")
    tragetID = int(tra)
    traget = []
    for i in ot:
        if tragetID in i.getL():
            traget.append(i.getL())

    for i in traget:
        print(str(i))

    filename = '/Users/yxyang/Desktop/worldit/weight.txt'
    # filename = '/Users/yxyang/Desktop/t7.txt'

    with open(filename, "r") as f:
        numObj = int(f.readline())  # 获取对象数量
        numAttr = int(f.readline())  # 获取属性数量
        weight = np.zeros(shape=(numObj, numAttr), dtype=int)  # 存储形式背景矩阵
        # 将形式背景存储到矩阵内
        for i in range(numObj):
            for j in range(numAttr):
                t = int(f.read(1))
                weight[i][j] = t
            f.read(1)


        trust = []
        trs = {}
        for i in traget:
            sum = 0
            for j in i:
                if i is not j:
                    sum = sum + weight[tragetID-1][j-1]
            trust.append(sum/(len(i)-1))
            temp = {i: sum/(len(i) - 1)}
            trs.update(temp)

        print(trust)
        # sorted(zip(trs.values(), trs.keys()))
        # print(sorted(trs.items(), reverse=False))
        max(trs.values())

        for key, value in trs.items():
            if(value == max(trs.values())):
                print(key,value)

        print(trs)









findMaximal()