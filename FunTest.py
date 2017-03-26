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
    neuronvaule=GetOutput(weightTrain,testMIn)
    discrepancies=neuronvaule[-1]-testMOut
    for i in range(discrepancies.shape[0]):
        dist.append(np.linalg.norm(discrepancies[i,:]))
        M.append(np.linalg.norm(neuronvaule[-1][i,:]))
    D=np.mean(dist)-np.mean(M)
    return D
    
