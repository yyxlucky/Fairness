#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : baseLineAF2.py

from collections import OrderedDict
import util.IO as IO
import datetime as dt

class Stack(object):
    def __init__(self):
        self.items = list()

    # 入栈
    def push(self, item):
        self.items.append(item)

    # 出栈
    def pop(self):
        return self.items.pop()

    # 清空栈
    def clear(self):
        del self.items[:]

    # 判断栈是否为空
    def empty(self):
        return self.size() == 0

    # 获取栈的大小
    def size(self):
        return len(self.items)

    # 获取栈顶的节点
    def top(self):
        return self.items[self.size() - 1]

# tarjan算法求连通图
def tarjan(u):
    global s, n, count, flag, stack, pre, low, matrix
    count = count + 1
    pre[u] = low[u] = count
    s.push(u)
    flag[u] =  True
    for i in range(n):
        if matrix[u][i] == 0:
            continue
        if flag.get(i, False) is True:
            if(pre[i] < low[u]):
                low[u] = pre[i]
        else:
            tarjan(i)
            low[u] = min(low[u], low[i])

    if(pre[u]== low[u] and s.empty() is False):
        mc = list()
        m = s.pop()
        flag[m] = False
        mc.append(m+1)

        while m!=u and s.empty() is False:
            m = s.pop()
            flag[m] =  False
            mc.append(m+1)
        mc.sort()
        mc = tuple(mc)
        MCS.add(mc)


def Fairness(allCliques, nodeAttr, attrNum):
    pseFarinessCliques = []
    # nodeAttr = []

    nodeAttrDic = {}
    nodeAttrDicTemp = {}

    for key in attrNum:
        nodeKey = []
        for keyT in nodeAttr:
            if keyT == key:
                iT = nodeAttr.index(keyT)
                nodeKey.append(iT + 1)
                nodeAttr[iT] = 0
        nodeAttrDic[key] = nodeKey
        nodeAttrDicTemp[key] = 0
    print("属性字典为", nodeAttrDic)

    for i in allCliques:
        NumberofAttribute = nodeAttrDicTemp.copy()
        # print(NumberofAttribute)
        for j in i:
            # print(j)
            key = get_key(nodeAttrDic, j)
            # print(str(key[0]))
            key = str(key[0])
            NumberofAttribute[key] = NumberofAttribute[key] + 1
            # print(NumberofAttribute[key])
        # print(NumberofAttribute)

        num = set()
        for key, value in NumberofAttribute.items():
            num.add(value)
            # print(value)
        # print(num)
        if len(num) == 1:
            pseFarinessCliques.append(i)
    return pseFarinessCliques



def get_key (dict, value):
    return [k for k, v in dict.items() if value in v]

if __name__ == "__main__":
    io = IO.io()
    # /Users/yxyang/Desktop/absoluteFairData/1.txt
    time1 = dt.datetime.now()
    matrix = io.__getitem__(0)
    matrix = matrix.tolist()
    MCS = set()
    pre = OrderedDict()
    low = OrderedDict()
    flag = dict()
    count = 0
    n = len(matrix)
    s = Stack()
    for i in range(len(matrix[0])):
        tarjan(i)


    print("极大连通子图的数量为：",len(MCS))
    print("连通子图有：",MCS)

    allCliques = []
    for i in MCS:
        result = [[]]
        for x in i:
            result.extend([subset + [x] for subset in result])
        # print(result)
        for j in result:
            if j != []:
                allCliques.append(j)
        # allCliques.append(result)

    print("衍生的连通子图有:",allCliques)

    time2 = dt.datetime.now()

    filenameA = input("请输入属性文件：")

    nodeAttr = []
    with open(filenameA, "r") as f:
        word = f.readline()
        while (word):
            # print(word)
            word = word.replace("\n", "")
            nodeAttr.append(word)
            word = f.readline()

    print(nodeAttr)
    attrNum = set(nodeAttr)
    print("共有", len(attrNum), "种属性:", attrNum)

    time3= dt.datetime.now()

    result = Fairness(allCliques, nodeAttr, attrNum)
    print("存在的absoluteFair有：",result)
    print(len(result), "个")

    time4 = dt.datetime.now()

    timeTotal = time4-time3 + time2-time1
    print("time:", timeTotal)












