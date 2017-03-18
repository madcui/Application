# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 02:52:32 2017

@author: Yu
"""

from numpy import *
import numpy as np

def GetOutput(weight,inputData,neuronValue=[]):
    inputData=mat(inputData)
    neuronValue.append(inputData)
    for i in range(0,len(weight)):
        neuronValue.append(mat(neuronValue[-1])*weight[i])
    return neuronValue

"""test
from FunInit import Init
layerNum=[2,3,4]
inputData=[1,2]
weight=Init(layerNum)
O=GetOutput(weight,inputData)
"""