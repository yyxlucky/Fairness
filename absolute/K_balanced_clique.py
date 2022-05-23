#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : fca.py
import util.CL as CL
import util.IO as IO
import util.vo as vo
import numpy as np
import datetime as dt
import itertools as itertools


def k_balance():
    # 读入形式背景
    filename = input("请输入文件名：")
    # filename = '/Users/yxyang/Desktop/t7.txt'
    # C:\yyx\SCH\ThirdSeme\jips\sla.txt
    # C:\yyx\SCH\ThirdSeme\jips\experiment\data
    cur1 = dt.datetime.now()

    with open(filename, "r") as f:
        numObj = int(f.readline())  # 获取对象数量
        numAttr = int(f.readline())  # 获取属性数量
        adjMat = np.zeros(shape=(numObj, numAttr), dtype=int)  # 存储形式背景矩阵
        adjMatOrignal = np.zeros(shape=(numObj, numAttr), dtype=int)  # 存储补形式背景矩阵
        obj = []
        attr = []


        # 将形式背景存储到矩阵内
        for i in range(numObj):
            obj.append(i + 1)
            attr.append(i + 1)

        for i in range(numObj):
            for j in range(numAttr):
                t = int(f.read(1))
                if t == 1:
                    adjMat[i][j] = 1
                    adjMatOrignal[i][j] = 1
                elif t == 2:
                    adjMat[i][j] = 1
                    adjMatOrignal[i][j] = -1
            f.read(1)


    # 计算原形式背景和补形式背景下的概念格cl,clC
    cl = CL.cl(adjMat, obj, attr)
    bp = cl.__getitem__(2)


    #查找所有的等式概念
    ec = []
    ecL = []
    k_balance_clique = []
    for i in bp:

        if i.getL().__eq__(i.getR()) and len(i.getL()) == 2:
            ec.append(i)
            ecL.append(i.getL())

        elif i.getL().__eq__(i.getR()) and len(i.getL()) > 2:
            bb = list(i.getL())
            # print("bb:", bb)
            for j in range(3, len(i.getL())+1, 1):
                cc = list(itertools.combinations(bb, j))
                # print("cc:",cc)
                for m in cc:
                    vt = vo.Pair(tuple(m), tuple(m))
                    ec.append(vt)
                    ecL.append(tuple(m))




    #计算每个等式概念的权重之和，并与C（2，k）进行比较，符合条件的就是平衡的
    for i in ec:
        k = len(i.getL())
        Ck2 = k * (k-1) / 2
        weight = 0
        for j in i.getL():
            # print("j:", j)
            for m in i.getL():
                # print("m:", m)
                if j != m:
                    weight = weight + adjMat[j-1][m-1]
        # print(weight)


        if weight/2 == Ck2:
            k_balance_clique.append(i.getL())
            # print(weight, Ck2)
            # print(i.getL(), i.getR())

    set(k_balance_clique)
    print("k_balance_clique:", len(k_balance_clique))


    adjMatM1 = adjMatOrignal.copy()
    adjMatM1[adjMatM1==-1] = 0

    adjMatM2 = adjMatOrignal.copy()
    adjMatM2[adjMatM2==1] = 0
    adjMatM2[adjMatM2==-1] = 1

    cl2 = CL.cl(adjMatM1, obj, attr)
    bp2 = cl2.__getitem__(2)
    cl3 = CL.cl(adjMatM2, obj, attr)
    bp3 = cl3.__getitem__(3)

    # 查找positive的等式概念
    ec2 = []
    ecL2 = []
    for i in bp2:
        if i.getL().__eq__(i.getR()):
            ec2.append(i)
            ecL2.append(set(i.getL()))
            ecL2.append(set(i.getL()))
            # print(i.getL(), i.getR())


    # 查找negative的等式概念
    ec3 = []
    for i in bp3:
        if i.getL().__eq__(i.getR()):
            ec3.append(i)

    resultEC = set()
    finalRS = []
    # 判断他们是否是一个整体等式概念

    left = tuple()
    right = tuple()

    '''

    for i in k_balance_clique:
        # print("i:", i)
        for j in ec2:
            # print("j:", j.getL())
            for m in ec2:
                # print("m:", m.getL())
                if j.getL() in i and m.getL() in i:
                    left = j.getL()
                    right = m.getL()
                    v = left + right
                    print("left:" + str(left) + ", right:" + str(right))
                    v = tuple(sorted(v))
                    if v in resultEC:
                        pass
                    else:
                        resultEC.add(v)
                        tt = vo.Pair(left, right)
                        finalRS.append(tt)
    '''






    for i in ec2:
        for j in ec2:
            if type(i.getL()) is int:
                if type(j.getL()) is int:
                    num0 = i.getL()
                    num0 = [num0]
                    num0 = tuple(num0)
                    num = j.getL()
                    num = [num]
                    num = tuple(num)
                    ecc = num0 + num
                    left = num0
                    right = num
                else:
                    num = i.getL()
                    num = [num]
                    num = tuple(num)
                    ecc = num + j.getL()
                    left = num
                    right = j.getL()
            else:
                if type(j.getL()) is int:
                    num = j.getL()
                    num = [num]
                    num = tuple(num)
                    ecc = i.getL() + num
                    left = i.getL()
                    right = num
                else:
                    ecc = i.getL() + j.getL()
                    left = i.getL()
                    right = j.getL()


            ecc = sorted(set(ecc))
            ecc = tuple(ecc)
            if ecc in k_balance_clique:

                v = left + right
                # print("left:" + str(left) + ", right:" +str(right))
                v = tuple(sorted(set(v)))
                if len(v) <= 2:
                    pass
                else:

                    if v in resultEC:
                        pass
                    else:
                        resultEC.add(v)
                        tt = vo.Pair(left, right)
                        finalRS.append(tt)
    FT = finalRS.copy()

    for i in resultEC:
        for j in resultEC:
            set_c = set(i).intersection(set(j))
            set_c = set(sorted(set_c))
            # print(set_c)
            if set_c in ecL2 and len(set_c) != 0:
                # print("aaa")
                vt = vo.Pair(j, tuple(set_c))
                FT.append(vt)



    for i in FT:
        if i.getL().__eq__(i.getR()):
            pass
        else:
            print(i.getL(),i.getR())




    cur2 = dt.datetime.now()

    time = cur2 - cur1

    print("time is:", time)




    outFile = input("请输入写出结果的文件路径：")
    # outFile = '/Users/yxyang/Desktop/rs.txt'
    with open(outFile, 'w') as fi:
        fi.write(str(time) + "\n")
        fi.write("finalRS:" + str(len(finalRS)) + "\n")
        for i in finalRS:
            # print(i.getL(), i.getR())
            #fi.write(str(i.getR()) + "#" + str(i.getL()) + "\n")
            fi.write(str(i.getL()) + str(i.getR()) + "\n")
        fi.write("balanced-cliques:" + str(len(resultEC)) + "\n")
        for i in resultEC:
            fi.write(str(i) + "\n")


k_balance()