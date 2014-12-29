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
        self.project_Field.setText(self.project_Name)
        self.project_Field.setMaximumSize(5000, 25)
        self.address_Text = QtGui.QLabel("Output:")
        self.output_Field = QtGui.QTextEdit()
        self.output_Field.setText("Path_Name")
        self.output_Field.setEnabled(False)
        self.output_Field.setMaximumSize(5000, 25)
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
        self.comment_Text = QtGui.QLabel("Comment:")
        self.comment_Text.setAlignment(QtCore.Qt.AlignTop)
        self.comment_Field = QtGui.QTextEdit()
        self.comment_Field.setText("")
        # self.version_Field.setValidator(QtGui.QDoubleValidator())
        self.version_Field.setMaximumHeight(25)
        self.version_Field.textChanged.connect(self.textChanging)
        self.playblast_now.released.connect(self.do_Playblast)
        
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
        self.project_Name = self._app.context.project["name"]
        self.tk = sgtk.sgtk_from_path(self.tank_Path)
        self.sequence_Name = self.tk.shotgun.find_one("Shot", [['code', 'is', self.shot_Name]], fields=['sg_sequence'])['sg_sequence']['name']
        self.stepName = self._app.context.step["name"]


    def textChanging(self):
        """
        Updating the Path whenever textfield has been changed.
        """
        baseTemplate = 'M:/[PROJECT]/[SEQUENCE]/[SHOT]/Reviews/[STEP]/work/R[VERSION]/[NAME].v[VERSION].mov'
        
        self.shotName = self.shot_Field.toPlainText()
        self.sequenceName = self.sequence_Field.toPlainText()
        self.versionNum = self.version_Field.toPlainText()
        self.projectName = self.project_Field.toPlainText()
        self.defaultComment = self.comment_Field.toPlainText()

        self.finalOutput = 'M:/%s/%s/%s/Reviews/%s/work/R%s/%s.v%s.mov'%(self.projectName,self.sequenceName,self.shotName,self.stepName,self.versionNum,self.shotName,self.versionNum)
        self.output_Field.setText(self.finalOutput)

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
        cmds.playblast(format="qt", filename=self.localOutput, forceOverwrite=True, sequenceTime=0, clearCache=1, viewer=0, showOrnaments=1, fp=4, percent=100, compression="Photo - JPEG", quality=70, widthHeight=(1280,720))

        #Move the video to the Server directory 
        move(self.localOutput,self.output)

        #default Comment
        if self.defaultComment == "":
            self.defaultComment = "None"

        # create and upload new version to shotgun
        self._version_playblast(self.shotName,
                                self._app.context.entity,
                                self._app.context.task,
                                self._app.context.project,
                                self.defaultComment,
                                self.finalOutput.replace('/','\\'),
                                )

    def _publish_playblast(self, tk_Path, context, publish_path, name, version):
        """
        Helper method to register publish using the 
        specified publish info.
        Required parameters:

            tk - a Sgtk API instance

            context - the context we want to associate with the publish

            path - the path to the file or sequence we want to publish. If the
                   path is a sequence path it will be abstracted so that
                   any sequence keys are replaced with their default values.

            name - a name, without version number, which helps distinguish
                   this publish from other publishes. This is typically
                   used for grouping inside of Shotgun so that all the
                   versions of the same "file" can be grouped into a cluster.
                   For example, for a maya publish, where we track only
                   the scene name, the name would simply be that: the scene
                   name. For something like a render, it could be the scene
                   name, the name of the AOV and the name of the render layer.

            version_number - the version numnber of the item we are publishing.

        Optional arguments:

            task - a shotgun entity dictionary with id and type (which should always be Task).
                   if no value is specified, the task will be grabbed from the context object.

            comment - a string containing a description of the comment

            thumbnail_path - a path to a thumbnail (png or jpeg) which will be uploaded to shotgun
                             and associated with the publish.

            dependency_paths - a list of file system paths that should be attempted to be registered
                               as dependencies. Files in this listing that do not appear as publishes
                               in shotgun will be ignored.

            dependency_ids - a list of publish ids which should be registered as dependencies.

            published_file_type - a tank type in the form of a string which should match a tank type
                                that is registered in Shotgun.

            update_entity_thumbnail - push thumbnail up to the attached entity

            update_task_thumbnail - push thumbnail up to the attached task

            created_by - override for the user that will be marked as creating the publish.  This should
                        be in the form of shotgun entity, e.g. {"type":"HumanUser", "id":7}

            created_at - override for the date the publish is created at.  This should be a python
                        datetime object
                        
            version_entity - the Shotgun version entity this published file should be linked to 
        """
        #construct args:
        args = {
            "tk": tk_Path,
            "context": context,
            "path": publish_path,
            "name": name,
            "version_number": version,
        }
        
        #registering publish
        sg_data = tank.util.register_publish(**args)

    def _version_playblast(self, name, shotName, taskName, projectName, comment, publish_path):
        """
        create a new version and upload it to shotgun. 
        """
        verData= {
                "code": name,
                "entity": shotName,
                "sg_task": taskName,
                "project": projectName,
                "description": comment,
                "sg_path_to_movie": publish_path,
        }
        sg_version = self._app.tank.shotgun.create("Version", verData)
        self._app.tank.shotgun.upload("Version", sg_version["id"], publish_path, "sg_uploaded_movie")

from . import resources_rc
