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
# import tank.templatekey
# from tank.platform import Application

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 200)

        self._app = sgtk.platform.current_bundle()
        tank_Path = self._app.get_setting("tank_address_field")
        shot_Name = self._app.context.entity["name"]
        tk = sgtk.sgtk_from_path(tank_Path)
        sequence_Name = tk.shotgun.find_one("Shot", [['code', 'is', shot_Name]], fields=['sg_sequence'])['sg_sequence']['name']
        self.stepName = self._app.context.step["name"]

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
        self.outputLine.setText('M:/defaultmultirootproject/[SEQUENCE]/[SHOT]/Reviews/%s/work/R[VERSION]/[NAME].v[VERSION].mov'%self.stepName )
        self.outputLine.setEnabled(False)
        self.outputLine.setMaximumSize(5000, 25)
        self.shot_Text = QtGui.QLabel("Shot:")
        self.shot_Field = QtGui.QTextEdit()
        self.shot_Field.setText(shot_Name)
        self.shot_Field.setMaximumHeight(25)
        self.shot_Field.textChanged.connect(self.textChanging)
        self.sequence_Text = QtGui.QLabel("Sequence:")
        self.sequence_Field = QtGui.QTextEdit()
        self.sequence_Field.setText(sequence_Name)
        self.sequence_Field.setMaximumHeight(25)
        self.sequence_Field.textChanged.connect(self.textChanging)
        self.version_Text = QtGui.QLabel("Version:")
        self.version_Field = QtGui.QTextEdit()
        self.version_Field.setText("001")
        # self.version_Field.setValidator(QtGui.QDoubleValidator())
        self.version_Field.setMaximumHeight(25)
        self.version_Field.textChanged.connect(self.textChanging)
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

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.context.setText(QtGui.QApplication.translate("Dialog", "Your Current Context: ", None, QtGui.QApplication.UnicodeUTF8))
    
    def textChanging(self):
        self._app = sgtk.platform.current_bundle()
        self.stepName = self._app.context.step["name"]
        baseTemplate = 'M:/defaultmultirootproject/[SEQUENCE]/[SHOT]/Reviews/[STEP]/work/R[VERSION]/[NAME].v[VERSION].mov'
        
        self.shotName = self.shot_Field.toPlainText()
        self.sequenceName = self.sequence_Field.toPlainText()
        self.versionNum = self.version_Field.toPlainText()

        finalOutput = 'M:/defaultmultirootproject/%s/%s/Reviews/%s/work/R%s/%s.v%s.mov'%(self.sequenceName,self.shotName,self.stepName,self.versionNum,self.shotName,self.versionNum)
        self.outputLine.setText(finalOutput)


    def happybirthday(self):
        print "Playblast Starting..."
        #outputPAth = self.get_template("movie_path_template")
        self.textChanging()
        finalOutput = 'M:/defaultmultirootproject/%s/%s/Reviews/%s/work/R%s/'%(self.sequenceName,self.shotName,self.stepName,self.versionNum)
        if os.path.exists(finalOutput):
            print "Yeay"
        else:
            os.makedirs(finalOutput)
        cmds.playblast(format="qt", filename=('%s%s.v%s.mov'%(finalOutput,self.shotName,self.versionNum)).replace('/','\\'), forceOverwrite=True, sequenceTime=0, clearCache=1, viewer=1, showOrnaments=1, fp=4, percent=100, compression="Photo - JPEG", quality=100, widthHeight=(1280,720))

        # if "PNGMOV" not in os.listdir(baseDir):
        #             os.makedirs(destDir)
        # self._app = sgtk.platform.current_bundle()
        # output_Tempelate = self._app.get_template("export_movie_template")
        # shot_Name = self._app.context.entity["name"]
        # stepName = self._app.context.step["name"]
        # tank_Path = self._app.get_setting("tank_address_field")
        # tk = sgtk.sgtk_from_path(tank_Path)
        # sequence_Name = tk.shotgun.find_one("Shot", [['code', 'is', shot_Name]], fields=['sg_sequence'])['sg_sequence']['name']




        # self._work_template = self._app.get_template("movie_path_template")
from . import resources_rc
