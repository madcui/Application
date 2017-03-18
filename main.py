import numpy as np

from FunParam import Param
from FunGenerateData import GenerateData
from FunInit import Init
from FunTrain import Train

# generate data 
(weightTarget, trainMIn, trainMOut, testMIn, testMOut) = GenerateData(Param.trainSize, Param.testSize, Param.numNode[0], Param.numNode[-1])

# initialize the weight matrix
weightInit = Init(Param.numNode)

# train
weightTrain = Train(weightInit, trainMIn, trainMOut, Param)

print(weightTrain)