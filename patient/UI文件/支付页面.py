# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '支付页面.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.pay_widget = QtWidgets.QWidget(Form)
        self.pay_widget.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.pay_widget.setObjectName("pay_widget")
        self.page_title_label = QtWidgets.QLabel(self.pay_widget)
        self.page_title_label.setGeometry(QtCore.QRect(390, 110, 241, 61))
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.page_title_label.setFont(font)
        self.page_title_label.setObjectName("page_title_label")
        self.pushButton = QtWidgets.QPushButton(self.pay_widget)
        self.pushButton.setGeometry(QtCore.QRect(440, 460, 90, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.page_title_label.setText(_translate("Form", "支付页面"))
        self.pushButton.setText(_translate("Form", "支付"))

