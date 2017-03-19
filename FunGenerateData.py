#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:03:28 2017

@author: guangwei
"""
import numpy as np
from numpy import *
from FunNeuronNLFun import NeuronNLFun 

def GenerateData(nTrain, nTest, nIn, nOut):
    # Generate a nIn-by-nOut matrix, 
    # the value follow random uniform distribution between [-1 1]
    weightTarget = []
    weightTarget.append(mat(np.random.uniform(-1 ,1, (nIn ,nOut))))
    
    # Generate random inputs for train and test
    trainMIn  = mat(np.random.rand(nTrain, nIn))
    testMIn = mat(np.random.rand(nTest, nIn))
    
    # Calculate the outputs using input by the weight Matrix
    trainMOut = np.dot(trainMIn,  weightTarget)
    testMOut = np.dot(testMIn,  weightTarget)
    
    trainMOut = mat(NeuronNLFun(trainMOut))
    testMOut  = mat(NeuronNLFun(testMOut))
    
    return weightTarget, trainMIn, trainMOut, testMIn, testMOut

"""
# test:
nTrain = 12
nTest= 8
nIn = 10
nOut = 4

(weightTarget,trainMIn,trainMOut,testMIn,testMOut)= GenerateData(nTrain, nTest, nIn, nOut)
print(weightTarget)
"""