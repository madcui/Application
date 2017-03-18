# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 00:29:06 2017

@author: Yu
"""
from numpy import *
import numpy as np

def Init(layerNum,weight=[]):
    
    # range count from 0 to len(layerNum)-1-1
    for i in range(0,len(layerNum)-1):
        # append is a function to generate list
        # mat is to make a matrix
        weight.append(mat(random.rand(layerNum[i],layerNum[i+1])))
    return weight

layerNum=[3,4,5]
weight=Init(layerNum)
print(weight)