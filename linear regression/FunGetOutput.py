# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 02:52:32 2017

@author: Yu
"""

from numpy import *
import numpy as np
from FunNeuronNLFun import NeuronNLFun

# all inputs are list type variable
def GetOutput(weight,inputData):
    neuronValue=[]
    
    inputData = mat(inputData)
    neuronValue.append(inputData)
    for i in range(0,len(weight)):
        # retrive the last vector in the neuronValue list to generate next layer's value
        neuronValue.append(NeuronNLFun(mat(neuronValue[-1]) * weight[i]))
    return neuronValue

"""
from FunInit import Init
layerNum=[12,5,4]
inputData=[1,2,3,4,5,6,7,8,9,10,11,12]
weight=Init(layerNum)
O=GetOutput(weight,inputData)
"""