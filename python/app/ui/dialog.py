# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui
import maya.cmds as cmds
import sgtk
import tank
import os
from shutil import move
# import tank.templatekey
# from tank.platform import Application

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self._Default_TextField()

        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 200)

        self.mainLayout = QtGui.QVBoxLayout(Dialog)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.layout_01 = QtGui.QHBoxLayout(Dialog)
        self.layout_01_01 = QtGui.QVBoxLayout(Dialog)
        self.layout_01_02 = QtGui.QVBoxLayout(Dialog)
        self.layout_02 = QtGui.QHBoxLayout(Dialog)
        self.layout_03 = QtGui.QHBoxLayout(Dialog)

        self.mainLayout.addLayout(self.horizontalLayout)
        self.mainLayout.addLayout(self.layout_01)
        self.layout_01.addLayout(self.layout_01_01)
        self.layout_01.addLayout(self.layout_01_02)
        self.mainLayout.addLayout(self.layout_02)
        self.mainLayout.addLayout(self.layout_03)

        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playblast_now = QtGui.QPushButton("Playblast")
        self.outputLine = QtGui.QTextEdit()
        self.addressText = QtGui.QLabel("Output:")
        self.outputLine.setText('Path_Name')
        self.outputLine.setEnabled(False)
        self.outputLine.setMaximumSize(5000, 25)
        self.shot_Text = QtGui.QLabel("Shot:")
        self.shot_Field = QtGui.QTextEdit()
        self.shot_Field.setText(self.shot_Name)
        self.shot_Field.setMaximumHeight(25)
        self.shot_Field.textChanged.connect(self.textChanging)
        self.sequence_Text = QtGui.QLabel("Sequence:")
        self.sequence_Field = QtGui.QTextEdit()
        self.sequence_Field.setText(self.sequence_Name)
        self.sequence_Field.setMaximumHeight(25)
        self.sequence_Field.textChanged.connect(self.textChanging)
        self.version_Text = QtGui.QLabel("Version:")
        self.version_Field = QtGui.QTextEdit()
        self.version_Field.setText("001")
        # self.version_Field.setValidator(QtGui.QDoubleValidator())
        self.version_Field.setMaximumHeight(25)
        self.version_Field.textChanged.connect(self.textChanging)
        self.playblast_now.released.connect(self.do_Playblast)
        
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
        self.layout_02.addWidget(self.addressText)
        self.layout_02.addWidget(self.outputLine)
        self.layout_03.addWidget(self.playblast_now)
        self.layout_01_01.addWidget(self.sequence_Text)
        self.layout_01_01.addWidget(self.shot_Text)
        self.layout_01_01.addWidget(self.version_Text)
        self.layout_01_02.addWidget(self.sequence_Field)
        self.layout_01_02.addWidget(self.shot_Field)
        self.layout_01_02.addWidget(self.version_Field)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.textChanging()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.context.setText(QtGui.QApplication.translate("Dialog", "Your Current Context: ", None, QtGui.QApplication.UnicodeUTF8))
    
    def _Default_TextField(self):
        """
        Getting the default setting form shorgun and set them into text field.
        """
        self._app = sgtk.platform.current_bundle()
        self.tank_Path = self._app.get_setting("tank_address_field")
        self.shot_Name = self._app.context.entity["name"]
        self.tk = sgtk.sgtk_from_path(self.tank_Path)
        self.sequence_Name = self.tk.shotgun.find_one("Shot", [['code', 'is', self.shot_Name]], fields=['sg_sequence'])['sg_sequence']['name']
        self.stepName = self._app.context.step["name"]


    def textChanging(self):
        """
        Updating the Path whenever textfield has been changed.
        """
        baseTemplate = 'M:/defaultmultirootproject/[SEQUENCE]/[SHOT]/Reviews/[STEP]/work/R[VERSION]/[NAME].v[VERSION].mov'
        
        self.shotName = self.shot_Field.toPlainText()
        self.sequenceName = self.sequence_Field.toPlainText()
        self.versionNum = self.version_Field.toPlainText()

        self.finalOutput = 'M:/defaultmultirootproject/%s/%s/Reviews/%s/work/R%s/%s.v%s.mov'%(self.sequenceName,self.shotName,self.stepName,self.versionNum,self.shotName,self.versionNum)
        self.outputLine.setText(self.finalOutput)

    def do_Playblast(self):
        """
        getting the final Filed, Playblasting and publish it to shotgun
        """
        print "Playblast Starting..."

        #check the path of exist:
        base_Path = '//192.168.5.253/Lsa-projects-sg/m'
        self.output = (self.finalOutput.replace('M:',base_Path)).replace('%s.v%s.mov'%(self.shotName,self.versionNum),'')
        if not os.path.exists(self.output):
            print "Creating Server Folder..."
            os.makedirs(self.output)

        #set the File Name
        self.output = self.output + '%s.v%s.mov'%(self.shotName,self.versionNum)
        
        #local path
        self.localOutput = 'C:/Temp/%s.v%s.mov'%(self.shotName,self.versionNum)
        if not os.path.exists('C:/Temp'):
            print "Creating local Folder..."
            os.makedirs('C:/Temp/') 

        #Do the playblast
        cmds.playblast(format="qt", filename=self.localOutput, forceOverwrite=True, sequenceTime=0, clearCache=1, viewer=0, showOrnaments=1, fp=4, percent=100, compression="Photo - JPEG", quality=100, widthHeight=(1280,720))

        #Move the video to the Server directory 
        move(self.localOutput,self.output)

        #register the published file to the shotgun
        self._publish_playblast(self.tk, 
                                self._app.context,
                                self.finalOutput.replace('/','\\'),
                                self.shotName,
                                int(self.versionNum)
            )

    def _publish_playblast(self, tk_Path, context, publish_path, name, version):
        """
        Helper method to register publish using the 
        specified publish info.
        """
        # construct args:
        args = {
            "tk": tk_Path,
            "context": context,
            "path": publish_path,
            "name": name,
            "version_number": version,
        }
        
        # registering publish
        sg_data = tank.util.register_publish(**args)

from . import resources_rc
