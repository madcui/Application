#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:31:55 2017

@author: guangwei
"""

from numpy import *
import numpy as np

def UpdateWeight (weightOld, neuronValue, error, weightNew=[]):
    for i in range(0,len(neuronValue)-1):
        oPre = mat(neuronValue[i])
        ePost = mat(error[i+1])
        dW = oPre.transpose() * ePost
        weightNew.append(mat(weightOld[i]) + dW)
    return weightNew, dW, oPre, ePost

"""
#test
weightOld = np.matrix([[1, 2], [3, 4], [5, 6]])

neuronValue = [];
neuronValue.append([0.3, 0.4, 0.5])
neuronValue.append([0.7, 0.3])

error = [];
error.append([0.1, -0.15, 0.05])
error.append([-0.075, 0.125])

(weightNew, dW, oPre, ePost) = UpdateWeight (weightOld, neuronValue, error)

print(weightOld)
print(weightNew)
print(dW)
print(oPre)
print(ePost)
""