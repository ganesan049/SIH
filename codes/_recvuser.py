import stream_recv as recvbuffer
import time
import fec_decoder as fd
import numpy as np
import txt00
import geofence_poly_xy as geofencer
import xml_coord_get as xml
xml=xml.xml_parser("F:\SIH\codes\config\default_gps_coords.xml")

xml.initz('val_lat','val_lon')
lat_real=xml.parse_hkeys()
lon_real=xml.parse_vkeys()


b2f=txt00.txt00('','')

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
TXTIDe=40
BLKCs=40
BLKCe=48
BLKIs=48
BLKIe=56
TDATAs=56

TDATAe=256
PRNIDs=256
PRNIDe=262

FLAG={"coord_set":0}
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
def _toc(i):
    _v=int(i,2)
    _v=chr(_v)
    return _v

def d(data):
    head=data[:8]
    head=int(head,2)
    return data[head+8:]
blkcountcoord=0
blkidcoord=[]
datacoord={
    1:"",
2:"",
3:"",
4:"",
5:"",
6:"",
    7:""
    
}
lat=[]
lon=[]
geo=''
def _make_d():
    global lat,lon,geo,datacoord
    _tlatlon=[]
    def chunks(s, n):
        for start in range(0, len(s), n):
            yield s[start:start+n]
    _msg=""
    _tmp=""
    for i in range(1,8):
        _tmp+=datacoord[i]
    for _d in chunks(_tmp,19):
        _tlatlon.append(b2f.b2float(int(_d)))
    print("|GEO_F COORD SET -//")
    lat=_tlatlon[:4]
    lon=_tlatlon[4:]
    print("|LAT ` ",lat)
    print("|LONG ` ",lon)
    geo=geofencer.is_xy_inside_poly(lat,lon,len(lat))
    geo.initialize_vals()
    print("|G_SET //")
    
def get_coord(inp):
    global blkcountcoord,blkidcoord,datacoord
    txtid=_toi(inp[TXTIDs:TXTIDe])
    if txtid == 0:
        blkcountcoord=int(str(_toi(inp[BLKCs:BLKCe])),2)
        blkid=_toi(inp[BLKIs:BLKIe])
        print("blk id",blkid)
        if blkcountcoord == len(blkidcoord):
            FLAG["coord_set"]=1
            _make_d()
        if blkid in blkidcoord:
            if blkcountcoord == len(blkidcoord):
                FLAG["coord_set"]=1
                _make_d()
                
        else:
            if blkid == blkcountcoord:
                blkidcoord.append(blkid)
                datacoord[blkid]=_msg(d(inp[56:256]))
                print("_msg1",_msg(d(inp[56:256])))
                if blkcountcoord == len(blkidcoord):
                    FLAG["coordset"]=1
                    _make_d()
            else:
                blkidcoord.append(blkid)
                datacoord[blkid]=_msg(inp[56:256])
                print("_msg2",_msg(inp[56:256]))
                if blkcountcoord == len(blkidcoord):
                    FLAG["coord_set"]=1
                    _make_d()
    print("-----STAT------\n")
    print("coord-",blkidcoord)
    print("txtid",txtid)
    
    print("cnt-",blkcountcoord)
    print("DAT__",datacoord)
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
    print("| DECODING END#")
    td2["spare"]=data[SPAREs:SPAREe]
    td2["data"]=data[TDATAs:TDATAe]
    td2["msgid"]=data[MSGIDs:MSGIDe]
    if FLAG["coord_set"] == 0:
        print("COORDINATE RECEIVING IN PROGRESS//")
        get_coord(data)
        


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
    if a is not '':
        data_func_1(a)
