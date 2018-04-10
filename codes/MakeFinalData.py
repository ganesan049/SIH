##import fec_encoder as FecEnc
##import numpy as np
##class _make(object):
##    def __init__(self,inp=''):
##        self.fec_enc=FecEnc.encoder()
##        self.input=inp
##        self.r_d=[]
##        self.f_d=[]
##        #self.sync_word='0000000000000000'
##        self.sync_word='00000000000000'
##        for i in self.input:
##            self.r_d.append(self.fec_enc.conv_encoder(i,'000000'))
##    def returndata(self):
##        def _tostr(data):
##            rstr=''
##            for x in list(np.array_str(data[0])):
##                if x is '0' or x is '1':
##                    rstr+=x
##            return rstr        
##        for i in self.r_d:
##            t=_tostr(i)
##            self.f_d.append(self.sync_word+t)
##            print('--LEN FNL DAT /',len(self.sync_word+t))
##        return self.f_d            
##        
##        
import fec_encoder as FecEnc
import numpy as np
class _make(object):
    def __init__(self,inp=''):
        self.fec_enc=FecEnc.encoder()
        self.input=inp
        self.r_d=[]
        self.f_d=[]
        #self.sync_word='0000000000000000'
        self.sync_word='000000000000000000'
        for i in self.input:
            self.r_d.append(self.fec_enc.conv_encoder(i,'000000'))
    def returndata(self):
        def _tostr(data):
            rstr=''
            for x in list(np.array_str(data[0])):
                if x is '0' or x is '1':
                    rstr+=x
            return rstr        
        for i in self.r_d:
            t=_tostr(i)
            self.f_d.append(self.sync_word+t+"0")
            print('--LEN FNL DAT /',len(self.sync_word+t+"00"))
        return self.f_d            
        
        








