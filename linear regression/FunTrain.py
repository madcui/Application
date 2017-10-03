#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:53:26 2017

@author: guangwei
"""
import numpy as np

from FunParam import Param
from FunGetOutput import GetOutput
from FunGetError import GetError
from FunUpdateWeight import UpdateWeight

def Train(weightInit, trainMIn, trainMOut, teParam):
    
    weightHistory=[]
    weightOld = weightInit
    for l in range(0, Param.loop):
        for i in range(0, Param.trainSize):
            nValue = GetOutput(weightOld, trainMIn[i, :])
            error = GetError(weightOld, trainMOut[i, :], nValue)
            weightNew = UpdateWeight (weightOld, nValue, error)
            weightOld = weightNew
            weightHistory.append(weightNew)

        tolCurrent = np.max(error[-1])
        if tolCurrent < Param.tolerance:
            return weightNew, weightHistory
    
    return weightNew, weightHistory