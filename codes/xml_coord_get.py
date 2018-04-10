from xml.dom import minidom

class xml_parser(object):
    def __init__(self,xml_path=''):
        self.path=xml_path
        self.horizontal_tag_name=''
        self.vertical_tag_name=''
        self.xml=''
    def initz(self,h_tag_name='',v_tag_name=''):
        self.horizontal_tag_name=h_tag_name
        self.vertical_tag_name=v_tag_name
        self.xml=minidom.parse(self.path)
    def parse_hkeys(self):    
        list_1=[]
        item_1=self.xml.getElementsByTagName(self.horizontal_tag_name)
        for x in range(len(item_1)):
            list_1.append(item_1[x].attributes['value'].value)
        return list_1            
    def parse_vkeys(self):    
        list_2=[]
        item_2=self.xml.getElementsByTagName(self.vertical_tag_name)
        for x in range(len(item_2)):
            list_2.append(item_2[x].attributes['value'].value)
        return list_2
    def get_coord_count(self):
        dummy=self.xml.getElementsByTagName(self.vertical_tag_name)
        return len(dummy)
        
