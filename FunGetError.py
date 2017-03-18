# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 04:11:50 2017

@author: Yu
"""
from numpy import *
import numpy as np

def GetError(weight,target,outputValue):
    errorPart1=[]
    errorPart2=[]
    error=[]
    #output layer error
    outError=mat(target)-mat(outputValue[-1])
    errorPart1.append(outError)
    #error back transmit
    for i in range(len(weight)-1,-1,-1):
        errorPart1.insert(0,errorPart1[0]*weight[i].T)
    #error part related with the current neuron vaule
    for i in range(0,len(outputValue)):
        errorPart2.append(multiply(outputValue[i],1-outputValue[i]))
    #combine the error
    for i in range(0,len(errorPart1)):
        error.append(multiply(errorPart1[i],errorPart2[i]))
    return error


from FunInit import Init
from FunGetOutput import GetOutput
layerNum=[2,3,4]
inputData=[1,2]
target=[1,2,3,4]
weight=Init(layerNum)
outputValue=GetOutput(weight,inputData)
error=GetError(weight,target,outputValue)