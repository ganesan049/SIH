
class binMake(object):
    def __init__(self):
        self.data=''
        self.stream_str=''
        self.bin_stream=''
        self.encoding='utf-8'
        self.errors='surrogatepass'
        self.lst=[]
        self.txt=''
        self.l8=[]
    def set(self,data):
        self.data=data
        for dat in self.data:
            self.stream_str+=dat.strip('\n')
    def set2(self,data):
        self.stream_str=data
##    def _tobin(self):
##        self.bin_stream = bin(int.from_bytes(self.stream_str.encode(
##            self.encoding, self.errors), 'big'))[2:]
##        self.bin_stream.zfill(8 * ((len(self.bin_stream) + 7) // 8)) 
    def _tobin(self):
        print(self.stream_str)
        def _make_block_id(id_val):
            tmp=''
            bin_val=len(id_val)
            if bin_val <8:
                for y in range(1,(8-(bin_val))+1):
                    tmp+='0'                    
            return tmp+id_val
        for x in self.stream_str:
            v=format(ord(str(x)),'b')
            v=_make_block_id(v)
            self.l8.append(v)
    def _to8(self):
        for y in self.l8:
            self.lst.append(y)
            self.txt+=y
        return self.lst,self.txt    
##    def _to8(self):
##        def _make_block_id(id_val):
##            tmp=''
##            binval=format(int(id_val),'b')
##            if len(binval) <8:
##                for y in range(1,(8-len(binval))+1):
##                    tmp+='0'                    
##            return tmp+binval
##        def chunks(s, n):
##            for start in range(0, len(s), n):
##                yield s[start:start+n]
##        for data in chunks(self.bin_stream,8):
##            
##            if len(data)<8:
##                _make_block_id(data)
##            self.lst.append(data)
##            self.txt+=data
##        return self.lst,self.txt        
                
