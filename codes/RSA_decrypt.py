from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
import base64
from io import StringIO

class RSA_dec(object):
    def __init__(self,PRIVATE_KEY,passphrase):
        self.decrypted_data=''
        self.passphrase=passphrase
        self.private_key=PRIVATE_KEY.decode("utf-8")
        self.pri_stream=''
        self.size=''
        self.encrypted_data=''
    def set_data(self,data):
        self.encrypted_data=data.encode("utf-8")
    def dec(self):
        cipher_text=base64.decodestring(self.encrypted_data)
        key_stream=StringIO(self.private_key)
        self.pri_stream=RSA.importKey(key_stream.read(),passphrase=self.passphrase)
        dsize=SHA.digest_size
        self.size=dsize
        sentinel = Random.new().read(15+dsize)
        cipher_enc=PKCS1_v1_5.new(self.pri_stream)
        self.decrypted_data=cipher_enc.decrypt(cipher_text,sentinel)
        digest = SHA.new(self.decrypted_data[:-dsize]).digest()
        if digest == self.decrypted_data[-dsize:]:
            return self.decrypted_data[:-dsize],"[DEBUGGER] decryption success"
        else:
            raise ValueError("[DEBUGGER] - Cannot decrypt")

    def get_decrypted_data(self):
        return self.decrypted_data[:-self.size].decode("utf-8")
