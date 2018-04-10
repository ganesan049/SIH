import struct

class txt00(object):
    def __init__(self,data_x='',data_y=''):
        self.hc=data_x
        self.vc=data_y
        self.rtstr=""
    def float2b(self,value):
        return struct.unpack('Q', struct.pack('d', value))[0]
    def b2float(self,bits):
        return struct.unpack('d', struct.pack('Q', bits))[0]
    def _make(self):
        for x in self.hc:
            self.rtstr+=str(self.float2b(float(x)))
        for x in self.vc:
            self.rtstr+=str(self.float2b(float(x)))    
        return self.rtstr     
