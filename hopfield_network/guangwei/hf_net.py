import numpy as np
import numpy.matlib

class HopfNet(object):
    def __init__(self, n):
        self.n = n
        self.w = np.zeros((n, n))
        self.train_times = 0

    def train(self, input_img):
        delta_w = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                delta_w[i][j] = (2 * input_img[i] - 1) * (2 * input_img[j] - 1)
        self.w = (self.train_times * self.w + delta_w)/(self.train_times + 1)
        index = range(self.n)
        self.w[index, index] = 0.
        self.train_times = self.train_times + 1

    def run_once(self, input_img):
        m = numpy.matlib.repmat(input_img, 1, self.n)
        m = self.w * m
        output = m.sum(1)
        output[output < 0.5] = 0
        output[output > 0.5] = 1
        output.shape= (self.n, 1)
        return output

    def retrieve(self, input_img):
        old_net = input_img
        new_net = self.run_once(input_img)
        while np.logical_not(np.all(new_net == old_net)):
            old_net = new_net
            new_net = self.run_once(old_net)
        return new_net
