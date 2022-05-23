#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : MoMopreprocess.py

import pandas as pd

def preprocess():
    path_file = "/Users/yxyang/Desktop/absoluteFairData/data/data20190223/friend_large2.csv"
    df = pd.read_csv(path_file)
    df.drop(labels = 'Time', axis = 1, columns=2)
    print(df.head(5))





preprocess()