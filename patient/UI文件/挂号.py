# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '挂号.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.second_page_widget = QtWidgets.QWidget(Form)
        self.second_page_widget.setGeometry(QtCore.QRect(260, 20, 981, 681))
        self.second_page_widget.setObjectName("second_page_widget")
        self.label = QtWidgets.QLabel(self.second_page_widget)
        self.label.setGeometry(QtCore.QRect(430, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.second_page_widget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.second_page_widget)
        self.comboBox.setGeometry(QtCore.QRect(150, 100, 69, 28))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_3 = QtWidgets.QLabel(self.second_page_widget)
        self.label_3.setGeometry(QtCore.QRect(430, 100, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.second_page_widget)
        self.comboBox_2.setGeometry(QtCore.QRect(570, 100, 69, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(self.second_page_widget)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.second_page_widget)
        self.label_5.setGeometry(QtCore.QRect(60, 240, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.second_page_widget)
        self.label_6.setGeometry(QtCore.QRect(60, 300, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.second_page_widget)
        self.comboBox_7.setGeometry(QtCore.QRect(160, 300, 69, 28))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_7 = QtWidgets.QLabel(self.second_page_widget)
        self.label_7.setGeometry(QtCore.QRect(60, 370, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.second_page_widget)
        self.pushButton.setGeometry(QtCore.QRect(260, 600, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.second_page_widget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 600, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.second_page_widget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(150, 240, 194, 30))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.groupBox = QtWidgets.QGroupBox(self.second_page_widget)
        self.groupBox.setGeometry(QtCore.QRect(140, 160, 411, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 10, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.second_page_widget)
        self.groupBox_2.setGeometry(QtCore.QRect(140, 350, 411, 61))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 20, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(290, 20, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.tableView = QtWidgets.QTableView(self.second_page_widget)
        self.tableView.setGeometry(QtCore.QRect(50, 410, 891, 161))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "挂号单"))
        self.label_2.setText(_translate("Form", "医院"))
        self.comboBox.setItemText(0, _translate("Form", "A"))
        self.comboBox.setItemText(1, _translate("Form", "B"))
        self.comboBox.setItemText(2, _translate("Form", "C"))
        self.label_3.setText(_translate("Form", "科室"))
        self.comboBox_2.setItemText(0, _translate("Form", "甲"))
        self.comboBox_2.setItemText(1, _translate("Form", "乙"))
        self.label_4.setText(_translate("Form", "挂号类型"))
        self.label_5.setText(_translate("Form", "时间"))
        self.label_6.setText(_translate("Form", "时长"))
        self.comboBox_7.setItemText(0, _translate("Form", "一小时"))
        self.comboBox_7.setItemText(1, _translate("Form", "一个半小时"))
        self.comboBox_7.setItemText(2, _translate("Form", "两小时"))
        self.label_7.setText(_translate("Form", "医生"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.radioButton_2.setText(_translate("Form", "为他人挂号"))
        self.radioButton.setText(_translate("Form", "为自己挂号"))
        self.radioButton_3.setText(_translate("Form", "推荐医生"))
        self.radioButton_4.setText(_translate("Form", "自己选择"))

