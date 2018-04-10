import socket
import threading
import time
class packet_streamer(object):
    def __init__(self,ip='',port=''):
        self.ip=ip
        self.port=port
        self.soc=socket.socket()
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.stream_data=''
        self.connection=''
        self.bd_thread=''
        self.sock_client=''
        print("[DEBUGGER] : packet_streamer init")
    def bind_socket(self):
        self.soc.bind((self.ip,self.port))
        self.soc.listen(4)
        print("[DEBUGGER] : packet_streamer bind_socket{function - 1}")
    def set_data(self,data=[]):
        self.stream_data=data
        print("[DEBUGGER] : set_data - set ")
##    def get_connection(self):
##        FLAG=True
##        while FLAG:
##            c,addr=self.soc.accept()
##            if c is not None:
##                FLAG=False
##                self.sock_client=c
##                self.sock_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
##                
    def get_connection(self):
        c,addr=self.soc.accept()
        self.sock_client=c
        self.sock_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                
    def start_stream(self):
        def broadcast():
            while True:
                for i in self.stream_data:
                    try:
                        print("|SEN->DATA\\",str(i))
                        print("|LEN-_DATA\\",len(str(i)))
                        self.sock_client.send(bytes(str(i),"utf8"))
                    except:
                        pass
                    time.sleep(.5)
        self.bd_thread=threading.Thread(target=broadcast)
        self.bd_thread.daemon=True
        self.bd_thread.start()
    def stop_broadcast(self):
        self.bd_thread=None
        self.sock_client.close()
                
        
        
    
