# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '从热点选择2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.widget.setObjectName("widget")
        self.ComRan_comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.ComRan_comboBox_2.setGeometry(QtCore.QRect(20, 20, 201, 26))
        self.ComRan_comboBox_2.setObjectName("ComRan_comboBox_2")
        self.ComRan_comboBox_2.addItem("")
        self.area_comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.area_comboBox_2.setGeometry(QtCore.QRect(270, 20, 201, 26))
        self.area_comboBox_2.setObjectName("area_comboBox_2")
        self.area_comboBox_2.addItem("")
        self.area_comboBox_2.addItem("")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(20, 130, 911, 491))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ComRan_comboBox_2.setItemText(0, _translate("Form", "综合排序"))
        self.area_comboBox_2.setItemText(0, _translate("Form", "地区选择"))
        self.area_comboBox_2.setItemText(1, _translate("Form", "甘井子"))

