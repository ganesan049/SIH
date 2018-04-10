from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
import base64
from io import StringIO

class RSA_enc(object):
    def __init__(self,PUBLIC_KEY):
        self.data=''
        self.public_key=PUBLIC_KEY.decode("utf-8")
        self.pub_stream=''
        self.encrypted_data=''
    def set_data(self,data):
        self.data=data.encode("utf-8")
    def enc(self):
        key_stream=StringIO(self.public_key)
        self.pub_stream=RSA.importKey(key_stream.read())
        sha=SHA.new(self.data)
        cipher_enc=PKCS1_v1_5.new(self.pub_stream)
        self.encrypted_data=base64.encodestring(cipher_enc.encrypt(self.data+sha.digest()))
    def get_encrypted_data(self):
        return self.encrypted_data.decode("utf-8")
