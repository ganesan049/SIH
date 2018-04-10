from commpy.channelcoding import viterbi_decode as dec
from numpy import array
import commpy.channelcoding.convcode as cc

class decoder(object):
    def __init__(self):
        memory = array([6])
        g_matrix = array([[0b1111001,0b1011011]])
        self.trellis = cc.Trellis(memory, g_matrix)
    def decode(self,inp):
        print("[DEBUGGER] - start decode")
        out=dec(inp,self.trellis)
        print("[DEBUGGER] - end decode")
        return out
