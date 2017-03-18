#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:03:28 2017

@author: guangwei
"""
import numpy as np

def GenerateData(nTrain, nTest, nIn, nOut):
    # Generate a nIn-by-nOut matrix, 
    # the value follow random uniform distribution between [-1 1]
    wTarget = np.random.uniform(-1 ,1, (nIn ,nOut))
    
    # Generate random inputs for train and test
    trainMIn  = np.random.rand(nTrain, nIn)
    testMIn = np.random.rand(nTest, nIn)
    
    # Calculate the outputs using input by the weight Matrix
    trainMOut = np.dot(trainMIn,  wTarget)
    testMOut = np.dot(testMIn,  wTarget)
    
    return wTarget, trainMIn, trainMOut, testMIn, testMOut

GenerateData(12, 8, 10, 4)