# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fr.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(307, 113)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.progressBar = QtGui.QProgressBar(Frame)
        self.progressBar.setGeometry(QtCore.QRect(20, 60, 261, 23))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Light"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.label.setText(_translate("Frame", "Initializing...", None))

    def setprogress(self,prg):
        self.progressBar.setProperty("value", prg)

