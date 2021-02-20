# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_patient.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 448)
        self.patient_register_widget = QtWidgets.QWidget(Dialog)
        self.patient_register_widget.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.patient_register_widget.setObjectName("patient_register_widget")
        self.register_id_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_id_label.setGeometry(QtCore.QRect(80, 50, 25, 18))
        self.register_id_label.setObjectName("register_id_label")
        self.register_password_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_password_label.setGeometry(QtCore.QRect(80, 93, 25, 18))
        self.register_password_label.setObjectName("register_password_label")
        self.register_name_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_name_label.setGeometry(QtCore.QRect(80, 136, 24, 18))
        self.register_name_label.setObjectName("register_name_label")
        self.register_idcard_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_idcard_label.setGeometry(QtCore.QRect(80, 178, 49, 18))
        self.register_idcard_label.setObjectName("register_idcard_label")
        self.register_address_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_address_label.setGeometry(QtCore.QRect(80, 221, 25, 18))
        self.register_address_label.setObjectName("register_address_label")
        self.register_age_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_age_label.setGeometry(QtCore.QRect(80, 264, 25, 18))
        self.register_age_label.setObjectName("register_age_label")
        self.registerid_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.registerid_input.setGeometry(QtCore.QRect(140, 50, 251, 30))
        self.registerid_input.setObjectName("registerid_input")
        self.register_password_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_password_input.setGeometry(QtCore.QRect(140, 93, 251, 30))
        self.register_password_input.setObjectName("register_password_input")
        self.register_name_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_name_input.setGeometry(QtCore.QRect(140, 136, 251, 30))
        self.register_name_input.setObjectName("register_name_input")
        self.register_idcard_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_idcard_input.setGeometry(QtCore.QRect(140, 178, 251, 30))
        self.register_idcard_input.setObjectName("register_idcard_input")
        self.register_address_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_address_input.setGeometry(QtCore.QRect(140, 221, 251, 30))
        self.register_address_input.setObjectName("register_address_input")
        self.register_age_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_age_input.setGeometry(QtCore.QRect(140, 264, 251, 30))
        self.register_age_input.setObjectName("register_age_input")
        self.register_submit_button = QtWidgets.QPushButton(self.patient_register_widget)
        self.register_submit_button.setGeometry(QtCore.QRect(140, 310, 90, 30))
        self.register_submit_button.setObjectName("register_submit_button")
        self.register_cancle_button = QtWidgets.QPushButton(self.patient_register_widget)
        self.register_cancle_button.setGeometry(QtCore.QRect(300, 310, 90, 30))
        self.register_cancle_button.setObjectName("register_cancle_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.register_id_label.setText(_translate("Dialog", "账号"))
        self.register_password_label.setText(_translate("Dialog", "密码"))
        self.register_name_label.setText(_translate("Dialog", "姓名"))
        self.register_idcard_label.setText(_translate("Dialog", "身份证号"))
        self.register_address_label.setText(_translate("Dialog", "地址"))
        self.register_age_label.setText(_translate("Dialog", "年龄"))
        self.register_submit_button.setText(_translate("Dialog", "提交"))
        self.register_cancle_button.setText(_translate("Dialog", "返回"))

