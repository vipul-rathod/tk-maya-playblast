# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 392)
        #Creating Layout
        mainLayout = QtGui.QHBoxLayout(self)
        Layout_01 = QtGui.QVBoxLayout(self)
        Layout_02 = QtGui.QVBoxLayout(self)
        Layout_03 = QtGui.QVBoxLayout(self)
        
        #Creating Objects
        episode_txt = QtGui.QLabel("Episodes:")
        episode_list = QtGui.QListWidget()
        shot_txt = QtGui.QLabel("Shots:")
        shot_list = QtGui.QListWidget()
        version_txt = QtGui.QLabel("Versions:")
        version_list = QtGui.QListWidget()
        
        #Connecting Layouts
        mainLayout.addLayout(Layout_01)
        mainLayout.addLayout(Layout_02)
        mainLayout.addLayout(Layout_03)
        
        #Connecting Widget
        Layout_01.addWidget(episode_txt)
        Layout_01.addWidget(episode_list)
        Layout_02.addWidget(shot_txt)
        Layout_02.addWidget(shot_list)
        Layout_03.addWidget(version_txt)
        Layout_03.addWidget(version_list)
        
        #Widgets Actions
        EpList = []
        episodePath = "i:/bubblebathbay/episodes"
        for eachfile in os.listdir(episodePath):
            print eachfile
            if os.path.isdir("%s/%s"%(episodePath,eachfile)):
                EpList.append(eachfile)
        EpList.sort()
        episode_list.addItems(EpList)

from . import resources_rc
