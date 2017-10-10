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

Setup the network (discrete):
1, the network has a number of 28^2 nodes.
2, each nodes has tow states, 0 and 1.
3, the connection is all-to-all, described by a matrix T, initialized with all zeros.
4, neuron activity funciton: V_i = 1 if Sum_j{T_ij * V_j} > 0; V_i = 0 if Sum_j{T_ij * V_j} < 0.

Train the network, form memory:
1, Input a lot of pictures (binarized), T_ij = Sum_s{(2V_i^s - 1)(2V_j^s - 1)}
2, s is the index of the inputs picture, i and j are the index of neuron. 

Retrieve memory:
1, input a picture as the initial activity pattern, update the neuron states, until the steady state. 