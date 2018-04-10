import socket
import threading

class stream_data_recv(object):
    def __init__(self,ip='',port=12345):
        self.ip=ip
        self.port=port
        self.sock=socket.socket()
        self.current_packet=''
        self.recv_thread=''
    def _connect(self):
        self.sock.connect((self.ip,self.port))
##    def get_data(self):
##        return self.current_packet.decode("utf-8")
            
    def get_data(self):
        return self.current_packet[2:-1]
    def _start_thread(self):
        def thr_start():
            while 1:
                inp_data=self.sock.recv(1024)
                if not (inp_data == b''):
                    self.current_packet=inp_data
                else:
                    self.sock=socket.socket()
                    self.sock.connect((self.ip, self.port))
        self.recv_thread=threading.Thread(target=thr_start)
        self.recv_thread.daemon=True
        self.recv_thread.start()
    def stop_kthread(self):
        self.recv_thread=None
        
