#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:28:05 2017

@author: guangwei
"""
from FunParam import Param
from FunTest import Test
from FunVisualizeNet import VisualizeNet

def VisualizeTrainingProcess (wHistroy, testMIn, testMOut, wTarget, Param):
    total = len(wHistroy)
    l = 0
    while (l<total-1):
        w = wHistroy[l]
        (error,nodeError)=Test(w,testMIn,testMOut)
        VisualizeNet(w, nodeError.transpose(), wTarget, Param)
        l = l+Param.plotInterval
    return