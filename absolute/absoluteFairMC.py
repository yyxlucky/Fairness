#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : Absolute Fair Concept.py

import util.CL as CL
import util.IO as IO
import itertools as itertools
from allpairspy import AllPairs as ap
import util.readFCA as readFCA
import datetime as dt

def Fairness(allCliques, nodeAttrDic, nodeAttrDicTemp):
    pseFarinessCliques = []
    # nodeAttr = []




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

def Fair():
    '''
    io = IO.io()
    # C:\yyx\SCH\fourthSeme\worldIT2022\data\1.txt
    # /Users/yxyang/Desktop/absoluteFairData/1.txt
    # cur1 = dt.datetime.now()
    adjMat = io.__getitem__(0)
    obj = io.__getitem__(2)
    attr = io.__getitem__(3)

    # 计算原形式背景和补形式背景下的概念格cl,clC
    cl = CL.cl(adjMat, obj, attr)
    extent = cl.__getitem__(0)
    bp = cl.__getitem__(2)
    bpo = cl.__getitem__(3)
    ec = set() #ec is equiConcept
    '''


    '''
    conceptLattice = fca.fca()
    adjMat = conceptLattice.__getitem__(0)
    obj = conceptLattice.__getitem__(1)
    attr = conceptLattice.__getitem__(2)
    cl = conceptLattice.__getitem__(3)
    bp = conceptLattice.__getitem__(4)
    ec = set() #ec is the set of equiConcept
    
    '''

    bp = readFCA.readFCA()
    ec = set() # ec is the set of equiconcept




    nodeAttr = []

    filenameA = input("请输入属性文件：")

    with open(filenameA, "r") as f:
        word = f.readline()
        while(word):
            # print(word)
            word = word.replace("\n", "")
            nodeAttr.append(word)
            word = f.readline()

    print(nodeAttr)
    attrNum = set(nodeAttr)
    print("共有", len(attrNum), "种属性:", attrNum)

    # 获取等式概念，即Maximal Cliques
    for e in bp:
        # print(e)
        if e.getL() == e.getR():
            ec.add(e)
    print("-------等式概念有--------")
    for i in ec:
        print(i.getL(), i.getR())
    print("等式概念个数为:", len(ec))
    print("------------------------")


    pseudoEC = [] #衍生的绝对公平等式概念
    pseudoECcandidate = []
    nodeAttrDic = {}
    nodeAttrDicTemp = {}

    for key in attrNum:
        nodeKey = []
        for keyT in nodeAttr:
            if keyT == key:
                iT = nodeAttr.index(keyT)
                nodeKey.append(iT+1)
                nodeAttr[iT] = 0
        nodeAttrDic[key] = nodeKey
        nodeAttrDicTemp[key] = 0
    print("属性字典为", nodeAttrDic)

    time1 = dt.datetime.now()

    #
    # for i in ec:
    #     print("---------ec:", i.getL(), i.getR())
    #     nodes = list(i.getL())
    #     if len(nodes) < len(attrNum):
    #         print("pass")
    #         pass

    MCS = set()
    for i in ec:
        MCS.add(i.getL())
    allCliques = []
    for i in MCS:
        result = [[]]
        for x in i:
            result.extend([subset + [x] for subset in result])
        # print(result)
        for j in result:
            if j != []:
                allCliques.append(j)
    print(allCliques)
    '''
    for i in ec:
        # print("---ec:", i.getL(), i.getR())
        nodeAttrDicCopy = nodeAttrDic.copy()
        # print("dicCopy:",nodeAttrDicCopy)
        # print("dic:", nodeAttrDic)
        nodes = list(i.getL())
        # print("----nodes---:", nodes)
        if len(nodes) < len(attrNum):
            # print("跳过")
            continue
        else:
            for key, value in nodeAttrDicCopy.items():
                # print(type(value))
                value = list(set(value).intersection(set(nodes)))
                if value is not None:
                    nodeAttrDicCopy[key] = value
                    # print("k-v:", key, value)
                else:
                    continue
            # print(nodes)
            # print(nodeAttrDicCopy)

            valuesDic = nodeAttrDicCopy.values()
            minL = len(nodeAttrDicCopy.get(next(iter(nodeAttrDicCopy))))
            for v in valuesDic:
                if minL > v.__len__():
                    minL = v.__len__()
            # print(minL)

            if minL == 0:
                continue
            else:
                pseudoTemp = []
                for v in valuesDic:
                    # print("v:", v)
                    if len(v) > minL:
                        newNode = list(itertools.combinations(v, minL))
                    else:
                        newNode = v

                    pseudoTemp.append(newNode)
                    # print("newNode:", newNode)
        pseudoECcandidate.append(pseudoTemp)
    print("candidate:", pseudoECcandidate)

    # print("\n----可以衍生的概念有(候选集)--------")

    for i in pseudoECcandidate:
        # print(i)
        psNew = []
        for j in i:
            list_new = [str(x) if type(x)== int else str(x[0]) for x in j]
            # print(list_new)
            psNew.append(list_new)

        # print("psNew:", psNew)
        for pairs in ap(psNew[:len(attrNum)]):
            pseudoEC.append(','.join(pairs))

    # print("-------------------------\n")
    '''

        #
        # for k in range(2, len(psNew)):
        #     new_psEC = []
        #     for pairs in ap(pseudoEC, psNew[k]):
        #         new_psEC.append(''.join(pairs))
        #         print("newpsEC:", new_psEC)
        #         pseudoEC = new_psEC




    # print("pseudoCandidate:", pseudoECcandidate)
    # psCandidateNum = len(pseudoECcandidate)
    #
    # for i in pseudoECcandidate:
    #     for pairs in ap(i[:2]):
    #         pseudoEC.append(''.join(pairs))
    #
    #     for j in range(2, len(i)):
    #         new_psEC = []
    #         for pairs in ap([pseudoEC, i[j]]):
    #             new_psEC.append(''.join(pairs))
    #             pseudoEC = new_psEC

    '''
    print("存在的absoluteFair有：", pseudoEC)
    print("共有", len(pseudoEC), "个")
    '''

    result = Fairness(allCliques, nodeAttrDic, nodeAttrDicTemp)
    print("存在的absoluteFair有：", result)
    print(len(result), "个")

    time2 = dt.datetime.now()
    timeTotal = time2 - time1
    print("time:", timeTotal)



Fair()

