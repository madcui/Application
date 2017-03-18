# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 00:29:06 2017

@author: Yu
"""
from numpy import *
import numpy as np

def Init(layerNum):
    weight=[]
    for i in range(0,len(layerNum)-1):
        weight.append(mat(random.rand(layerNum[i],layerNum[i+1])))
    return weight

"""test
layerNum=[3,4,5]
weight=Init(layerNum)
print(weight)
"""