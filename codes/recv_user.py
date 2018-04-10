import stream_recv as recvbuffer
import time
import fec_decoder as fd
import numpy as np
TLMs=0
TLMe=9
SIDs=27
SIDe=29
SPAREs=29
SPAREe=30
TAILs=286
TAILe=292
DATAs=36
DATAe=256
#ok
MSGIDs=30
MSGIDe=36
#-1   -1
TXTIDs=36
TXTIDe=48
BLKCs=40
BLKCe=48
BLKIs=48
BLKIe=56
TDATAs=56

TDATAe=256
PRNIDs=256
PRNIDe=262

td={
    "tlm":"",
    "s_id":"",
    "spare":"",
    "data":"",
    "tail":"",
    "msgid":"",
    "txtid":"",
    "blkcount":"",
    "blkid":"",
    "txtdata":"",
    "prnid":""
   }
DICT={}
DICT["txtidcount"]=[]
DICT["completedtxtid"]=[]

def comp(d):
    msg=""
    def chunks(s, n):
            for start in range(0, len(s), n):
                yield s[start:start+n]
                    
    data=DICT[d]["textdata"]
    for x in data:
        msg+=x
    print("|-[DECODE] // sub_text")        
    return msg       
def _msg(d):
    def chunks(s, n):
        for start in range(0, len(s), n):
            yield s[start:start+n]
    msg=""
    for x in chunks(d,8):
        _t=int(x,2)
        _t=chr(_t)
        msg+=_t
    return msg    
def _toi(i):
    _v=int(i,2)
    return _v
def d(data):
    head=data[:8]
    head=int(head,2)
    return data[(len(data)-head)-8:]
    
    
def logic_1(data,td):
    global DICT
    td["txtid"]=data[TXTIDs:TXTIDe]
    
    td["blkcount"]=data[BLKCs:BLKCe]
    td["blkid"]=data[BLKIs:BLKIe]
    td["txtdata"]=data[TDATAs:TDATAe]
    
    txtid=_toi(td["txtid"])
    blkc=_toi(td["blkcount"])
    blkid=_toi(td["blkid"])
    msg=_msg(td["txtdata"])
    
    if txtid in DICT:
        if blkid in DICT[txtid]["blockid"]:
            if blkid in DICT[txtid]["blockid"]:
                return
            else:
                DICT[txtid]["textdata"][blkc]=_msg(d(td["txtdata"]))
                return
        if blkid is len(DICT[txtid][blkc]):
            if td["txtid"] is "0000":
                pass
            else:
                comp(txtid)
                
        else:
            if blkid == len(DICT[td["txtid"]]["blockid"]):
                DICT[td["txtid"]]["blockid"].append(td["blkid"])
                DICT[td["txtid"]]["textdata"][blkid]=d(td["txtdata"])
            else:    
                DICT[td["txtid"]]["blockid"].append(td["blkid"])
                DICT[td["txtid"]]["textdata"][blkid]=td["txtdata"]
            
            
    else:
        DICT[txtid]={}
        DICT[txtid]["blockcount"]=blkc
        DICT[txtid]["blockid"]=[]
        DICT[txtid]["blockid"].append(blkid)
        DICT[txtid]["textdata"]={}
        DICT[txtid]["textdata"][blkid]=td["txtdata"]
        
    



def data_func_1(data):
    global td
    td2=td
    print("------------------")
    print("| DECODING LOGIC#")
    print("|RECV LEN-",len(data))
    print("|RECV DATA-",data)
    _dat=data[16:]
    print(",..",_dat)
    print("+++",len(_dat))
    _lst=[]
    for x in _dat:
        _lst.append(x)
    data=decoder.decode(np.array(_lst))
    print(len(np.atleast_1d(data)))
    print((data))
    strtmp=""
    for x in data:
        strtmp+=str(x)
    data=strtmp
    print(data)
    input()
    print("| DECODING END#")
    td2["tlm"]=data[TLMs:TLMe]
    td2["s_id"]=data[SIDs:SIDe]
    td2["spare"]=data[SPAREs:SPAREe]
    td2["data"]=data[DATAs:DATAe]
    td2["tail"]=data[TAILs:TAILe]
    td2["msgid"]=data[MSGIDs:MSGIDe]
    if int(td2["msgid"],2) ==18:
        logic_1(td2["data"],td2)
    



##ip=input(" | Enter IP: ")
##port=input(" | ENTER PORT :")
##recv=recvbuffer.stream_data_recv(ip,int(port))

##recv=recvbuffer.stream_data_recv('192.168.43.49',12345)
recv=recvbuffer.stream_data_recv('127.0.0.1',12345)
decoder=fd.decoder()
recv._connect()
recv._start_thread()



time.sleep(1)


while 1:
    a=recv.get_data().decode("utf8")
    data_func_1(a)
