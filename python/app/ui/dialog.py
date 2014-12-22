# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui
import maya.cmds as cmds

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(150, 90)
        
        self.mainLayout = QtGui.QVBoxLayout(Dialog)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.layout_01 = QtGui.QHBoxLayout(Dialog)

        self.mainLayout.addLayout(self.horizontalLayout)
        self.mainLayout.addLayout(self.layout_01)

        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playblast_now = QtGui.QPushButton("Playblast")
        self.playblast_now.released.connect(self.happybirthday)
        self.logo_example = QtGui.QLabel(Dialog)
        self.logo_example.setText("")
        self.logo_example.setPixmap(QtGui.QPixmap(":/res/sg_logo.png"))
        self.logo_example.setObjectName("logo_example")
        self.horizontalLayout.addWidget(self.logo_example)
        self.context = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context.sizePolicy().hasHeightForWidth())
        self.context.setSizePolicy(sizePolicy)
        self.context.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.context.setObjectName("context")
        self.horizontalLayout.addWidget(self.context)
        self.layout_01.addWidget(self.playblast_now)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.context.setText(QtGui.QApplication.translate("Dialog", "Your Current Context: ", None, QtGui.QApplication.UnicodeUTF8))
    
    def happybirthday(self):
        print "Happy Birthday MAN!!!"
        cmds.playblast(format="qt", filename="C:/Temp/render.mov", forceOverwrite=True, sequenceTime=0, clearCache=1, viewer=1, showOrnaments=1, fp=4, percent=100, compression="H.264", quality=100, widthHeight=(1280,720))


from . import resources_rc
