import numpy as np
from math import factorial
import scipy.special as special



class trellis_nodes(object):
   
    def __init__(self,Ns):
        self.Ns = Ns
        self.fn = np.zeros((Ns,1),dtype=int) 
        self.tn = np.zeros((Ns,1),dtype=int)
        self.out_bits = np.zeros((Ns,1),dtype=int)

class trellis_branches(object):
   
    def __init__(self,Ns):
        self.Ns = Ns
        self.states1 = np.zeros((Ns,1),dtype=int)
        self.states2 = np.zeros((Ns,1),dtype=int)
        self.bits1 = np.zeros((Ns,1),dtype=int)
        self.bits2 = np.zeros((Ns,1),dtype=int)
        self.input1 = np.zeros((Ns,1),dtype=int)
        self.input2 = np.zeros((Ns,1),dtype=int)
class trellis_paths(object):
   
    def __init__(self,Ns,D):
        self.Ns = Ns
        self.decision_depth = D
        self.traceback_states = np.zeros((Ns,self.decision_depth),dtype=int)
        self.cumulative_metric = np.zeros((Ns,self.decision_depth),dtype=float)
        self.traceback_bits = np.zeros((Ns,self.decision_depth),dtype=int)

def binary(num, length=8):
        return format(num, '0{}b'.format(length))



class encoder(object):
    def __init__(self):
        self.G_polys = ('1111001','1011011')
        self.state='000000'
        self.constraint_length = len(self.G_polys[0]) 
        self.Nstates = 2**(self.constraint_length-1) # number of states
        self.decision_depth = 6
        self.input_zero = trellis_nodes(self.Nstates)
        self.input_one = trellis_nodes(self.Nstates)
        self.paths = trellis_paths(self.Nstates,self.decision_depth)
        for m in range(self.Nstates):
            self.input_zero.fn[m] = m
            self.input_one.fn[m] = m
            # state labeling with LSB on right (more common)
            output0,state0 = self.conv_encoder([0],
                             binary(m,self.constraint_length-1))
            output1,state1 = self.conv_encoder([1],
                             binary(m,self.constraint_length-1))
            self.input_zero.tn[m] = int(state0,2)
            self.input_one.tn[m] = int(state1,2)
            self.input_zero.out_bits[m] = 2*output0[0] + output0[1]
            self.input_one.out_bits[m] = 2*output1[0] + output1[1]

        self.branches = trellis_branches(self.Nstates)

        for m in range(self.Nstates):
            match_zero_idx = np.where(self.input_zero.tn == m)
            match_one_idx = np.where(self.input_one.tn == m)
            if len(match_zero_idx[0]) != 0:
                self.branches.states1[m] = self.input_zero.fn[match_zero_idx[0][0]]
                self.branches.states2[m] = self.input_zero.fn[match_zero_idx[0][1]]
                self.branches.bits1[m] = self.input_zero.out_bits[match_zero_idx[0][0]]
                self.branches.bits2[m] = self.input_zero.out_bits[match_zero_idx[0][1]]
                self.branches.input1[m] = 0
                self.branches.input2[m] = 0
            elif len(match_one_idx[0]) != 0:
                self.branches.states1[m] = self.input_one.fn[match_one_idx[0][0]]
                self.branches.states2[m] = self.input_one.fn[match_one_idx[0][1]]
                self.branches.bits1[m] = self.input_one.out_bits[match_one_idx[0][0]]
                self.branches.bits2[m] = self.input_one.out_bits[match_one_idx[0][1]]
                self.branches.input1[m] = 1
                self.branches.input2[m] = 1
            else:
                print('branch calculation error')
                exit(1)
    def conv_encoder(self,inp,state):
        output = []
        for n in range(len(inp)):
            u1 = int(inp[n])
            u2 = int(inp[n])
            for m in range(1,self.constraint_length):
                if int(self.G_polys[0][m]) == 1:
                    u1 = u1 ^ int(state[m-1])
                if int(self.G_polys[1][m]) == 1:
                    u2 = u2 ^ int(state[m-1])
            output = np.hstack((output, [u1, u2]))
            state = bin(int(inp[n]))[-1] + state[:-1]
        return output,state
        
