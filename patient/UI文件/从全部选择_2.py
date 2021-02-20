# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '从全部选择_2.ui'
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
        self.area_comboBox = QtWidgets.QComboBox(self.widget)
        self.area_comboBox.setGeometry(QtCore.QRect(260, 40, 201, 26))
        self.area_comboBox.setObjectName("area_comboBox")
        self.area_comboBox.addItem("")
        self.area_comboBox.addItem("")
        self.ComRan_comboBox = QtWidgets.QComboBox(self.widget)
        self.ComRan_comboBox.setGeometry(QtCore.QRect(20, 40, 201, 26))
        self.ComRan_comboBox.setObjectName("ComRan_comboBox")
        self.ComRan_comboBox.addItem("")
        self.department_comboBox = QtWidgets.QComboBox(self.widget)
        self.department_comboBox.setGeometry(QtCore.QRect(490, 40, 201, 26))
        self.department_comboBox.setObjectName("department_comboBox")
        self.department_comboBox.addItem("")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(20, 130, 911, 491))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.area_comboBox.setItemText(0, _translate("Form", "选择地区"))
        self.area_comboBox.setItemText(1, _translate("Form", "甘井子"))
        self.ComRan_comboBox.setItemText(0, _translate("Form", "综合排序"))
        self.department_comboBox.setItemText(0, _translate("Form", "选择科室"))

