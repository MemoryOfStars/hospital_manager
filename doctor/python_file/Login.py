from ui_file.login import Ui_Login
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import pymysql
from python_file.getip import get_host_ip
from python_file import glb
from python_file import glb
class Login(QMainWindow, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.login_is_sucess_flag = 0 # 登录成功1
    def login(self):
        '''
        获取用户名，密码，验证成功login_sucess_flag = 1
        :return: None
        '''
        self.passname = self.textEdit.toPlainText()
        self.password = self.textEdit_2.toPlainText()
        conn = pymysql.connect(host=glb.get_value("MYSQL_IP"), user="root", passwd="caoqiming6666", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()
        length = cur.execute("SELECT 医生ID,医生密码 FROM 医生")
        sql = cur.fetchall()
        self.login_is_sucess_flag = 0
        for i in range(length):
            if (self.passname == sql[i][0] and self.password == sql[i][1]):
                self.login_is_sucess_flag = 1
        cur.close()
        conn.close()

    def Close(self, login_is_sucess_flag):
        if (login_is_sucess_flag == 1):
            conn = pymysql.connect(host=glb.get_value("MYSQL_IP"), user="root", passwd="caoqiming6666",
                                   db="hospital_management", port=3306, charset="utf8")
            cur = conn.cursor()
            res = [str(get_host_ip()), str(3001)]
            cur.execute("UPDATE 医生 SET IP地址=%s WHERE 医生ID=%s", res)
            conn.commit()
            cur.close()
            conn.close()
            self.close()
            # 记录医生ID,全局变量
            glb.set_value("DOCTOR_ID",self.passname)

        self.textEdit.setText("")
        self.textEdit_2.setText("")

