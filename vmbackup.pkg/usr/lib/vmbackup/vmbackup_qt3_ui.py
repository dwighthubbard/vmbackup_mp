# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vmbackup_qt3.ui'
#
# Created: Sat May 3 02:57:50 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.4
#
# WARNING! All changes made in this file will be lost!


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

class vmbackup(QWizard):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QWizard.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        if not name:
            self.setName("vmbackup")

        self.setModal(1)


        self.WizardIntrocution = QWidget(self,"WizardIntrocution")
        WizardIntrocutionLayout = QHBoxLayout(self.WizardIntrocution,11,6,"WizardIntrocutionLayout")

        self.textBrowser1 = QTextBrowser(self.WizardIntrocution,"textBrowser1")
        self.textBrowser1.setPaletteBackgroundColor(QColor(238,239,242))
        self.textBrowser1.setFrameShape(QTextBrowser.NoFrame)
        self.textBrowser1.setTabStopWidth(4)
        WizardIntrocutionLayout.addWidget(self.textBrowser1)
        self.addPage(self.WizardIntrocution,QString(""))

        self.pageSelectVM = QWidget(self,"pageSelectVM")
        pageSelectVMLayout = QVBoxLayout(self.pageSelectVM,11,6,"pageSelectVMLayout")

        self.frame3 = QFrame(self.pageSelectVM,"frame3")
        self.frame3.setPaletteBackgroundColor(QColor(255,255,255))
        self.frame3.setFrameShape(QFrame.NoFrame)
        self.frame3.setFrameShadow(QFrame.Sunken)
        self.frame3.setLineWidth(2)
        frame3Layout = QVBoxLayout(self.frame3,0,0,"frame3Layout")

        self.listVMs = QListBox(self.frame3,"listVMs")
        self.listVMs.setPaletteBackgroundColor(QColor(238,239,242))
        frame3Layout.addWidget(self.listVMs)
        pageSelectVMLayout.addWidget(self.frame3)
        self.addPage(self.pageSelectVM,QString(""))

        self.WizardBackupType = QWidget(self,"WizardBackupType")
        WizardBackupTypeLayout = QVBoxLayout(self.WizardBackupType,11,6,"WizardBackupTypeLayout")

        self.buttonGroup1 = QButtonGroup(self.WizardBackupType,"buttonGroup1")
        self.buttonGroup1.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1.layout().setSpacing(6)
        self.buttonGroup1.layout().setMargin(11)
        buttonGroup1Layout = QVBoxLayout(self.buttonGroup1.layout())
        buttonGroup1Layout.setAlignment(Qt.AlignTop)

        self.radioBackupHot = QRadioButton(self.buttonGroup1,"radioBackupHot")
        buttonGroup1Layout.addWidget(self.radioBackupHot)

        self.textLabel1_2 = QLabel(self.buttonGroup1,"textLabel1_2")
        self.textLabel1_2.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)
        buttonGroup1Layout.addWidget(self.textLabel1_2)
        spacer5 = QSpacerItem(20,17,QSizePolicy.Minimum,QSizePolicy.Expanding)
        buttonGroup1Layout.addItem(spacer5)

        self.radioBackupLVM = QRadioButton(self.buttonGroup1,"radioBackupLVM")
        buttonGroup1Layout.addWidget(self.radioBackupLVM)

        self.textLabel2 = QLabel(self.buttonGroup1,"textLabel2")
        self.textLabel2.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)
        buttonGroup1Layout.addWidget(self.textLabel2)
        spacer6 = QSpacerItem(20,17,QSizePolicy.Minimum,QSizePolicy.Expanding)
        buttonGroup1Layout.addItem(spacer6)

        self.radioBackupCold = QRadioButton(self.buttonGroup1,"radioBackupCold")
        self.radioBackupCold.setChecked(1)
        buttonGroup1Layout.addWidget(self.radioBackupCold)

        self.textLabel3 = QLabel(self.buttonGroup1,"textLabel3")
        self.textLabel3.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)
        buttonGroup1Layout.addWidget(self.textLabel3)
        WizardBackupTypeLayout.addWidget(self.buttonGroup1)
        self.addPage(self.WizardBackupType,QString(""))

        self.BackupType = QWidget(self,"BackupType")
        BackupTypeLayout = QVBoxLayout(self.BackupType,11,6,"BackupTypeLayout")

        self.buttonGroup3 = QButtonGroup(self.BackupType,"buttonGroup3")
        self.buttonGroup3.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup3.layout().setSpacing(6)
        self.buttonGroup3.layout().setMargin(11)
        buttonGroup3Layout = QVBoxLayout(self.buttonGroup3.layout())
        buttonGroup3Layout.setAlignment(Qt.AlignTop)

        self.radioTAR = QRadioButton(self.buttonGroup3,"radioTAR")
        buttonGroup3Layout.addWidget(self.radioTAR)
        spacer12_2 = QSpacerItem(20,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        buttonGroup3Layout.addItem(spacer12_2)

        self.radioTGZ = QRadioButton(self.buttonGroup3,"radioTGZ")
        self.radioTGZ.setChecked(1)
        buttonGroup3Layout.addWidget(self.radioTGZ)
        spacer13 = QSpacerItem(20,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        buttonGroup3Layout.addItem(spacer13)

        self.radioTBZ2 = QRadioButton(self.buttonGroup3,"radioTBZ2")
        buttonGroup3Layout.addWidget(self.radioTBZ2)
        spacer14_2 = QSpacerItem(20,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        buttonGroup3Layout.addItem(spacer14_2)

        self.radioZip = QRadioButton(self.buttonGroup3,"radioZip")
        self.radioZip.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Maximum,0,0,self.radioZip.sizePolicy().hasHeightForWidth()))
        buttonGroup3Layout.addWidget(self.radioZip)
        spacer15 = QSpacerItem(20,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        buttonGroup3Layout.addItem(spacer15)

        self.radioDir = QRadioButton(self.buttonGroup3,"radioDir")
        self.radioDir.setSizePolicy(QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed,0,0,self.radioDir.sizePolicy().hasHeightForWidth()))
        buttonGroup3Layout.addWidget(self.radioDir)
        spacer11 = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        buttonGroup3Layout.addItem(spacer11)

        self.radioISO = QRadioButton(self.buttonGroup3,"radioISO")
        buttonGroup3Layout.addWidget(self.radioISO)
        BackupTypeLayout.addWidget(self.buttonGroup3)
        self.addPage(self.BackupType,QString(""))

        self.WizardPageDestination = QWidget(self,"WizardPageDestination")
        WizardPageDestinationLayout = QVBoxLayout(self.WizardPageDestination,11,6,"WizardPageDestinationLayout")

        self.buttonGroup2 = QButtonGroup(self.WizardPageDestination,"buttonGroup2")
        self.buttonGroup2.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Minimum,0,0,self.buttonGroup2.sizePolicy().hasHeightForWidth()))
        self.buttonGroup2.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup2.layout().setSpacing(6)
        self.buttonGroup2.layout().setMargin(11)
        buttonGroup2Layout = QGridLayout(self.buttonGroup2.layout())
        buttonGroup2Layout.setAlignment(Qt.AlignTop)

        self.radioLocalComputer = QRadioButton(self.buttonGroup2,"radioLocalComputer")
        self.radioLocalComputer.setChecked(1)

        buttonGroup2Layout.addMultiCellWidget(self.radioLocalComputer,0,0,0,2)

        self.radioRemoteComputer = QRadioButton(self.buttonGroup2,"radioRemoteComputer")

        buttonGroup2Layout.addMultiCellWidget(self.radioRemoteComputer,1,1,0,2)

        self.textLabel1_3 = QLabel(self.buttonGroup2,"textLabel1_3")

        buttonGroup2Layout.addWidget(self.textLabel1_3,3,1)

        self.textLabel2_2 = QLabel(self.buttonGroup2,"textLabel2_2")

        buttonGroup2Layout.addWidget(self.textLabel2_2,2,1)

        self.lineRemoteComputer = QLineEdit(self.buttonGroup2,"lineRemoteComputer")
        self.lineRemoteComputer.setEnabled(0)

        buttonGroup2Layout.addWidget(self.lineRemoteComputer,3,2)

        self.lineRemoteUser = QLineEdit(self.buttonGroup2,"lineRemoteUser")
        self.lineRemoteUser.setEnabled(0)

        buttonGroup2Layout.addWidget(self.lineRemoteUser,2,2)
        spacer8 = QSpacerItem(40,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        buttonGroup2Layout.addItem(spacer8,2,0)
        spacer9 = QSpacerItem(40,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        buttonGroup2Layout.addItem(spacer9,3,0)
        WizardPageDestinationLayout.addWidget(self.buttonGroup2)

        self.groupBox2 = QGroupBox(self.WizardPageDestination,"groupBox2")
        self.groupBox2.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Minimum,0,0,self.groupBox2.sizePolicy().hasHeightForWidth()))
        self.groupBox2.setColumnLayout(0,Qt.Vertical)
        self.groupBox2.layout().setSpacing(6)
        self.groupBox2.layout().setMargin(11)
        groupBox2Layout = QHBoxLayout(self.groupBox2.layout())
        groupBox2Layout.setAlignment(Qt.AlignTop)

        self.lineDestination = QLineEdit(self.groupBox2,"lineDestination")
        groupBox2Layout.addWidget(self.lineDestination)

        self.pushDestinationDirectory = QPushButton(self.groupBox2,"pushDestinationDirectory")
        self.pushDestinationDirectory.setPixmap(self.image0)
        groupBox2Layout.addWidget(self.pushDestinationDirectory)
        WizardPageDestinationLayout.addWidget(self.groupBox2)
        spacer10 = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
        WizardPageDestinationLayout.addItem(spacer10)
        self.addPage(self.WizardPageDestination,QString(""))

        self.WizardSummary = QWidget(self,"WizardSummary")
        WizardSummaryLayout = QVBoxLayout(self.WizardSummary,11,6,"WizardSummaryLayout")

        self.frame7 = QFrame(self.WizardSummary,"frame7")
        self.frame7.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding,0,0,self.frame7.sizePolicy().hasHeightForWidth()))
        self.frame7.setFrameShape(QFrame.StyledPanel)
        self.frame7.setFrameShadow(QFrame.Sunken)
        self.frame7.setLineWidth(0)
        frame7Layout = QVBoxLayout(self.frame7,0,0,"frame7Layout")

        self.textLabel8 = QLabel(self.frame7,"textLabel8")
        frame7Layout.addWidget(self.textLabel8)
        spacer14 = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
        frame7Layout.addItem(spacer14)

        self.frame6 = QFrame(self.frame7,"frame6")
        self.frame6.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.frame6.sizePolicy().hasHeightForWidth()))
        self.frame6.setFrameShape(QFrame.NoFrame)
        self.frame6.setFrameShadow(QFrame.Raised)
        frame6Layout = QHBoxLayout(self.frame6,11,6,"frame6Layout")
        spacer1 = QSpacerItem(40,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        frame6Layout.addItem(spacer1)

        self.textLabel1 = QLabel(self.frame6,"textLabel1")
        self.textLabel1.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum,0,0,self.textLabel1.sizePolicy().hasHeightForWidth()))
        frame6Layout.addWidget(self.textLabel1)

        self.textSummarySource = QLabel(self.frame6,"textSummarySource")
        self.textSummarySource.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.textSummarySource.sizePolicy().hasHeightForWidth()))
        self.textSummarySource.setScaledContents(0)
        self.textSummarySource.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter | QLabel.AlignRight)
        frame6Layout.addWidget(self.textSummarySource)
        frame7Layout.addWidget(self.frame6)

        self.frame7_2 = QFrame(self.frame7,"frame7_2")
        self.frame7_2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.frame7_2.sizePolicy().hasHeightForWidth()))
        self.frame7_2.setFrameShape(QFrame.NoFrame)
        self.frame7_2.setFrameShadow(QFrame.Raised)
        frame7_2Layout = QHBoxLayout(self.frame7_2,11,6,"frame7_2Layout")
        spacer2 = QSpacerItem(40,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        frame7_2Layout.addItem(spacer2)

        self.textLabel3_2 = QLabel(self.frame7_2,"textLabel3_2")
        frame7_2Layout.addWidget(self.textLabel3_2)

        self.textSummaryBackupMethod = QLabel(self.frame7_2,"textSummaryBackupMethod")
        self.textSummaryBackupMethod.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.textSummaryBackupMethod.sizePolicy().hasHeightForWidth()))
        self.textSummaryBackupMethod.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        frame7_2Layout.addWidget(self.textSummaryBackupMethod)
        frame7Layout.addWidget(self.frame7_2)

        self.frame8 = QFrame(self.frame7,"frame8")
        self.frame8.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.frame8.sizePolicy().hasHeightForWidth()))
        self.frame8.setFrameShape(QFrame.NoFrame)
        self.frame8.setFrameShadow(QFrame.Raised)
        frame8Layout = QHBoxLayout(self.frame8,11,6,"frame8Layout")
        spacer12 = QSpacerItem(40,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        frame8Layout.addItem(spacer12)

        self.textLabel5_2 = QLabel(self.frame8,"textLabel5_2")
        self.textLabel5_2.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum,0,0,self.textLabel5_2.sizePolicy().hasHeightForWidth()))
        frame8Layout.addWidget(self.textLabel5_2)

        self.textSummaryBackupFormat = QLabel(self.frame8,"textSummaryBackupFormat")
        self.textSummaryBackupFormat.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.textSummaryBackupFormat.sizePolicy().hasHeightForWidth()))
        self.textSummaryBackupFormat.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        frame8Layout.addWidget(self.textSummaryBackupFormat)
        frame7Layout.addWidget(self.frame8)

        self.frame9_2 = QFrame(self.frame7,"frame9_2")
        self.frame9_2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.frame9_2.sizePolicy().hasHeightForWidth()))
        self.frame9_2.setFrameShape(QFrame.NoFrame)
        self.frame9_2.setFrameShadow(QFrame.Raised)
        frame9_2Layout = QHBoxLayout(self.frame9_2,11,6,"frame9_2Layout")
        spacer3 = QSpacerItem(40,20,QSizePolicy.Minimum,QSizePolicy.Minimum)
        frame9_2Layout.addItem(spacer3)

        self.textLabel5 = QLabel(self.frame9_2,"textLabel5")
        self.textLabel5.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Minimum,0,0,self.textLabel5.sizePolicy().hasHeightForWidth()))
        frame9_2Layout.addWidget(self.textLabel5)

        self.textSelectDestDir = QLabel(self.frame9_2,"textSelectDestDir")
        self.textSelectDestDir.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Minimum,0,0,self.textSelectDestDir.sizePolicy().hasHeightForWidth()))
        self.textSelectDestDir.setScaledContents(0)
        self.textSelectDestDir.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter | QLabel.AlignRight)
        frame9_2Layout.addWidget(self.textSelectDestDir)
        frame7Layout.addWidget(self.frame9_2)
        WizardSummaryLayout.addWidget(self.frame7)
        self.addPage(self.WizardSummary,QString(""))

        self.languageChange()

        self.resize(QSize(633,427).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushDestinationDirectory,SIGNAL("clicked()"),self.pushDestinationDirectory_clicked)
        self.connect(self.radioRemoteComputer,SIGNAL("clicked()"),self.radioRemoteComputer_clicked)
        self.connect(self.radioLocalComputer,SIGNAL("clicked()"),self.radioLocalComputer_clicked)
        self.connect(self,SIGNAL("selected(const QString&)"),self.vmbackup_selected)

        self.setTabOrder(self.radioTGZ,self.radioLocalComputer)
        self.setTabOrder(self.radioLocalComputer,self.lineRemoteUser)
        self.setTabOrder(self.lineRemoteUser,self.lineRemoteComputer)
        self.setTabOrder(self.lineRemoteComputer,self.lineDestination)
        self.setTabOrder(self.lineDestination,self.pushDestinationDirectory)
        self.setTabOrder(self.pushDestinationDirectory,self.radioBackupCold)
        self.setTabOrder(self.radioBackupCold,self.radioBackupLVM)
        self.setTabOrder(self.radioBackupLVM,self.radioBackupHot)
        self.setTabOrder(self.radioBackupHot,self.radioRemoteComputer)
        self.setTabOrder(self.radioRemoteComputer,self.textBrowser1)
        self.setTabOrder(self.textBrowser1,self.listVMs)


    def languageChange(self):
        self.setCaption(self.__tr("VMBackup"))
        self.textBrowser1.setText(self.__tr("<b>Virtual Machine Backup Wizard</b>\n"
"<br><br>\n"
"This wizard helps you to backup a single VMware Server 1.0x, VMware GSX, VMware Server 2.0 or VMware Workstation virtual machine. \n"
"<br><br>\n"
"To continue, click Next."))
        self.setTitle(self.WizardIntrocution,self.__tr("Introduction"))
        self.setTitle(self.pageSelectVM,self.__tr("Select Virtual Machine to Backup"))
        self.buttonGroup1.setTitle(QString.null)
        self.radioBackupHot.setText(self.__tr("Hot Backup using VMware Snapshots"))
        self.textLabel1_2.setText(self.__tr("This option allows backing up the virtual machine while it is running.  However, this option doesn't work under VMware GSX or VMware Server 1.0.x"))
        self.radioBackupLVM.setText(self.__tr("Hot Backup using LVM Snapshots"))
        self.textLabel2.setText(self.__tr("This option allows backing up the virtual machine while it is running.  However, it does require the virtual machine be stored on a LVM volume with at least 4GB of unallocated space."))
        self.radioBackupCold.setText(self.__tr("Cold Backup"))
        self.textLabel3.setText(self.__tr("This option suspends operation of the virtual machine, performs a backup and resumes the virtual machine's operation where it left off.  This option does not work on VMware Server 2.0 Beta 2."))
        self.setTitle(self.WizardBackupType,self.__tr("Backup Method"))
        self.buttonGroup3.setTitle(QString.null)
        self.radioTAR.setText(self.__tr("Uncompressed Tar file - Generates an uncompress tar file (.tar)"))
        self.radioTGZ.setText(self.__tr("GZipped Tar File - Generates a gzipped tar file (.tar.gz)"))
        self.radioTBZ2.setText(self.__tr("BZip2 Tar File - Generates a bzip2 tar file (.tar.bz2)"))
        self.radioZip.setText(self.__tr("Zip File - This generates a zip file (.zip)"))
        self.radioDir.setText(self.__tr("Directory - Copy the Virtual Machine directory to another directory"))
        self.radioISO.setText(self.__tr("ISO File - Generates an ISO format file for burning to CD/DVD"))
        self.setTitle(self.BackupType,self.__tr("Backup Type"))
        self.buttonGroup2.setTitle(self.__tr("Destination Computer"))
        self.radioLocalComputer.setText(self.__tr("Local Computer"))
        self.radioRemoteComputer.setText(self.__tr("Remote Computer"))
        self.textLabel1_3.setText(self.__tr("Hostname"))
        self.textLabel2_2.setText(self.__tr("UserName"))
        self.groupBox2.setTitle(self.__tr("Destination Directory"))
        self.pushDestinationDirectory.setText(QString.null)
        self.setTitle(self.WizardPageDestination,self.__tr("Select the Destination"))
        self.textLabel8.setText(self.__tr("You have completed the steps required to create a Virtual Machine backup.\n"
"\n"
"You're backup is defined below:"))
        self.textLabel1.setText(self.__tr("Source"))
        self.textSummarySource.setText(QString.null)
        self.textLabel3_2.setText(self.__tr("Backup Method"))
        self.textSummaryBackupMethod.setText(QString.null)
        self.textLabel5_2.setText(self.__tr("Backup Format"))
        self.textSummaryBackupFormat.setText(QString.null)
        self.textLabel5.setText(self.__tr("Destination"))
        self.textSelectDestDir.setText(QString.null)
        self.setTitle(self.WizardSummary,self.__tr("Summary"))


    def pushDestinationDirectory_clicked(self):
            print 'test'
        

    def radioRemoteComputer_clicked(self):
            print 'radioRemoteComputer_clicked()'
        

    def radioLocalComputer_clicked(self):
            print 'radioLocalComputer_clicked()'
        

    def vmbackup_selected(self,a0):
            print 'vmbackup_selected',a0
        

    def __tr(self,s,c = None):
        return qApp.translate("vmbackup",s,c)
