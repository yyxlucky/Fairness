#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : findBMC.py
import util.IO as IO
import util.CL as CL

def findBMC():
    io = IO.io()
    adjMat = io.__getitem__(0)
    obj = io.__getitem__(2)
    attr = io.__getitem__(3)

    # 计算原形式背景下的概念格cl,clC
    cl = CL.cl(adjMat, obj, attr)
    bp = cl.__getitem__(2)
    os = cl.__getitem__(0)

    io2 = IO.io()
    adjMat2 = io2.__getitem__(0)
    obj2 = io2.__getitem__(2)
    attr2 = io2.__getitem__(3)

    cl2 = CL.cl(adjMat2, obj2, attr2)
    bp2 = cl2.__getitem__(2)
    os2 = cl2.__getitem__(0)

    ot = []
    for i in os:
        for j in os2:
            if i.__eq__(j) and len(i) is not 1:
                ot.append(i)

    for i in ot:
        print(str(i))

findBMC()