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
    nodeDiscrepancies=[]
    for i in range(testMIn.shape[0]):
        neuronvaule=GetOutput(weightTrain,testMIn[i,:])
        discrepancies=neuronvaule[-1]-testMOut[i,:]
        nodeDiscrepancies.append(discrepancies)
        dist.append(np.linalg.norm(discrepancies))
        M.append(np.linalg.norm(neuronvaule[-1]))
    totalDicrepancies=np.mean(mat(dist)/mat(M))
        
    return totalDicrepancies,nodeDiscrepancies
    
