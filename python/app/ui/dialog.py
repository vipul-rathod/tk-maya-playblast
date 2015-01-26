# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui
import maya.cmds as cmds
import tank
import os, time, subprocess
from shutil import move

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self._app = tank.platform.current_bundle()
        self.tk = self._app.engine._TankBundle__tk
        self.ctx = self._app.engine._TankBundle__context
        self.project_name = self.ctx.project["name"]
        self.shot_name = self.ctx.entity["name"]
        self.sequence_name = self.tk.shotgun.find_one("Shot", [['code', 'is', self.shot_name]], fields=['sg_sequence'])['sg_sequence']['name']
        self.step_name = self.ctx.step["name"]
        self.name = self.shot_name.replace("_", "")
        self.main01()
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 200)

        self.mainLayout = QtGui.QVBoxLayout(Dialog)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.layout_01 = QtGui.QHBoxLayout(Dialog)
        self.layout_01_01 = QtGui.QVBoxLayout(Dialog)
        self.layout_01_02 = QtGui.QVBoxLayout(Dialog)
        self.layout_02 = QtGui.QHBoxLayout(Dialog)
        self.layout_02_01 = QtGui.QVBoxLayout(Dialog)
        self.layout_02_02 = QtGui.QVBoxLayout(Dialog)
        self.layout_03 = QtGui.QHBoxLayout(Dialog)
        self.layout_03_01 = QtGui.QVBoxLayout(Dialog)
        self.layout_03_02 = QtGui.QVBoxLayout(Dialog)
        self.layout_04 = QtGui.QHBoxLayout(Dialog)

        self.mainLayout.addLayout(self.horizontalLayout)
        self.mainLayout.addLayout(self.layout_01)
        self.layout_01.addLayout(self.layout_01_01)
        self.layout_01.addLayout(self.layout_01_02)
        self.mainLayout.addLayout(self.layout_02)
        self.layout_02.addLayout(self.layout_02_01)
        self.layout_02.addLayout(self.layout_02_02)
        self.mainLayout.addLayout(self.layout_03)
        self.layout_03.addLayout(self.layout_03_01)
        self.layout_03.addLayout(self.layout_03_02)
        self.mainLayout.addLayout(self.layout_04)

        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playblast_now = QtGui.QPushButton("Playblast")
        self.project_Text = QtGui.QLabel("Project:")
        self.project_Field = QtGui.QTextEdit()
        self.project_Field.setText(self.project_name)
        self.project_Field.setMaximumSize(5000, 25)
        self.address_Text = QtGui.QPushButton("Output:")
        self.address_Text.setMaximumWidth(50)
        self.address_Text.released.connect(self.open_folder)
        self.output_Field = QtGui.QTextEdit()
        self.output_Field.setText(self.path)
        self.output_Field.setEnabled(False)
        self.output_Field.setMaximumSize(5000, 25)
        self.shot_Text = QtGui.QLabel("Shot:")
        self.shot_Field = QtGui.QTextEdit()
        self.shot_Field.setText(self.shot_name)
        self.shot_Field.setMaximumHeight(25)
        self.sequence_Text = QtGui.QLabel("Sequence:")
        self.sequence_Field = QtGui.QTextEdit()
        self.sequence_Field.setText(self.sequence_name)
        self.sequence_Field.setMaximumHeight(25)
        self.version_Text = QtGui.QLabel("Version:")
        self.version_Field = QtGui.QTextEdit()
        self.version_Field.setText(str(self.fields["version"]))
        self.comment_Text = QtGui.QLabel("Comment:")
        self.comment_Text.setAlignment(QtCore.Qt.AlignTop)
        self.comment_Field = QtGui.QTextEdit()
        self.comment_Field.setText("")
        self.version_Field.setMaximumHeight(25)
        self.playblast_now.released.connect(self.playblast_and_publish)
        
        self.context = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context.sizePolicy().hasHeightForWidth())
        self.context.setSizePolicy(sizePolicy)
        self.context.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.context.setObjectName("context")
        
        self.horizontalLayout.addWidget(self.context)
        self.layout_01_01.addWidget(self.project_Text)
        self.layout_01_01.addWidget(self.sequence_Text)
        self.layout_01_01.addWidget(self.shot_Text)
        self.layout_01_01.addWidget(self.version_Text)
        self.layout_01_02.addWidget(self.project_Field)
        self.layout_01_02.addWidget(self.sequence_Field)
        self.layout_01_02.addWidget(self.shot_Field)
        self.layout_01_02.addWidget(self.version_Field)
        self.layout_02_01.addWidget(self.comment_Text)
        self.layout_02_02.addWidget(self.comment_Field)
        self.layout_03_01.addWidget(self.address_Text)
        self.layout_03_02.addWidget(self.output_Field)
        self.layout_04.addWidget(self.playblast_now)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.context.setText(QtGui.QApplication.translate("Dialog", "Your Current Context: ", None, QtGui.QApplication.UnicodeUTF8))

    def main01(self):
        self.publish_template = self._app.engine.get_template_by_name("maya_shot_custom_playblast")
        self.fields = {}
        self.fields["Sequence"] = self.sequence_name
        self.fields["Shot"] = self.shot_name
        self.fields["Step"] = self.step_name
        self.fields["date"] = time.strftime("%y%m%d")
        self.fields["name"] = self.name
        self.fields["version"] = 1
        tmp_file_path = self.publish_template.apply_fields(self.fields)
        file_dir = tmp_file_path.split(os.path.basename(tmp_file_path))[0]
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        else:
            pass
        list_files = self.listFilesWithParticularExtensions(file_dir, self.name)
        if list_files:
            latest_file = max(list_files)
            self.fields["version"] = int(os.path.splitext(latest_file)[0].split('.v')[1]) + 1
            self.path = self.publish_template.apply_fields(self.fields)
            print 'Version Path: %s' % self.path
        else:
            self.fields["version"] = 1
            self.path = self.publish_template.apply_fields(self.fields)
            print 'Version Path: %s' % self.path

#    Check the existing versions
    def listFilesWithParticularExtensions(self, file_path, file_prefix):
        files = [ f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path,f)) and f.startswith('%s' % file_prefix) and f.endswith(f.split(os.path.extsep)[-1]) and f.__contains__('.v')]
        if files:
            return files
        else:
            return False

    def playblast_and_publish(self):
        self.main01()
        #    Playblast in local and move to server
        local_dir = 'C:/Temp'
        if not os.path.exists(local_dir):
            os.mkdir(local_dir)
        local_path = os.path.join(local_dir, os.path.basename(self.path))
        
        if os.path.exists(local_path):
            os.remove(local_path)
        cmds.playblast(format="qt", filename= local_path, forceOverwrite=True, sequenceTime=0, clearCache=1, viewer=0, showOrnaments=1, fp=4, percent=100, compression="Photo - JPEG", quality=70, widthHeight=(1280,720))
        
        #    Publish playblast
        move(local_path, self.path)
        verData= {
                "code": os.path.basename(self.path),
                "entity": self.ctx.entity,
                "sg_task": self.ctx.task,
                "project": self.ctx.project,
                "description": self.comment_Field.toPlainText(),
                "sg_path_to_movie": self.path,
        }

        sg_version = self._app.tank.shotgun.create("Version", verData)
        self._app.tank.shotgun.upload("Version", sg_version["id"], self.path, "sg_uploaded_movie")
        cmds.confirmDialog(t='Playblast Published', m='Playblast finished and published to shotgun', b='Ok')

    def open_folder(self):
        subprocess.check_call(['explorer', self.path.split(os.path.basename(self.path))[0]])