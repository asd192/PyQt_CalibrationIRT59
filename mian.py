# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(411, 10, 78, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setEnabled(True)
        self.dateEdit.setGeometry(QtCore.QRect(670, 10, 110, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit.setWrapping(False)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(316, 15, 91, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 130, 261, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setFrame(True)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 490, 801, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(162, 15, 31, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(201, 10, 101, 25))
        self.comboBox_2.setMaximumSize(QtCore.QSize(101, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAcceptDrops(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.line_up = QtWidgets.QFrame(self.centralwidget)
        self.line_up.setGeometry(QtCore.QRect(10, 35, 771, 20))
        self.line_up.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_up.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_up.setObjectName("line_up")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 110, 141, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(15, 15, 16, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(36, 10, 113, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(135, 55, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(15, 60, 121, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(210, 55, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(541, 15, 131, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(500, 60, 131, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(310, 110, 141, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(290, 130, 161, 181))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setReadOnly(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(150, 320, 71, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 340, 261, 71))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(630, 55, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(705, 55, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(690, 450, 86, 30))
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu1 = QtWidgets.QMenu(self.menubar)
        self.menu1.setGeometry(QtCore.QRect(317, 165, 198, 110))
        self.menu1.setObjectName("menu1")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.menu1.addAction(self.action_3)
        self.menu1.addSeparator()
        self.menu1.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menubar.addAction(self.menu1.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.label.setBuddy(self.comboBox)
        self.label_7.setBuddy(self.comboBox_2)
        self.label_9.setBuddy(self.lineEdit_6)
        self.label_11.setBuddy(self.dateEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox_2, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.comboBox_3)
        MainWindow.setTabOrder(self.comboBox_3, self.comboBox_4)
        MainWindow.setTabOrder(self.comboBox_4, self.comboBox_5)
        MainWindow.setTabOrder(self.comboBox_5, self.comboBox_6)
        MainWindow.setTabOrder(self.comboBox_6, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_12)
        MainWindow.setTabOrder(self.lineEdit_12, self.lineEdit_13)
        MainWindow.setTabOrder(self.lineEdit_13, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        MainWindow.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "2011"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2012"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2013"))
        self.comboBox.setItemText(3, _translate("MainWindow", "2014"))
        self.comboBox.setItemText(4, _translate("MainWindow", "2015"))
        self.comboBox.setItemText(5, _translate("MainWindow", "2016"))
        self.comboBox.setItemText(6, _translate("MainWindow", "2017"))
        self.comboBox.setItemText(7, _translate("MainWindow", "2018"))
        self.comboBox.setItemText(8, _translate("MainWindow", "2019"))
        self.comboBox.setItemText(9, _translate("MainWindow", "2020"))
        self.comboBox.setItemText(10, _translate("MainWindow", "2021"))
        self.comboBox.setItemText(11, _translate("MainWindow", "2022"))
        self.label.setText(_translate("MainWindow", "Год выпуска:"))
        self.label_2.setText(_translate("MainWindow", "5%"))
        self.label_3.setText(_translate("MainWindow", "25%"))
        self.label_4.setText(_translate("MainWindow", "50%"))
        self.label_5.setText(_translate("MainWindow", "75%"))
        self.label_6.setText(_translate("MainWindow", "95%"))
        self.label_7.setText(_translate("MainWindow", "Тип:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ИРТ 5920"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "ИРТ 5940"))
        self.label_8.setText(_translate("MainWindow", "Показания прибора"))
        self.label_9.setText(_translate("MainWindow", "№"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "mA"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "ТСМ"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "ТП"))
        self.label_10.setText(_translate("MainWindow", "Входной сигнал:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "0-5"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "0-20"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "4-20"))
        self.label_11.setText(_translate("MainWindow", "Дата калибровки:"))
        self.label_12.setText(_translate("MainWindow", "Выходной сигнал:"))
        self.label_13.setText(_translate("MainWindow", "Входные значения"))
        self.label_14.setText(_translate("MainWindow", "ПВИ - 24В"))
        self.label_15.setText(_translate("MainWindow", "R = 0 Ом"))
        self.label_16.setText(_translate("MainWindow", "R = 820 Ом"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "mA"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "ТСМ"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "ТП"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "0-5"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "0-20"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "4-20"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menu1.setTitle(_translate("MainWindow", "Файл"))
        self.menu.setTitle(_translate("MainWindow", "Помощь"))
        self.action_3.setText(_translate("MainWindow", "Открыть"))
        self.action_5.setText(_translate("MainWindow", "Выйти"))
        self.action_6.setText(_translate("MainWindow", "Справка"))
