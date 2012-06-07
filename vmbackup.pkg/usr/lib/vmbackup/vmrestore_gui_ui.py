# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vmrestore.gui.ui'
#
# Created: Sun May 4 22:44:26 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.4
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x10\x00\x00\x00\x10" \
    "\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\x00\x00\x02" \
    "\xf9\x49\x44\x41\x54\x38\x8d\xa5\x90\x4b\x6b\x9c" \
    "\x65\x00\x46\xcf\xfb\x7d\xef\x5c\x92\x49\xa6\x89" \
    "\x49\x1a\x53\x42\x9a\xd2\x06\x9a\x26\x25\x48\xab" \
    "\xb4\x16\x83\x25\x18\x5c\x04\x51\x10\x5c\xa9\x54" \
    "\x97\x5d\x08\xee\x54\xe8\xa2\x2a\x28\xfe\x04\x41" \
    "\xc1\x85\xa0\xfe\x03\x41\x2a\x41\xda\x22\x8d\x34" \
    "\x31\x69\xab\x4d\x49\x32\x93\x4c\x32\xb9\xcd\x25" \
    "\x33\xdf\xe5\xbd\xba\x28\xb8\x73\xe5\xb3\x3f\x87" \
    "\xc3\x23\xbc\xf7\xfc\x9f\x89\xd3\xef\xac\x70\xe5" \
    "\x62\x3f\xed\xd8\x63\x3d\xdc\xbe\x5b\xe5\xca\x60" \
    "\x83\xe1\xa2\x21\x4d\x21\x56\xb6\xa7\xd0\x99\xb9" \
    "\xd9\x99\xcf\xcc\x6d\x6e\x35\x2f\x7b\xa8\x36\x63" \
    "\x90\x01\xcc\x2f\x69\xe4\x7f\x99\x9d\xf7\xc4\xb1" \
    "\x9e\x1e\x3b\xdd\xff\xc5\xdc\xab\x67\x2e\x17\x8b" \
    "\x39\x6e\x7c\xfe\xdb\x8d\xfd\xc3\xe8\xfa\xcf\x0b" \
    "\x02\x52\x20\x74\x48\xe7\xdc\x37\x4a\xfb\x9c\xd6" \
    "\x4f\x0b\xb4\x72\x6d\x6b\xdd\x87\xa1\x08\xaf\xcf" \
    "\xce\x8c\x7e\x3c\x7b\x75\xa4\xd8\x91\x0f\x51\xca" \
    "\x71\x75\x7a\xf4\xed\xef\x7f\x5a\xfe\x41\xca\x60" \
    "\xde\x38\x01\x80\x3c\x3b\xd6\x7d\xed\xda\xbb\xfd" \
    "\x1c\x34\xa1\x6d\x60\xe2\x6c\x8e\xf4\xe1\xc6\xdc" \
    "\x7b\x6f\x8c\x0c\x4d\x8c\xf7\x12\x45\xd0\x6a\x59" \
    "\x70\x30\xf3\xd2\x70\xf7\xfc\xef\x3b\x5f\xda\xc5" \
    "\xfd\xb7\x20\x2c\x01\x04\xd9\x0c\xad\xde\x9e\x80" \
    "\x8e\x3c\xa8\x8d\x3a\x13\xbe\xc6\xcd\x0f\x26\x87" \
    "\xce\x4f\xf4\xa2\x35\x18\x03\x41\x00\xd6\x59\x76" \
    "\xeb\x86\xc9\x73\xfd\x97\x86\x8e\xdb\xd7\x49\x4c" \
    "\x1f\xce\xf7\x49\x63\xc1\x79\xd8\xb9\xbf\xcf\x54" \
    "\xb7\xe1\xc5\x37\x4f\xfd\xfb\x43\x2e\x07\x59\x01" \
    "\x2e\x1f\xf2\xd1\xd7\x65\x96\xd6\x0c\x27\x06\x0b" \
    "\x8c\x4e\x9d\xf9\x74\x60\x4c\xbc\xf6\xd7\xd2\xb6" \
    "\x95\xce\x42\x18\x40\x92\xeb\xe0\xc7\x7b\xfb\xfc" \
    "\x51\x6b\xa2\x53\x8d\xb1\x16\xab\x01\xeb\x59\x7e" \
    "\xdc\x60\xad\x1e\x32\x72\xfe\x24\x95\x24\x43\xef" \
    "\xc5\xe1\xe2\xfe\x9d\xea\xcb\xa6\xbd\xb5\x20\xad" \
    "\x77\x48\x01\xbf\x2e\x46\x0c\xf8\x0c\x03\x3d\x19" \
    "\x92\x30\x47\x3d\x76\x34\x8e\x1c\xb5\x96\xa7\x30" \
    "\xd2\xc5\xe4\x78\x81\xa5\x12\xc4\xb1\xa3\xb6\x5a" \
    "\x73\xe5\x5b\x2b\x01\x2e\xf9\x45\x3a\xeb\xa9\xb7" \
    "\xa0\x5a\x6a\xf1\xd5\x27\xa7\x88\x52\x43\x66\x30" \
    "\xc3\x72\x59\x70\xf8\xb7\x67\xb7\xea\x29\xef\x78" \
    "\xf6\xb6\x13\x6a\x9b\x07\x34\x1e\x57\x48\xb7\x9a" \
    "\x15\x32\xaa\x93\x9c\xbb\x27\xa5\x14\xdc\x5e\x88" \
    "\x19\x3f\xd9\x45\xae\x2f\xe0\xee\x43\x38\x58\x77" \
    "\xac\x6f\x87\x3c\x79\xe2\xd8\x2c\x25\x54\xb6\x14" \
    "\xf5\x8d\x03\xd4\x61\x0d\xe2\xd8\x83\x70\x04\xba" \
    "\x84\xb7\x0f\x02\x04\xdc\x5f\x3c\x64\xfa\x42\x07" \
    "\x8f\x6a\x50\x8e\xb3\xac\xac\x3b\x6a\x0d\x87\x36" \
    "\x8e\x44\x79\x9a\x07\x31\x2a\x05\xb2\x1d\x20\xf3" \
    "\x20\x6c\x0f\xe8\x15\x2c\xab\x72\xa3\x94\x32\x3e" \
    "\x96\x65\xe8\x78\x9e\x63\xc0\xb9\x22\x3c\x33\x1c" \
    "\xd2\x38\xd4\x9c\x08\x0d\xbd\x69\xc4\xb3\xa1\x45" \
    "\xc7\x60\xdb\x86\xb4\x6d\xc4\x66\xd9\x75\xed\x55" \
    "\xec\x9f\x08\x61\xe4\xda\xea\x11\x33\x17\x8e\x31" \
    "\x3b\x96\x05\x01\xf4\x40\x32\x04\x51\x04\x51\xdb" \
    "\x91\x5e\x92\x44\xb1\xa3\xd5\xf6\x44\xed\x2e\x94" \
    "\xca\xf3\xd9\xb7\x71\xbc\x57\x72\x0b\x84\x02\xa9" \
    "\x5b\x29\xaf\x4c\x15\x9e\xc2\x00\x02\xf2\x85\x80" \
    "\x30\x94\x78\xa7\x51\xca\x62\x8d\x46\xa9\x18\xa5" \
    "\x12\xda\x89\xe6\xc1\xa3\xa3\x0a\xde\xdd\x81\x00" \
    "\x21\x9f\xbb\x55\x7b\xfe\x85\xfe\xae\x42\x2e\xc0" \
    "\x5a\xc0\x59\xb4\x71\xe8\x44\xa1\x52\x85\x4a\x53" \
    "\x54\xa2\x31\xa9\xc2\x28\x43\x9a\x1a\x76\xd7\xcc" \
    "\x77\x18\xde\x47\xc0\x3f\x86\xcc\xa2\x5b\x1a\xec" \
    "\xc3\x70\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42" \
    "\x60\x82"

