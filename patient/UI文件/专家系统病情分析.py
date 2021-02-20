# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '专家系统病情分析.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.expert_sys_widget = QtWidgets.QWidget(Form)
        self.expert_sys_widget.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.expert_sys_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.expert_sys_widget.setAutoFillBackground(False)
        self.expert_sys_widget.setObjectName("expert_sys_widget")
        self.page_title_label = QtWidgets.QLabel(self.expert_sys_widget)
        self.page_title_label.setGeometry(QtCore.QRect(370, 0, 261, 61))
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.page_title_label.setFont(font)
        self.page_title_label.setAutoFillBackground(True)
        self.page_title_label.setObjectName("page_title_label")
        self.descrip_textBrowser = QtWidgets.QTextBrowser(self.expert_sys_widget)
        self.descrip_textBrowser.setGeometry(QtCore.QRect(40, 100, 891, 341))
        self.descrip_textBrowser.setObjectName("descrip_textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.expert_sys_widget)
        self.pushButton.setGeometry(QtCore.QRect(440, 520, 90, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.page_title_label.setText(_translate("Form", "专家系统病情分析"))
        self.descrip_textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans CJK SC\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">专家系统详细描述</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "进入聊天"))

