# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 00:29:06 2017

@author: Yu
"""
from numpy import *
import numpy as np

def Init(layer_num):
    for i in range(0,len(layer_num)-1):
        weight[i]=mat(random.rand(layer_num[i],layer_num[i]))
    return weight