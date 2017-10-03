Method: Hopfield network.

Dataset: MNIST
http://yann.lecun.com/exdb/mnist/
grayscale, 28-by-28
training set 60000 samples, test set 10000 samples.

Aims:
1, form 'memories' of the images 
2, classify the digits
3, change the form the free energy

Steps:
1, funciton to pull all the data: trian, test, labels.
2, build the network: weights, learning rule, 
3, training or form memories
4, retrieve memory: given input image, find its 'memory'
5, add label nodes into the network to classifify the images