class VMRestore(QWizard):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QWizard.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        if not name:
            self.setName("VMRestore")



        self.WizardPageSource = QWidget(self,"WizardPageSource")
        WizardPageSourceLayout = QVBoxLayout(self.WizardPageSource,11,6,"WizardPageSourceLayout")

        self.groupBox1 = QGroupBox(self.WizardPageSource,"groupBox1")
        self.groupBox1.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Minimum,0,0,self.groupBox1.sizePolicy().hasHeightForWidth()))
        self.groupBox1.setColumnLayout(0,Qt.Vertical)
        self.groupBox1.layout().setSpacing(6)
        self.groupBox1.layout().setMargin(11)
        groupBox1Layout = QHBoxLayout(self.groupBox1.layout())
        groupBox1Layout.setAlignment(Qt.AlignTop)

        self.lineEditSource = QLineEdit(self.groupBox1,"lineEditSource")
        groupBox1Layout.addWidget(self.lineEditSource)

        self.pushButtonSource = QPushButton(self.groupBox1,"pushButtonSource")
        self.pushButtonSource.setPixmap(self.image0)
        groupBox1Layout.addWidget(self.pushButtonSource)
        WizardPageSourceLayout.addWidget(self.groupBox1)
        spacer9 = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
        WizardPageSourceLayout.addItem(spacer9)

        self.textLabel3 = QLabel(self.WizardPageSource,"textLabel3")
        self.textLabel3.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Minimum,0,0,self.textLabel3.sizePolicy().hasHeightForWidth()))
        WizardPageSourceLayout.addWidget(self.textLabel3)
        self.addPage(self.WizardPageSource,QString(""))

        self.WizardPageDest = QWidget(self,"WizardPageDest")
        WizardPageDestLayout = QVBoxLayout(self.WizardPageDest,11,6,"WizardPageDestLayout")

        self.textLabel1_2 = QLabel(self.WizardPageDest,"textLabel1_2")
        self.textLabel1_2.setSizePolicy(QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Preferred,0,0,self.textLabel1_2.sizePolicy().hasHeightForWidth()))
        WizardPageDestLayout.addWidget(self.textLabel1_2)
        spacer6 = QSpacerItem(20,30,QSizePolicy.Minimum,QSizePolicy.Expanding)
        WizardPageDestLayout.addItem(spacer6)

        self.buttonGroup1 = QButtonGroup(self.WizardPageDest,"buttonGroup1")
        self.buttonGroup1.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1.layout().setSpacing(6)
        self.buttonGroup1.layout().setMargin(11)
        buttonGroup1Layout = QVBoxLayout(self.buttonGroup1.layout())
        buttonGroup1Layout.setAlignment(Qt.AlignTop)

        self.frame4 = QFrame(self.buttonGroup1,"frame4")
        self.frame4.setFrameShape(QFrame.NoFrame)
        self.frame4.setFrameShadow(QFrame.Raised)
        frame4Layout = QHBoxLayout(self.frame4,11,6,"frame4Layout")

        self.radioButtonDestLocal = QRadioButton(self.frame4,"radioButtonDestLocal")
        self.radioButtonDestLocal.setChecked(1)
        frame4Layout.addWidget(self.radioButtonDestLocal)
        buttonGroup1Layout.addWidget(self.frame4)

        self.frame3 = QFrame(self.buttonGroup1,"frame3")
        self.frame3.setFrameShape(QFrame.NoFrame)
        self.frame3.setFrameShadow(QFrame.Raised)
        frame3Layout = QHBoxLayout(self.frame3,11,6,"frame3Layout")

        self.radioButtonDestRemote = QRadioButton(self.frame3,"radioButtonDestRemote")
        frame3Layout.addWidget(self.radioButtonDestRemote)

        self.lineEditRemoteHost = QLineEdit(self.frame3,"lineEditRemoteHost")
        frame3Layout.addWidget(self.lineEditRemoteHost)
        buttonGroup1Layout.addWidget(self.frame3)
        WizardPageDestLayout.addWidget(self.buttonGroup1)
        spacer8 = QSpacerItem(20,30,QSizePolicy.Minimum,QSizePolicy.Expanding)
        WizardPageDestLayout.addItem(spacer8)

        self.groupBox1_2 = QGroupBox(self.WizardPageDest,"groupBox1_2")
        self.groupBox1_2.setColumnLayout(0,Qt.Vertical)
        self.groupBox1_2.layout().setSpacing(6)
        self.groupBox1_2.layout().setMargin(11)
        groupBox1_2Layout = QHBoxLayout(self.groupBox1_2.layout())
        groupBox1_2Layout.setAlignment(Qt.AlignTop)

        self.lineEditDestDir = QLineEdit(self.groupBox1_2,"lineEditDestDir")
        groupBox1_2Layout.addWidget(self.lineEditDestDir)

        self.pushButtonDestDir = QPushButton(self.groupBox1_2,"pushButtonDestDir")
        self.pushButtonDestDir.setPixmap(self.image0)
        groupBox1_2Layout.addWidget(self.pushButtonDestDir)
        WizardPageDestLayout.addWidget(self.groupBox1_2)
        spacer7 = QSpacerItem(20,30,QSizePolicy.Minimum,QSizePolicy.Expanding)
        WizardPageDestLayout.addItem(spacer7)

        self.textLabel3_2 = QLabel(self.WizardPageDest,"textLabel3_2")
        WizardPageDestLayout.addWidget(self.textLabel3_2)
        self.addPage(self.WizardPageDest,QString(""))

        self.WizardPageSummary = QWidget(self,"WizardPageSummary")
        WizardPageSummaryLayout = QGridLayout(self.WizardPageSummary,1,1,11,6,"WizardPageSummaryLayout")

        self.textLabel4 = QLabel(self.WizardPageSummary,"textLabel4")

        WizardPageSummaryLayout.addMultiCellWidget(self.textLabel4,1,1,1,2)

        self.textLabel5 = QLabel(self.WizardPageSummary,"textLabel5")

        WizardPageSummaryLayout.addWidget(self.textLabel5,2,1)

        self.textLabel6 = QLabel(self.WizardPageSummary,"textLabel6")

        WizardPageSummaryLayout.addMultiCellWidget(self.textLabel6,3,3,1,2)
        spacer10 = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
        WizardPageSummaryLayout.addMultiCell(spacer10,0,0,2,3)
        spacer11 = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
        WizardPageSummaryLayout.addItem(spacer11,4,4)

        self.textLabelDestComputer = QLabel(self.WizardPageSummary,"textLabelDestComputer")
        self.textLabelDestComputer.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred,0,0,self.textLabelDestComputer.sizePolicy().hasHeightForWidth()))

        WizardPageSummaryLayout.addMultiCellWidget(self.textLabelDestComputer,2,2,3,4)

        self.textLabelDestDir = QLabel(self.WizardPageSummary,"textLabelDestDir")
        self.textLabelDestDir.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred,0,0,self.textLabelDestDir.sizePolicy().hasHeightForWidth()))

        WizardPageSummaryLayout.addMultiCellWidget(self.textLabelDestDir,3,3,3,4)
        spacer12 = QSpacerItem(40,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        WizardPageSummaryLayout.addItem(spacer12,1,0)
        spacer13 = QSpacerItem(40,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        WizardPageSummaryLayout.addItem(spacer13,2,0)
        spacer14 = QSpacerItem(40,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        WizardPageSummaryLayout.addItem(spacer14,3,0)

        self.textLabelSummarySource = QLabel(self.WizardPageSummary,"textLabelSummarySource")
        self.textLabelSummarySource.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred,0,0,self.textLabelSummarySource.sizePolicy().hasHeightForWidth()))

        WizardPageSummaryLayout.addMultiCellWidget(self.textLabelSummarySource,1,1,3,4)
        self.addPage(self.WizardPageSummary,QString(""))

        self.languageChange()

        self.resize(QSize(600,363).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButtonSource,SIGNAL("clicked()"),self.pushButtonSource_clicked)
        self.connect(self.pushButtonDestDir,SIGNAL("clicked()"),self.pushButtonDestDir_clicked)
        self.connect(self,SIGNAL("selected(const QString&)"),self.VMRestore_selected)


    def languageChange(self):
        self.setCaption(self.__tr("VMBackup Restore"))
        self.groupBox1.setTitle(self.__tr("Select VMbackup Image"))
        self.pushButtonSource.setText(QString.null)
        self.textLabel3.setText(self.__tr("To continue, click Next."))
        self.setTitle(self.WizardPageSource,self.__tr("Select what to restore"))
        self.textLabel1_2.setText(self.__tr("Please select the destination for this VM"))
        self.buttonGroup1.setTitle(self.__tr("Destination Host"))
        self.radioButtonDestLocal.setText(self.__tr("The local computer system"))
        self.radioButtonDestRemote.setText(self.__tr("Remote computer"))
        self.groupBox1_2.setTitle(self.__tr("Destination Directory"))
        self.pushButtonDestDir.setText(QString.null)
        self.textLabel3_2.setText(self.__tr("To continue, click Next."))
        self.setTitle(self.WizardPageDest,self.__tr("Select the Destination to restore to"))
        self.textLabel4.setText(self.__tr("<b>Backup Image to Restore</b>"))
        self.textLabel5.setText(self.__tr("<b>Destination Computer</b>"))
        self.textLabel6.setText(self.__tr("<b>Destination Directory</b>"))
        self.textLabelDestComputer.setText(self.__tr("Local Computer"))
        self.textLabelDestDir.setText(self.__tr("/tmp"))
        self.textLabelSummarySource.setText(self.__tr("Image"))
        self.setTitle(self.WizardPageSummary,self.__tr("Summary"))


    def pushButtonSource_clicked(self):
            pass
        

    def pushButtonDestDir_clicked(self):
            pass
        

    def VMRestore_selected(self,a0):
            pass
        

    def __tr(self,s,c = None):
        return qApp.translate("VMRestore",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = VMRestore()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
