#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:12:12 2017

@author: guangwei
"""

import numpy as np

class Param: 
    # parameters for the training process
    loop = 80      #number of times to train the data set
    tolerance = 10**-6      #tolerance to terminate the training
    plotFlag = 1    # flag of visualizing the training process. 1 yes, 0 no.
    
    # parameters for the datasets
    trainSize = 100     #sample size of the training dataset
    testSize =  10      #sample size fo the testing dataset
    
    # structure of the network
    numNode = [10,4]


"""
# test
print(Param.loop)
print(Param.testSize)
"""