#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:13:20 2017

@author: guangwei
"""
import numpy as np
def NeuronNLFun(x):
    return 1/(1+np.exp(-x))