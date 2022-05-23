#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : formatCV.py

import numpy as np
def format():
    #读入形式背景
        filename = input("请输入文件名：")
        # filename = '/Users/yxyang/Desktop/Intra-organisational networks.txt'

        with open(filename, "r") as f:
            numObj = int(f.readline())#获取对象数量
            numAttr = numObj
            adjMat = np.zeros(shape=(numObj, numAttr), dtype=int)#存储形式背景矩阵
            adjMatC = np.zeros(shape=(numObj, numAttr), dtype=int)  # 存储补形式背景矩阵
            weight = np.zeros(shape=(numObj, numAttr), dtype=int)  # 存储权重
            obj = []
            attr = []

            #将形式背景存储到矩阵内
            lines = f.readlines()  # 读取全部内容

            for i in range(0, lines.__len__(), 1):  # (开始/左边界, 结束/右边界, 步长)

                list = []  ## 空列表, 将第i行数据存入list中
                for word in lines[i].split():
                    word = word.split(" ")
                    list.append(word);
                # print(list)
                n1 = int(list[0][0])
                n2 = int(list[1][0])
                rship = int(list[2][0])
                if rship == -1:
                    adjMatC[n1-1][n2-1] = 1
                else:
                    adjMat[n1-1][n2-1] = 1
                    weight[n1-1][n2-1] = rship

            numObj = 46
            numAttr = 46

            a1 = adjMat[0:numObj+1, 0:numAttr+1]
            a2 = adjMatC[0:numObj+1, 0:numAttr+1]
            a3 = weight[0:numObj + 1, 0:numAttr + 1]



            for i in range(numObj):
                for j in range(numAttr):
                    if a1[i][j] == 1 and a1[j][i] == 1:
                        pass
                    else:
                        a1[i][j] = 0
                        a1[j][i] = 0

            for i in range(numObj):
                for j in range(numAttr):
                    if a2[i][j] == 1 or a2[j][i] == 1:
                        a2[i][j] = 1
                        a2[j][i] = 1



            outFile = input("请输入写出adjMat结果的文件路径：")
            # outFile = '/Users/yxyang/Desktop/rs.txt'
            with open(outFile, 'w') as fi:


                fi.write(str(numObj)+"\n")
                fi.write(str(numAttr)+'\n')

                for i in range(numObj):
                    for j in range(numAttr):
                        if i == j:
                            # adjMat[i][j] = 1
                            a1[i][j] = 1
                        # fi.write(str(adjMat[i][j]))
                        fi.write(str(a1[i][j]))
                    fi.write('\n')

            outFile = input("请输入写出weight结果的文件路径：")
            # outFile = '/Users/yxyang/Desktop/rs.txt'
            with open(outFile, 'w') as fi:

                fi.write(str(numObj) + "\n")
                fi.write(str(numAttr) + '\n')

                for i in range(numObj):
                    for j in range(numAttr):
                        if i == j:
                            # adjMat[i][j] = 1
                            a3[i][j] = 1
                        # fi.write(str(adjMat[i][j]))
                        fi.write(str(a3[i][j]))
                    fi.write('\n')

            outFile = input("请输入写出adjMatC结果的文件路径：")
            # outFile = '/Users/yxyang/Desktop/rs.txt'
            with open(outFile, 'w') as fi:

                fi.write(str(numObj) + "\n")
                fi.write(str(numAttr) + '\n')

                for i in range(numObj):
                    for j in range(numAttr):
                        if i == j:
                            # adjMatC[i][j] = 1
                            a2[i][j] = 1
                        # fi.write(str(adjMatC[i][j]))
                        fi.write(str(a2[i][j]))
                    fi.write('\n')

format()