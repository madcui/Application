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
    samplenorm=[]
    nodeDiscrepancies=0
    for i in range(testMIn.shape[0]):
        neuronvaule=GetOutput(weightTrain,testMIn[i,:])
        discrepancies=neuronvaule[-1]-testMOut[i,:]
        nodeDiscrepancies=discrepancies+nodeDiscrepancies
        dist.append(np.linalg.norm(discrepancies))
        samplenorm.append(np.linalg.norm(neuronvaule[-1]))
    totalDicrepancies=np.mean(mat(dist)/mat(samplenorm))
    nodeDiscrepancies=nodeDiscrepancies/testMIn.shape[0]
        
    return totalDicrepancies,nodeDiscrepancies
    
