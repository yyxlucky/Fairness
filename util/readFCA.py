#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : readFCA.py
import util.vo as vo

def readFCA():


    filename = input("请输入conceptLattice文件名：")
    # filename = '/Users/yxyang/Desktop/t7.txt'

    bpCliques = []

    with open(filename, "r") as f:
        words = f.readline()
        while(words):
            word = words.split("#")
            extent = word[0].strip("(")
            extent = extent.strip(")")
            extent = extent.split(",")
            extent  = [int(x) for x in extent if x != '']
            extent = tuple(extent)

            intent = word[1].strip("(")
            intent = intent.strip(")\n")
            intent = intent.split(",")
            intent = [int(x) for x in intent if x != '']
            intent = tuple(intent)

            temp = vo.Pair(extent, intent)

            bpCliques.append(temp)

            words = f.readline()

    # for i in bpCliques:
    #     print(i.getL(), i.getR())
    return bpCliques



# readFCA()