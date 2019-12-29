# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\up1GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 729)
        MainWindow.setMinimumSize(QtCore.QSize(500, 729))
        MainWindow.setMaximumSize(QtCore.QSize(2000, 2000))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/teamwork.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("\n"
"background-color: rgb(220,220,220);")
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.SETTINGS = QtWidgets.QTabWidget(self.centralwidget)
        self.SETTINGS.setMinimumSize(QtCore.QSize(450, 450))
        self.SETTINGS.setMaximumSize(QtCore.QSize(2000, 2000))
        self.SETTINGS.setAutoFillBackground(False)
        self.SETTINGS.setIconSize(QtCore.QSize(16, 16))
        self.SETTINGS.setUsesScrollButtons(True)
        self.SETTINGS.setTabBarAutoHide(True)
        self.SETTINGS.setObjectName("SETTINGS")
        
        self.Take_Attendance = QtWidgets.QWidget()
        self.Take_Attendance.setMinimumSize(QtCore.QSize(450, 450))
        self.Take_Attendance.setMaximumSize(QtCore.QSize(2000, 2000))
        self.Take_Attendance.setObjectName("Take_Attendance")
        
        self.lcdCounter = QtWidgets.QLCDNumber(self.Take_Attendance)
        self.lcdCounter.setGeometry(QtCore.QRect(790, 440, 131, 81))
        self.lcdCounter.setStyleSheet("background-color: rgb(170, 255, 0);\n"
"")
        self.lcdCounter.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdCounter.setObjectName("lcdCounter")
        
        self.label = QtWidgets.QLabel(self.Take_Attendance)
        self.label.setGeometry(QtCore.QRect(800, 410, 111, 21))
        self.label.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setIndent(2)
        self.label.setObjectName("label")
        
        self.rawImage = QtWidgets.QLabel(self.Take_Attendance)
        self.rawImage.setGeometry(QtCore.QRect(10, 10, 721, 551))
        self.rawImage.setText("")
        self.rawImage.setPixmap(QtGui.QPixmap(":/camera/photograph.png"))
        self.rawImage.setAlignment(QtCore.Qt.AlignCenter)
        self.rawImage.setObjectName("rawImage")
        
        self.startRecognition = QtWidgets.QPushButton(self.Take_Attendance)
        self.startRecognition.setGeometry(QtCore.QRect(790, 140, 141, 61))
        self.startRecognition.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/camera/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.startRecognition.setIcon(icon1)
        self.startRecognition.setIconSize(QtCore.QSize(20, 20))
        self.startRecognition.setObjectName("startRecognition")
        
        self.progressBar_2 = QtWidgets.QProgressBar(self.Take_Attendance)
        self.progressBar_2.setGeometry(QtCore.QRect(460, 610, 501, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        
        self.PROCESSING_STATUS = QtWidgets.QLabel(self.Take_Attendance)
        self.PROCESSING_STATUS.setGeometry(QtCore.QRect(300, 610, 151, 20))
        self.PROCESSING_STATUS.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.PROCESSING_STATUS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PROCESSING_STATUS.setObjectName("PROCESSING_STATUS")
        
        self.imagePath = QtWidgets.QLineEdit(self.Take_Attendance)
        self.imagePath.setGeometry(QtCore.QRect(760, 70, 211, 20))
        self.imagePath.setAutoFillBackground(False)
        self.imagePath.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.imagePath.setAlignment(QtCore.Qt.AlignCenter)
        self.imagePath.setObjectName("imagePath")
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/camera/photograph.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.SETTINGS.addTab(self.Take_Attendance, icon2, "")
        
        self.RESULTS = QtWidgets.QWidget()
        self.RESULTS.setObjectName("RESULTS")
        
        self.treeWidget_1 = QtWidgets.QTreeWidget(self.RESULTS)
        self.treeWidget_1.setGeometry(QtCore.QRect(25, 0, 450, 550))
        self.treeWidget_1.setMinimumSize(QtCore.QSize(450, 550))
        self.treeWidget_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treeWidget_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeWidget_1.setIconSize(QtCore.QSize(120, 120))
        self.treeWidget_1.setTextElideMode(QtCore.Qt.ElideLeft)
        self.treeWidget_1.setUniformRowHeights(False)
        self.treeWidget_1.setItemsExpandable(True)
        self.treeWidget_1.setAllColumnsShowFocus(True)
        self.treeWidget_1.setObjectName("treeWidget_1")
        
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_1)
        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/persons/boy-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        item_0.setIcon(0, icon3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_1)
        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/persons/girl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        item_0.setIcon(0, icon4)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_1)
        
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/persons/man.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        item_0.setIcon(0, icon5)
        
        self.treeWidget_1.header().setVisible(False)
        self.treeWidget_1.header().setDefaultSectionSize(150)
        self.treeWidget_1.header().setHighlightSections(True)
        self.treeWidget_1.header().setMinimumSectionSize(150)
        
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.RESULTS)
        self.treeWidget_2.setGeometry(QtCore.QRect(525, 0, 450, 550))
        self.treeWidget_2.setMinimumSize(QtCore.QSize(450, 550))
        self.treeWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treeWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeWidget_2.setIconSize(QtCore.QSize(120, 120))
        self.treeWidget_2.setTextElideMode(QtCore.Qt.ElideLeft)
        self.treeWidget_2.setUniformRowHeights(False)
        self.treeWidget_2.setItemsExpandable(True)
        self.treeWidget_2.setAllColumnsShowFocus(True)
        self.treeWidget_2.setObjectName("treeWidget_2")
        
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0.setIcon(0, icon3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0.setIcon(0, icon4)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0.setIcon(0, icon5)
        
        self.treeWidget_2.header().setVisible(False)
        self.treeWidget_2.header().setDefaultSectionSize(150)
        self.treeWidget_2.header().setHighlightSections(True)
        self.treeWidget_2.header().setMinimumSectionSize(150)
        self.lcdCounter_2 = QtWidgets.QLCDNumber(self.RESULTS)
        self.lcdCounter_2.setGeometry(QtCore.QRect(410, 550, 64, 23))
        self.lcdCounter_2.setStyleSheet("color:green;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Showcard Gothic\";\n"
"")
        self.lcdCounter_2.setObjectName("lcdCounter_2")
        
        self.lcdCounter_3 = QtWidgets.QLCDNumber(self.RESULTS)
        self.lcdCounter_3.setGeometry(QtCore.QRect(910, 550, 64, 23))
        self.lcdCounter_3.setStyleSheet("color:red;background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Showcard Gothic\";\n"
"")
        self.lcdCounter_3.setObjectName("lcdCounter_3")
        
        self.update_in_excel = QtWidgets.QPushButton(self.RESULTS)
        self.update_in_excel.setGeometry(QtCore.QRect(30, 560, 111, 51))
        self.update_in_excel.setCheckable(False)
        self.update_in_excel.setObjectName("update_in_excel")
        
        self.edit_and_configure = QtWidgets.QPushButton(self.RESULTS)
        self.edit_and_configure.setGeometry(QtCore.QRect(525, 560, 111, 51))
        self.edit_and_configure.setCheckable(False)
        self.edit_and_configure.setObjectName("edit_and_configure")
        
        self.SETTINGS.addTab(self.RESULTS, "")
        
        self.Register_Faces = QtWidgets.QWidget()
        self.Register_Faces.setObjectName("Register_Faces")
        
        self.imageRecording = QtWidgets.QLabel(self.Register_Faces)
        self.imageRecording.setGeometry(QtCore.QRect(20, 10, 500, 500))
        self.imageRecording.setFrameShape(QtWidgets.QFrame.Box)
        self.imageRecording.setText("")
        self.imageRecording.setPixmap(QtGui.QPixmap(":/persons/man-1.png"))
        self.imageRecording.setScaledContents(True)
        self.imageRecording.setAlignment(QtCore.Qt.AlignCenter)
        self.imageRecording.setObjectName("imageRecording")
        
        self.progressBar = QtWidgets.QProgressBar(self.Register_Faces)
        self.progressBar.setGeometry(QtCore.QRect(50, 520, 471, 23))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 62)
        self.progressBar.setObjectName("progressBar")
        
        self.formLayoutWidget = QtWidgets.QWidget(self.Register_Faces)
        self.formLayoutWidget.setGeometry(QtCore.QRect(590, 10, 371, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(2, 2, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        self.nAMELabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nAMELabel.setObjectName("nAMELabel")
        
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nAMELabel)
        
        self.nAMELineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nAMELineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nAMELineEdit.setObjectName("nAMELineEdit")
        
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nAMELineEdit)
        
        self.rOLL_NUMBERLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rOLL_NUMBERLabel.setObjectName("rOLL_NUMBERLabel")
        
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rOLL_NUMBERLabel)
        
        self.rOLL_NUMBERLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rOLL_NUMBERLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rOLL_NUMBERLineEdit.setObjectName("rOLL_NUMBERLineEdit")
        
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rOLL_NUMBERLineEdit)
        
        self.sECTIONLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sECTIONLabel.setObjectName("sECTIONLabel")
        
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sECTIONLabel)
        
        self.sECTIONComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sECTIONComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sECTIONComboBox.setObjectName("sECTIONComboBox")
        self.sECTIONComboBox.addItem("")
        self.sECTIONComboBox.addItem("")
        self.sECTIONComboBox.addItem("")
        self.sECTIONComboBox.addItem("")
        self.sECTIONComboBox.addItem("")
        self.sECTIONComboBox.addItem("")
        
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sECTIONComboBox)
        
        self.sEMESTERLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sEMESTERLabel.setObjectName("sEMESTERLabel")
        
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sEMESTERLabel)
        
        self.sEMESTERComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sEMESTERComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sEMESTERComboBox.setObjectName("sEMESTERComboBox")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        self.sEMESTERComboBox.addItem("")
        
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sEMESTERComboBox)
        
        self.cOURSE_CODELabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.cOURSE_CODELabel.setObjectName("cOURSE_CODELabel")
        
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.cOURSE_CODELabel)
        
        self.cOURSE_CODELineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cOURSE_CODELineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cOURSE_CODELineEdit.setObjectName("cOURSE_CODELineEdit")
        
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cOURSE_CODELineEdit)
        
        self.sCHOOL_CODELabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sCHOOL_CODELabel.setObjectName("sCHOOL_CODELabel")
        
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.sCHOOL_CODELabel)
        
        self.sCHOOL_CODEComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sCHOOL_CODEComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sCHOOL_CODEComboBox.setObjectName("sCHOOL_CODEComboBox")
        self.sCHOOL_CODEComboBox.addItem("")
        self.sCHOOL_CODEComboBox.addItem("")
        self.sCHOOL_CODEComboBox.addItem("")
        self.sCHOOL_CODEComboBox.addItem("")
        
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sCHOOL_CODEComboBox)
        
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.Register_Faces)
        self.commandLinkButton.setGeometry(QtCore.QRect(640, 370, 287, 40))
        self.commandLinkButton.setAutoFillBackground(False)
        self.commandLinkButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.commandLinkButton.setObjectName("commandLinkButton")
        
        self.SETTINGS.addTab(self.Register_Faces, icon, "")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(120, 100, 681, 101))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.dATASET_SAVE_PATHLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.dATASET_SAVE_PATHLabel.setObjectName("dATASET_SAVE_PATHLabel")
        
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dATASET_SAVE_PATHLabel)
        
        self.dATASET_SAVE_PATHLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.dATASET_SAVE_PATHLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dATASET_SAVE_PATHLineEdit.setObjectName("dATASET_SAVE_PATHLineEdit")
        
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dATASET_SAVE_PATHLineEdit)
        
        self.iMAGE_PATHLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.iMAGE_PATHLabel.setObjectName("iMAGE_PATHLabel")
        
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iMAGE_PATHLabel)
        
        self.iMAGE_PATHLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.iMAGE_PATHLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.iMAGE_PATHLineEdit.setObjectName("iMAGE_PATHLineEdit")
        
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iMAGE_PATHLineEdit)
        
        self.eXCEL_SHEET_PATHLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.eXCEL_SHEET_PATHLabel.setObjectName("eXCEL_SHEET_PATHLabel")
        
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.eXCEL_SHEET_PATHLabel)
        
        self.eXCEL_SHEET_PATHLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.eXCEL_SHEET_PATHLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.eXCEL_SHEET_PATHLineEdit.setObjectName("eXCEL_SHEET_PATHLineEdit")
        
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.eXCEL_SHEET_PATHLineEdit)
        
        self.saveButton = QtWidgets.QPushButton(self.tab)
        self.saveButton.setGeometry(QtCore.QRect(390, 320, 201, 61))
        self.saveButton.setAutoFillBackground(False)
        self.saveButton.setStyleSheet("color: red;\n"
"background-color: rgba(170, 255, 255, 150);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.saveButton.setObjectName("saveButton")
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.SETTINGS.addTab(self.tab, icon6, "")
        
        self.gridLayout.addWidget(self.SETTINGS, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionoen = QtWidgets.QAction(MainWindow)
        self.actionoen.setObjectName("actionoen")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actionuct = QtWidgets.QAction(MainWindow)
        self.actionuct.setObjectName("actionuct")
        self.actioncoopy = QtWidgets.QAction(MainWindow)
        self.actioncoopy.setObjectName("actioncoopy")
        self.actionTAKE_ATTENDANCE = QtWidgets.QAction(MainWindow)
        self.actionTAKE_ATTENDANCE.setIcon(icon1)
        self.actionTAKE_ATTENDANCE.setObjectName("actionTAKE_ATTENDANCE")
        self.actionREGISTER = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/camera/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionREGISTER.setIcon(icon7)
        self.actionREGISTER.setObjectName("actionREGISTER")
        self.actionSETTINGS = QtWidgets.QAction(MainWindow)
        self.actionSETTINGS.setIcon(icon6)
        self.actionSETTINGS.setObjectName("actionSETTINGS")

        self.retranslateUi(MainWindow)
        

        self.SETTINGS.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UNIVERSITY_PROJECT-1"))
        
        self.label.setText(_translate("MainWindow", "FaceCount"))
        
        self.startRecognition.setText(_translate("MainWindow", "start"))
        self.startRecognition.setShortcut(_translate("MainWindow", "F5"))
        
        self.PROCESSING_STATUS.setText(_translate("MainWindow", "PROCESSING_STATUS :"))
        
        self.imagePath.setText(_translate("MainWindow", "Enter the Image Path"))
        
        self.SETTINGS.setTabText(self.SETTINGS.indexOf(self.Take_Attendance), _translate("MainWindow", "Take_Attendance"))
        
        self.treeWidget_1.setSortingEnabled(True)
        self.treeWidget_1.headerItem().setText(0, _translate("MainWindow", "person"))
        self.treeWidget_1.headerItem().setText(1, _translate("MainWindow", "New Column"))
        self.treeWidget_1.headerItem().setText(2, _translate("MainWindow", "name"))
        __sortingEnabled = self.treeWidget_1.isSortingEnabled()
        self.treeWidget_1.setSortingEnabled(False)
        self.treeWidget_1.topLevelItem(0).setText(1, _translate("MainWindow", "20171cse0331"))
        self.treeWidget_1.topLevelItem(0).setText(2, _translate("MainWindow", "kundanMunda"))
        self.treeWidget_1.topLevelItem(1).setText(1, _translate("MainWindow", "20171cse0332"))
        self.treeWidget_1.topLevelItem(1).setText(2, _translate("MainWindow", "sidharth Jarika"))
        self.treeWidget_1.topLevelItem(2).setText(1, _translate("MainWindow", "20171BSC0212"))
        self.treeWidget_1.topLevelItem(2).setText(2, _translate("MainWindow", "purnesh s"))
        self.treeWidget_1.setSortingEnabled(__sortingEnabled)
        
        self.treeWidget_2.setSortingEnabled(True)
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "person"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "New Column"))
        self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "name"))
        
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(1, _translate("MainWindow", "20171cse0331"))
        self.treeWidget_2.topLevelItem(0).setText(2, _translate("MainWindow", "kundanMunda"))
        self.treeWidget_2.topLevelItem(1).setText(1, _translate("MainWindow", "20171cse0332"))
        self.treeWidget_2.topLevelItem(1).setText(2, _translate("MainWindow", "sidharth Jarika"))
        self.treeWidget_2.topLevelItem(2).setText(1, _translate("MainWindow", "20171BSC0212"))
        self.treeWidget_2.topLevelItem(2).setText(2, _translate("MainWindow", "purnesh s"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        
        self.update_in_excel.setText(_translate("MainWindow", "Update_in_Excel"))
        
        self.edit_and_configure.setText(_translate("MainWindow", "EDIT and Configure"))
        
        self.SETTINGS.setTabText(self.SETTINGS.indexOf(self.RESULTS), _translate("MainWindow", "RESULTS"))
        
        self.nAMELabel.setText(_translate("MainWindow", "NAME"))
        
        self.rOLL_NUMBERLabel.setText(_translate("MainWindow", "ROLL_NUMBER"))
        
        self.sECTIONLabel.setText(_translate("MainWindow", "SECTION"))
        
        self.sECTIONComboBox.setItemText(0, _translate("MainWindow", "5cse5"))
        self.sECTIONComboBox.setItemText(1, _translate("MainWindow", "5cse6"))
        self.sECTIONComboBox.setItemText(2, _translate("MainWindow", "5cse7"))
        self.sECTIONComboBox.setItemText(3, _translate("MainWindow", "5cse8"))
        self.sECTIONComboBox.setItemText(4, _translate("MainWindow", "5cse9"))
        self.sECTIONComboBox.setItemText(5, _translate("MainWindow", "5cse10"))
        
        self.sEMESTERLabel.setText(_translate("MainWindow", "SEMESTER"))
        
        self.sEMESTERComboBox.setItemText(0, _translate("MainWindow", "SEM_1"))
        self.sEMESTERComboBox.setItemText(1, _translate("MainWindow", "SEM_2"))
        self.sEMESTERComboBox.setItemText(2, _translate("MainWindow", "SEM_3"))
        self.sEMESTERComboBox.setItemText(3, _translate("MainWindow", "SEM_4"))
        self.sEMESTERComboBox.setItemText(4, _translate("MainWindow", "SEM_5"))
        self.sEMESTERComboBox.setItemText(5, _translate("MainWindow", "SEM_6"))
        self.sEMESTERComboBox.setItemText(6, _translate("MainWindow", "SEM_7"))
        self.sEMESTERComboBox.setItemText(7, _translate("MainWindow", "SEM_8"))
        self.sEMESTERComboBox.setItemText(8, _translate("MainWindow", "SEM_9"))
        self.sEMESTERComboBox.setItemText(9, _translate("MainWindow", "SEM_10"))
        
        self.cOURSE_CODELabel.setText(_translate("MainWindow", "COURSE_CODE"))
        self.sCHOOL_CODELabel.setText(_translate("MainWindow", "SCHOOL_CODE"))
        
        self.sCHOOL_CODEComboBox.setItemText(0, _translate("MainWindow", "SOE"))
        self.sCHOOL_CODEComboBox.setItemText(1, _translate("MainWindow", "SOL"))
        self.sCHOOL_CODEComboBox.setItemText(2, _translate("MainWindow", "M.TECH"))
        self.sCHOOL_CODEComboBox.setItemText(3, _translate("MainWindow", "Phd"))
        
        self.commandLinkButton.setText(_translate("MainWindow", "REGISTER"))
        
        self.SETTINGS.setTabText(self.SETTINGS.indexOf(self.Register_Faces), _translate("MainWindow", "Register_Faces"))
        
        self.dATASET_SAVE_PATHLabel.setText(_translate("MainWindow", "DATASET_SAVE_PATH"))
        
        self.iMAGE_PATHLabel.setText(_translate("MainWindow", "IMAGE_PATH"))
        
        self.eXCEL_SHEET_PATHLabel.setText(_translate("MainWindow", "EXCEL_SHEET_PATH"))
        
        self.saveButton.setText(_translate("MainWindow", "SAVE BUTTON"))
        
        self.SETTINGS.setTabText(self.SETTINGS.indexOf(self.tab), _translate("MainWindow", "SETTINGS"))
        
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionoen.setText(_translate("MainWindow", "open"))
        self.actionsave_as.setText(_translate("MainWindow", "save as"))
        self.actionuct.setText(_translate("MainWindow", "uct"))
        self.actioncoopy.setText(_translate("MainWindow", "coopy"))
        self.actionTAKE_ATTENDANCE.setText(_translate("MainWindow", "TAKE_ATTENDANCE"))
        self.actionTAKE_ATTENDANCE.setToolTip(_translate("MainWindow", "takes_attendance"))
        self.actionREGISTER.setText(_translate("MainWindow", "REGISTER"))
        self.actionREGISTER.setToolTip(_translate("MainWindow", "maps to register screen"))
        self.actionSETTINGS.setText(_translate("MainWindow", "SETTINGS"))
        self.actionSETTINGS.setToolTip(_translate("MainWindow", "configuring the locations"))
#import UP_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
