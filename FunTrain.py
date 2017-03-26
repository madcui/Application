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

def Train(weightInit, trainMIn, trainMOut, Param):
    
    weightOld = weightInit
    for l in range(0, Param.loop):
        for i in range(0, Param.trainSize):
            nValue = GetOutput(weightOld, trainMIn[i, :])
            error = GetError(weightOld, trainMOut[i, :], nValue)
            weightNew = UpdateWeight (weightOld, nValue, error)
            weightOld = weightNew

<<<<<<< HEAD
        tolCurrent = sum(error[-1])
=======
            #print(weightNew)

        tolCurrent = np.sum(error[-1])
>>>>>>> origin/master
        if tolCurrent < Param.tolerance:
            return weightNew
    
    return weightNew 