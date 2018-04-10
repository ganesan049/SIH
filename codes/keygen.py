from Crypto import Random
from Crypto.PublicKey import RSA

class GenKey(object):
    def __init__(self,passphrase):
        self.PRIVATE_k=''
        self.PUBLIC_k=''
        self.key=''
        self.random_gen=Random.new().read
        self.key=RSA.generate(2048, self.random_gen)
        self.PRIVATE_k,self.PUBLIC_k=self.key.exportKey(passphrase=passphrase), self.key.publickey().exportKey()
        
    def get_private_key(self):
        return self.PRIVATE_k
    def get_public_key(self):
        return self.PUBLIC_k
    
        
        
        
            

                        
        
