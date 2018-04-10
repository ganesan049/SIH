

class PckGen(object):
    def __init__(self,inp='',textid='',spare='',subframe='',h='',v=''):
        sFrame={
        1:"00",
        2:"01",
        3:"10",
        4:"11"
               }
        self.inputdata=inp        
        self.subframeid=sFrame[int(subframe)]
        self.textid=textid
        # symbol tlw $ end tail ~
#--------------------------------------------------------
#
# TLW |  PARAMS |  SUBFRAME _ID |
#       -| SPARE | MSG_ID | TXT_ID | BLOCK_COUNT |
#                temp_ar[](192bits) | PRN_ID | CRC | TAIL
#
#---------------------------------------------------------
        #packet parameters
        self.tlm='00100100'
        self.tail='100001'
        self.params='0000000000000000000'
        self.spare=spare
        self.msgid='0'+format(18,'b')
        self.netdata=[]
        self.temp_ar=[]
        self.prnid='000000'
        self.crc='000000000000000000000000'
        self.block_count=''
        self.temp_ar_final=[]
        #
    def _initz(self):
        
        def _make_25_1_test(make_obj):
            for data in make_obj:
                temp_make_str=''
                for q in range(len(data)):
                    for x in range(len(data[q])):
                        temp_make_str+=data[q][x]
                self.temp_ar_final.append(temp_make_str)
        def _make_25_1(make_obj):
            temp_make_str=''
            for y in range(len(make_obj)):
                for x in range(len(make_obj[y])):
                    temp_make_str+=make_obj[y][x]
            self.temp_ar_final.append(temp_make_str)    
        def parse(data):
            temp=""
            for i in data:
                temp+=str(data)
            return temp                
        for i in range(0,len(self.inputdata),25):
            len_data=self.inputdata[i:i+25]
            self.temp_ar.append((self.inputdata[i:i+25]))
        #self.block_count=format(len(self.temp_ar),'b')
        _make_25_1_test(self.temp_ar)
    def _make(self):
        def _make_block_id(id_val):
            tmp=''
            binval=format(int(id_val),'b')
            if len(binval) <8:
                for y in range(1,(8-len(binval))+1):
                    tmp+='0'                    
            return tmp+binval
        self.block_count=format(int(_make_block_id(len(self.temp_ar_final))),'b')
        def _make_200(id_val):
            def _make_block_id(id_val):
                tmp=''
                for y in range(1,(8-len(id_val))+1):
                    tmp+='0'                    
                return tmp+id_val
            print("---in",len(id_val))
            tmp=''
            head=''
            if len(id_val) <200:               
                for y in range(1,(200-len(id_val)-(8))+1):
                    tmp+='0'
                head=format(len(tmp),'b')
                head=_make_block_id(head)
                print("b4h",len(head))
                print('tmp',len(tmp))
                print('h',len(head))
                print('id',len(id_val))
            print("---out",len(head+tmp+id_val))
            return head+tmp+id_val
        count=1
        print("[Db] - len(C) ",len(self.temp_ar_final))
        self.block_count=format(len(self.temp_ar_final),'b')
        for i in range(len(self.temp_ar_final)):
            self.netdata.append(self.tlm+self.params+self.subframeid+
                                self.spare+self.msgid+self.textid
                                +_make_block_id(self.block_count)+_make_block_id(count)+
                                _make_200(str(self.temp_ar_final[i]))+self.prnid+self.crc+self.tail)
            count+=1
            #dubugger
##            print("-------")
##            print(len(self.tlm))
##            print(len(self.params))
##            print(len(self.subframeid))
##            print(len(self.spare))
##            print(len(self.msgid))
##            print(len(self.textid))
##            print(len(_make_block_id(self.block_count)))
##            print(len(_make_block_id(count)))
##            print(len((str(self.temp_ar_final[i]))))
##            print(len(self.prnid))
##            print(len(self.crc))
##            print(len(self.tail))
        return self.netdata            
        
        
