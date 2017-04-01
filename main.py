import numpy as np

from FunParam import Param
from FunGenerateData import GenerateData
from FunInit import Init
from FunTrain import Train
from FunTest import Test
from FunVisualizeTrainingProcess import VisualizeTrainingProcess

# generate data 
"""
(weightTarget, trainMIn, trainMOut, testMIn, testMOut) = GenerateData(Param.trainSize, Param.testSize, Param.numNode[0], Param.numNode[-1])
temp = trainMIn[1,:]
"""

# initialize the weight matrix
weightInit = Init(Param.numNode)

# train
(weightTrain, weightHistory) = Train(weightInit, trainMIn, trainMOut, Param)

#print(weightTrain)

if len(Param.numNode) == 2:
    wError = (weightTrain[0]- weightTarget[0])/weightTarget[0]
    (error,nodeError)=Test(weightTrain,testMIn,testMOut)
    print(np.max(wError))

if Param.plotFlag:
    VisualizeTrainingProcess (weightHistory, testMIn, testMOut, weightTarget, Param)