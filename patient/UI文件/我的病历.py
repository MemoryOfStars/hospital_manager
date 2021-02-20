# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '我的病历.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.medical_record_widget = QtWidgets.QWidget(Form)
        self.medical_record_widget.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.medical_record_widget.setObjectName("medical_record_widget")
        self.tableWidget = QtWidgets.QTableWidget(self.medical_record_widget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 70, 901, 561))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

