# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 00:29:06 2017

@author: Yu
"""
from numpy import *
import numpy as np

def Init(layerNum):
    for i in range(0,len(layerNum)):
        weight.append=mat(random.rand(layerNum[i],layerNum[i]))
    return weight