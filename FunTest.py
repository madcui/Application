# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 02:00:02 2017

@author: Yu
"""
from FunGetOutput import GetOutput
import numpy as np
from numpy import *
def Test(weightTrain,testMIn,testMOut):
    dist=[]
    M=[]
    for i in range(testMIn.shape[0]):
        neuronvaule=GetOutput(weightTrain,testMIn[i,:])
        discrepancies=neuronvaule[-1]-testMOut[i,:]
        dist.append(np.linalg.norm(discrepancies))
        M.append(np.linalg.norm(neuronvaule[-1]))
    D=np.mean(dist)/np.mean(M)
    return D
    
