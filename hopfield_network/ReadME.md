# Method and Dataset
- Hopfield network
- http://yann.lecun.com/exdb/mnist/
- grayscale, 28-by-28
- training set 60000 samples, test set 10000 samples.

## Aims:
- form 'memories' of the images 
- classify the digits
- change the form the free energy

### Steps:
1. funciton to pull all the data: trian, test, labels.
2. build the network: weights, learning rule, 
3. training or form memories
4. retrieve memory: given input image, find its 'memory'
5. add label nodes into the network to classifify the images

### Setup the network (discrete):
- the network has a number of 28^2 nodes.
- each nodes has tow states, 0 and 1.
- the connection is all-to-all, described by a matrix T, initialized with all zeros.
- neuron activity funciton: V_i = 1 if Sum_j{T_ij * V_j} > 0; V_i = 0 if Sum_j{T_ij * V_j} < 0.

### Train the network, form memory:
- Input a lot of pictures (binarized), T_ij = Sum_s{(2V_i^s - 1)(2V_j^s - 1)}
  - s is the index of the inputs picture, i and j are the index of neuron. 

### Retrieve memory:
- input a picture as the initial activity pattern, update the neuron states, until the steady state. 
