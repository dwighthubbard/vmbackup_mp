# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vmbackupprogress_qt3.ui'
#
# Created: Mon May 5 23:48:15 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.3
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *


class VMBackupProgress(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("VMBackupProgress")


        VMBackupProgressLayout = QVBoxLayout(self,11,6,"VMBackupProgressLayout")

        self.frame3 = QFrame(self,"frame3")
        self.frame3.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum,0,0,self.frame3.sizePolicy().hasHeightForWidth()))
        self.frame3.setPaletteBackgroundColor(QColor(0,255,255))
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Sunken)
        frame3Layout = QHBoxLayout(self.frame3,11,6,"frame3Layout")

        self.textLabelCaption = QLabel(self.frame3,"textLabelCaption")
        self.textLabelCaption.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Minimum,0,0,self.textLabelCaption.sizePolicy().hasHeightForWidth()))
        frame3Layout.addWidget(self.textLabelCaption)
        VMBackupProgressLayout.addWidget(self.frame3)

        self.textLabelStatus = QLabel(self,"textLabelStatus")
        self.textLabelStatus.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.textLabelStatus.sizePolicy().hasHeightForWidth()))
        self.textLabelStatus.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)
        VMBackupProgressLayout.addWidget(self.textLabelStatus)

        self.progressBarStatus = QProgressBar(self,"progressBarStatus")
        VMBackupProgressLayout.addWidget(self.progressBarStatus)

        self.frame4 = QFrame(self,"frame4")
        self.frame4.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum,0,0,self.frame4.sizePolicy().hasHeightForWidth()))
        self.frame4.setFrameShape(QFrame.NoFrame)
        self.frame4.setFrameShadow(QFrame.Raised)
        frame4Layout = QHBoxLayout(self.frame4,0,0,"frame4Layout")

        self.pushButtonCancel = QPushButton(self.frame4,"pushButtonCancel")
        self.pushButtonCancel.setSizePolicy(QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed,0,0,self.pushButtonCancel.sizePolicy().hasHeightForWidth()))
        frame4Layout.addWidget(self.pushButtonCancel)
        VMBackupProgressLayout.addWidget(self.frame4)

        self.languageChange()

        self.resize(QSize(377,181).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButtonCancel,SIGNAL("clicked()"),self.pushButtonCancel_clicked)


    def languageChange(self):
        self.setCaption(self.__tr("VMBackup Progress"))
        self.textLabelCaption.setText(self.__tr("<b>VMBackup Status</b>"))
        self.textLabelStatus.setText(self.__tr("textLabel2"))
        self.pushButtonCancel.setText(self.__tr("Cancel"))


    def pushButtonCancel_clicked(self):
            sys.exit(0)
        

    def __tr(self,s,c = None):
        return qApp.translate("VMBackupProgress",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = VMBackupProgress()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
