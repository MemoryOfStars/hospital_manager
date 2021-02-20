# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_patient.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 352)
        self.login_Dialog = QtWidgets.QWidget(Dialog)
        self.login_Dialog.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.login_Dialog.setObjectName("login_Dialog")
        self.register_button = QtWidgets.QPushButton(self.login_Dialog)
        self.register_button.setGeometry(QtCore.QRect(280, 250, 81, 30))
        self.register_button.setObjectName("register_button")
        self.login_button = QtWidgets.QPushButton(self.login_Dialog)
        self.login_button.setGeometry(QtCore.QRect(180, 250, 90, 30))
        self.login_button.setObjectName("login_button")
        self.patient_ID_input = QtWidgets.QLineEdit(self.login_Dialog)
        self.patient_ID_input.setGeometry(QtCore.QRect(180, 170, 181, 30))
        self.patient_ID_input.setObjectName("patient_ID_input")
        self.doctor_login_button = QtWidgets.QPushButton(self.login_Dialog)
        self.doctor_login_button.setGeometry(QtCore.QRect(380, 330, 41, 21))
        self.doctor_login_button.setObjectName("doctor_login_button")
        self.patient_password_input = QtWidgets.QLineEdit(self.login_Dialog)
        self.patient_password_input.setGeometry(QtCore.QRect(180, 210, 181, 30))
        self.patient_password_input.setObjectName("patient_password_input")
        self.manager_login_button = QtWidgets.QPushButton(self.login_Dialog)
        self.manager_login_button.setGeometry(QtCore.QRect(430, 330, 41, 21))
        self.manager_login_button.setObjectName("manager_login_button")
        self.top_picture_Dialog = QtWidgets.QLabel(self.login_Dialog)
        self.top_picture_Dialog.setGeometry(QtCore.QRect(0, 0, 501, 141))
        self.top_picture_Dialog.setText("")
        self.top_picture_Dialog.setPixmap(QtGui.QPixmap("../../../.designer/backup/pic1.jpg"))
        self.top_picture_Dialog.setObjectName("top_picture_Dialog")
        self.profile_picture_lable = QtWidgets.QLabel(self.login_Dialog)
        self.profile_picture_lable.setGeometry(QtCore.QRect(60, 180, 91, 91))
        self.profile_picture_lable.setText("")
        self.profile_picture_lable.setPixmap(QtGui.QPixmap("../../../.designer/backup/pic1.jpg"))
        self.profile_picture_lable.setObjectName("profile_picture_lable")
        self.subtrack_button = QtWidgets.QPushButton(self.login_Dialog)
        self.subtrack_button.setGeometry(QtCore.QRect(400, 10, 30, 30))
        self.subtrack_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../subtract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subtrack_button.setIcon(icon)
        self.subtrack_button.setObjectName("subtrack_button")
        self.close_button = QtWidgets.QPushButton(self.login_Dialog)
        self.close_button.setGeometry(QtCore.QRect(440, 10, 30, 30))
        self.close_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setObjectName("close_button")
        self.register_button.raise_()
        self.login_button.raise_()
        self.patient_ID_input.raise_()
        self.doctor_login_button.raise_()
        self.patient_password_input.raise_()
        self.manager_login_button.raise_()
        self.top_picture_Dialog.raise_()
        self.profile_picture_lable.raise_()
        self.close_button.raise_()
        self.subtrack_button.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.register_button.setText(_translate("Dialog", "注册"))
        self.login_button.setText(_translate("Dialog", "登录"))
        self.doctor_login_button.setText(_translate("Dialog", "医生登录"))
        self.manager_login_button.setText(_translate("Dialog", "管理员登录"))

