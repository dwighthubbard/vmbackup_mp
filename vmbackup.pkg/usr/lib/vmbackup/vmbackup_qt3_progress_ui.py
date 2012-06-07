# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vmbackup_qt3_progress.ui'
#
# Created: Wed Apr 23 00:11:26 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.3
#
# WARNING! All changes made in this file will be lost!


from qt import *


class BackupStatus(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("BackupStatus")

        self.setModal(0)

        BackupStatusLayout = QVBoxLayout(self,0,0,"BackupStatusLayout")

        self.frame8 = QFrame(self,"frame8")
        self.frame8.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Minimum,0,0,self.frame8.sizePolicy().hasHeightForWidth()))
        self.frame8.setPaletteBackgroundColor(QColor(85,170,127))
        self.frame8.setFrameShape(QFrame.NoFrame)
        self.frame8.setFrameShadow(QFrame.Raised)
        frame8Layout = QVBoxLayout(self.frame8,11,0,"frame8Layout")

        self.textLabel1 = QLabel(self.frame8,"textLabel1")
        self.textLabel1.setPaletteForegroundColor(QColor(255,255,255))
        textLabel1_font = QFont(self.textLabel1.font())
        textLabel1_font.setPointSize(14)
        textLabel1_font.setBold(1)
        self.textLabel1.setFont(textLabel1_font)
        self.textLabel1.setScaledContents(1)
        frame8Layout.addWidget(self.textLabel1)
        BackupStatusLayout.addWidget(self.frame8)

        self.groupBox2 = QGroupBox(self,"groupBox2")
        self.groupBox2.setColumnLayout(0,Qt.Vertical)
        self.groupBox2.layout().setSpacing(6)
        self.groupBox2.layout().setMargin(11)
        groupBox2Layout = QVBoxLayout(self.groupBox2.layout())
        groupBox2Layout.setAlignment(Qt.AlignTop)

        self.textMessages = QTextEdit(self.groupBox2,"textMessages")
        self.textMessages.setWrapPolicy(QTextEdit.Anywhere)
        self.textMessages.setReadOnly(1)
        self.textMessages.setTabStopWidth(8)
        groupBox2Layout.addWidget(self.textMessages)
        BackupStatusLayout.addWidget(self.groupBox2)

        self.frame10 = QFrame(self,"frame10")
        self.frame10.setFrameShape(QFrame.NoFrame)
        self.frame10.setFrameShadow(QFrame.Raised)
        frame10Layout = QHBoxLayout(self.frame10,11,6,"frame10Layout")
        spacer15 = QSpacerItem(40,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        frame10Layout.addItem(spacer15)

        self.pushButton5 = QPushButton(self.frame10,"pushButton5")
        frame10Layout.addWidget(self.pushButton5)
        BackupStatusLayout.addWidget(self.frame10)

        self.languageChange()

        self.resize(QSize(515,235).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Backup Progress"))
        self.textLabel1.setText(self.__tr("Virtual Machine Backup"))
        self.groupBox2.setTitle(self.__tr("Messages"))
        self.pushButton5.setText(self.__tr("Abort"))


    def __tr(self,s,c = None):
        return qApp.translate("BackupStatus",s,c)
