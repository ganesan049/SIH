# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import xml_coord_get as xmlParser
import keygen as keyGenerator
import RSA_encrypt as RSAenc
import packets_broadcast as PCKbc
import threading
import time
import fec_encoder as FecEnc
import str_to_bin as sbin
import packetgenerator as PCKgen
import MakeFinalData as DF
import txt00 as txt00
#
#try
import popup
import streamui
#
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #
        self.obj_dat=''
        self.pgen=''
        self.list_18=''
        self.list_28=''
        self.sbin=sbin.binMake()
        self.sbin2=sbin.binMake()
        self.text_id='0001'
        self.subframe_set=3
        self.txt00=''
        #
        self.stream_1=''
        self.stream_2=''
        
        self.txt_1=''
        self.txt_2=''
        #
        self.brd_data=''
        self.Frame = QtGui.QFrame()
        self.ui = popup.Ui_Frame()
        self.Frame_stream = QtGui.QFrame()
        self.ui_stream = streamui.Ui_Frame()
        #
        #sockets
        self.sock=''
        #
        #class defenitions
        self.xml=''
        self.txtPUB=''
        self.txtPRI=''
        self.xmlPOS=''
        self.keygen=''
        self.publickey=''
        self.privatekey=''
        self.FIRST_TIME=True
        #
        #vars def
        self.HORZ=''
        self.VERT=''
        self.COORD_COUNT=''
        #
        self.lat=''
        self.lon=''
        self.radio=''
        self.txtIP=''
        self.txtPORT=''
        #
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(666, 542)
        MainWindow.setFixedSize(666, 542)
        MainWindow.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 281, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 671, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-30, 70, 711, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 90, 331, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 190, 331, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 280, 331, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 350, 641, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 370, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.radio1 = QtGui.QRadioButton(self.centralwidget)
        self.radio1.setGeometry(QtCore.QRect(10, 410, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        self.radio1.setFont(font)
        self.radio1.setObjectName(_fromUtf8("radio1"))
        self.radio2 = QtGui.QRadioButton(self.centralwidget)
        self.radio2.setGeometry(QtCore.QRect(10, 440, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        self.radio2.setFont(font)
        self.radio2.setObjectName(_fromUtf8("radio2"))
        self.radio3 = QtGui.QRadioButton(self.centralwidget)
        self.radio3.setGeometry(QtCore.QRect(10, 470, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        self.radio3.setFont(font)
        self.radio3.setObjectName(_fromUtf8("radio3"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(100, 380, 20, 131))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 260, 641, 20))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 170, 641, 20))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setMouseTracking(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineedit1 = QtGui.QLineEdit(self.centralwidget)
        self.lineedit1.setGeometry(QtCore.QRect(130, 430, 81, 20))
        self.lineedit1.setStyleSheet(_fromUtf8("lineedit1->setStyleSheet(\"background-color: yellow\");"))
        self.lineedit1.setObjectName(_fromUtf8("lineedit1"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 400, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(130, 460, 41, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineedit2 = QtGui.QLineEdit(self.centralwidget)
        self.lineedit2.setGeometry(QtCore.QRect(130, 490, 81, 20))
        self.lineedit2.setObjectName(_fromUtf8("lineedit2"))
        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(230, 380, 20, 131))
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 370, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setMouseTracking(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.key1 = QtGui.QLabel(self.centralwidget)
        self.key1.setGeometry(QtCore.QRect(250, 410, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(7)
        self.key1.setFont(font)
        self.key1.setObjectName(_fromUtf8("key1"))
        self.key2 = QtGui.QLabel(self.centralwidget)
        self.key2.setGeometry(QtCore.QRect(250, 440, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(7)
        self.key2.setFont(font)
        self.key2.setObjectName(_fromUtf8("key2"))
        self.genkeys = QtGui.QPushButton(self.centralwidget)
        self.genkeys.setGeometry(QtCore.QRect(350, 410, 91, 41))
        self.genkeys.setObjectName(_fromUtf8("genkeys"))
        self.genkeys2 = QtGui.QPushButton(self.centralwidget)
        self.genkeys2.setGeometry(QtCore.QRect(350, 470, 91, 41))
        self.genkeys2.setObjectName(_fromUtf8("genkeys2"))
        self.line_10 = QtGui.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(450, 380, 20, 131))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(490, 370, 141, 21))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(250, 470, 61, 21))
        self.streamstop = QtGui.QPushButton(self.centralwidget)
        self.streamstop.setGeometry(QtCore.QRect(520, 450, 61, 31))
        self.streamstop.setStyleSheet(_fromUtf8("QPushButton {color :red}"))
        self.streamstop.setObjectName(_fromUtf8("streamstop"))
        self.lineedit3 = QtGui.QLineEdit(self.centralwidget)
        self.lineedit3.setGeometry(QtCore.QRect(250, 490, 81, 20))
        self.lineedit3.setStyleSheet(_fromUtf8("lineedit1->setStyleSheet(\"background-color: yellow\");"))
        self.lineedit3.setObjectName(_fromUtf8("lineedit3"))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(470, 440, 181, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(470, 480, 188, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.upcoord = QtGui.QToolButton(self.centralwidget)
        self.upcoord.setGeometry(QtCore.QRect(430, 130, 25, 19))
        self.upcoord.setObjectName(_fromUtf8("upcoord"))
        self.path1 = QtGui.QLabel(self.centralwidget)
        self.path1.setGeometry(QtCore.QRect(100, 120, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.path1.setFont(font)
        self.path1.setMouseTracking(True)
        self.path1.setObjectName(_fromUtf8("path1"))
        self.uppublic = QtGui.QToolButton(self.centralwidget)
        self.uppublic.setGeometry(QtCore.QRect(430, 230, 25, 19))
        self.uppublic.setObjectName(_fromUtf8("uppublic"))
        self.path2 = QtGui.QLabel(self.centralwidget)
        self.path2.setGeometry(QtCore.QRect(100, 220, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.path2.setFont(font)
        self.path2.setMouseTracking(True)
        self.path2.setObjectName(_fromUtf8("path2"))
        self.upprivate = QtGui.QToolButton(self.centralwidget)
        self.upprivate.setGeometry(QtCore.QRect(430, 320, 25, 19))
        self.upprivate.setObjectName(_fromUtf8("upprivate"))
        self.path3 = QtGui.QLabel(self.centralwidget)
        self.path3.setGeometry(QtCore.QRect(100, 310, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(10)
        self.path3.setFont(font)
        self.path3.setMouseTracking(True)
        self.path3.setObjectName(_fromUtf8("path3"))
        self.uppos = QtGui.QToolButton(self.centralwidget)
        self.uppos.setGeometry(QtCore.QRect(610, 410, 25, 19))
        self.uppos.setObjectName(_fromUtf8("uppos"))
        self.pathpos = QtGui.QLabel(self.centralwidget)
        self.pathpos.setGeometry(QtCore.QRect(490, 400, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(8)
        self.pathpos.setFont(font)
        self.pathpos.setMouseTracking(True)
        self.pathpos.setObjectName(_fromUtf8("pathpos"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "GeoFence Application", None))
        self.label_2.setText(_translate("MainWindow", "Packet Generator - [ C&C center ]", None))
        self.label_3.setText(_translate("MainWindow", "V:0.1.0", None))
        self.label_4.setText(_translate("MainWindow", "Select GeoFence perimeter config file * (*. xml)", None))
        self.label_5.setText(_translate("MainWindow", "Select Public broadcast text file * (*. txt)", None))
        self.label_6.setText(_translate("MainWindow", "Select Private broadcast text file * (*. txt)", None))
        self.label_7.setText(_translate("MainWindow", "Set mode *", None))
        self.radio1.setText(_translate("MainWindow", "PUBLIC MODE", None))
        self.radio2.setText(_translate("MainWindow", "PRIVATE MODE", None))
        self.radio3.setText(_translate("MainWindow", "BOTH", None))
        self.label_8.setText(_translate("MainWindow", "TEST*", None))
        self.label_9.setText(_translate("MainWindow", "IP :", None))
        self.label_10.setText(_translate("MainWindow", "PORT :", None))
        self.label_11.setText(_translate("MainWindow", "GENERATE ENCRYPTION KEYS", None))
        self.key1.setText(_translate("MainWindow", "Private Key - HERE", None))
        self.key2.setText(_translate("MainWindow", "Public Key - HERE", None))
        self.genkeys.setText(_translate("MainWindow", "Gen Keys", None))
        self.genkeys2.setText(_translate("MainWindow", "Write Key to file", None))
        self.label_14.setText(_translate("MainWindow", "Config file for position data", None))
        self.commandLinkButton.setText(_translate("MainWindow", "VALIDATE AND STREAM", None))
        self.upcoord.setText(_translate("MainWindow", "...", None))
        self.path1.setText(_translate("MainWindow", "Path                                                                                                  :", None))
        self.uppublic.setText(_translate("MainWindow", "...", None))
        self.path2.setText(_translate("MainWindow", "Path                                                                                                  :", None))
        self.upprivate.setText(_translate("MainWindow", "...", None))
        self.path3.setText(_translate("MainWindow", "Path                                                                                                  :", None))
        self.uppos.setText(_translate("MainWindow", "...", None))
        self.streamstop.setText(_translate("MainWindow", "STOP", None))
        self.pathpos.setText(_translate("MainWindow", "Path                       -:", None))
        self.label_15.setText(_translate("MainWindow", "PassPhrase:", None))
        ##
        self.upcoord.clicked.connect(self.upcoord_func)
        self.uppublic.clicked.connect(self.uppublic_func)
        self.upprivate.clicked.connect(self.upprivate_func)
        self.uppos.clicked.connect(self.uppos_func)
        self.commandLinkButton.clicked.connect(self.commandLinkButton_func)
        self.genkeys.clicked.connect(self.genkeys_func)
        self.genkeys2.clicked.connect(self.genkeys2_func)
        self.radio1.clicked.connect(self.radio1_func)
        self.radio2.clicked.connect(self.radio2_func)
        self.radio3.clicked.connect(self.radio3_func)
        self.streamstop.clicked.connect(self.stopstream)
            
    
                
    def upcoord_func(self):
        xml_coords=QFileDialog.getOpenFileName()
        self.xml=xmlParser.xml_parser(xml_coords)
        #tage names val_h val_v
        self.xml.initz(h_tag_name="val_h",v_tag_name="val_v")
        self.HORZ=self.xml.parse_hkeys()
        self.VERT=self.xml.parse_vkeys()
        print("--COORD H_LEN |",len(self.HORZ))
        print("--COORD V_LEN |",len(self.VERT))
        self.COORD_COUNT=self.xml.get_coord_count()    
        self.path1.setText(xml_coords)
        print(self.HORZ)
        
    def uppublic_func(self):
        txt_public=QFileDialog.getOpenFileName()
        self.path2.setText(txt_public)
        f=open(txt_public,'r')
        self.txtPUB=f.readlines()
    def upprivate_func(self):
        txt_private=QFileDialog.getOpenFileName()
        self.path3.setText(txt_private)
        f=open(txt_private,'r')
        self.txtPRI=f.readlines()
    def uppos_func(self):
        xml_pos=QFileDialog.getOpenFileName()
        self.pathpos.setText(xml_pos)
        self.xmlPOS=xmlParser.xml_parser(xml_pos)
        self.xmlPOS.initz('val_lat','val_lon')
        self.lat=self.xmlPOS.parse_hkeys()[0]
        self.lon=self.xmlPOS.parse_vkeys()[0]
    def callback_sb(self,data):
        self.sbin.set(data)
        self.sbin._tobin()
        return self.sbin._to8()
    def stopstream(self):
        self.stream_1.stop_broadcast()
        
    def public_data_transfer(self):
        #self.Frame.show()
        self.txt00=txt00.txt00(self.HORZ,self.VERT)
        datac=self.txt00._make()
        self.sbin2.set(datac)
        self.sbin2._tobin()
        d8,dt=self.sbin2._to8()
        pck=PCKgen.PckGen(d8,"0000",'1',self.subframe_set)
        pck._initz()
        encd=pck._make()
        fdhead=DF._make(encd)
        fdhead=fdhead.returndata()

        ##
        self.list_18,self.txt_1=self.callback_sb(self.txtPUB)
        self.pckgen=PCKgen.PckGen(self.list_18,self.text_id,'0',self.subframe_set)
        self.pckgen._initz()
        self.encoded_data=self.pckgen._make()
        print("--",len(self.encoded_data[0]))
        self.obj_dat=DF._make(self.encoded_data)
        self.brd_data=self.obj_dat.returndata()

        self.brd_data=fdhead+self.brd_data
        self.stream_1=PCKbc.packet_streamer(self.lineedit1.text(),int(self.lineedit2.text()))
        self.stream_1.bind_socket()
        
        self.stream_1.set_data(self.brd_data)
        self.stream_1.get_connection()
        self.stream_1.start_stream()
    def private_data_transfer(self):
        pass
    def bothmode_data_transfer(self):
        pass
    def commandLinkButton_func(self):
        self.txtIP=self.lineedit1.text()
        self.txtPORT=self.lineedit2.text()
        
        #
        self.ui.setupUi(self.Frame)
        #
        self.ui_stream.setupUi(self.Frame_stream)
        #self.Frame_stream.show()
        #
        self.ui.setprogress(2)
        if self.radio is 'PUBLIC':
            self.public_data_transfer()
        elif self.radio is 'PRIVATE':
            self.private_data_transfer()
        elif self.radio is 'BOTH':
            self.bothmode_data_transfer()
        else:
            print("[DEBUGGER] - Error in selecting mode")
        print(self.radio)    
    def genkeys_func(self):
        if(self.FIRST_TIME):
            self.passphrase=self.lineedit3.text()
            self.keygen=keyGenerator.GenKey(self.passphrase)
            self.privatekey=self.keygen.get_private_key()
            self.publickey=self.keygen.get_public_key()
            self.key1.setText(self.privatekey[40:55].decode("utf-8")+"....")
            self.key2.setText(self.publickey[30:45].decode("utf-8")+"...")
            self.FIRST_TIME=False
    def genkeys2_func(self):
        file=open("PRIVATE_KEY.txt",'w+')
        file.write(self.privatekey.decode("utf-8"))
        file.close()
    def radio1_func(self):
        self.radio='PUBLIC'
    def radio2_func(self):
        self.radio='PRIVATE'
    def radio3_func(self):
        self.radio='BOTH'
    
    
    
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

