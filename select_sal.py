from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义一个根据工资号查找对应工资信息的函数
    def select_sal(self):
        try:
            var_salno = self.salnoEdit.text()
            if "'" in var_salno:
                self.textBrowser.setText("")
                self.messagelabel.setText("输入有误，请重新输入！")
            else:
                conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                c = conn.cursor()  # 获取cursor
                x = c.execute('select * from sal where salno={}'.format(var_salno))  # 使用cursor进行各种操作
                rs = x.fetchall()
                if (rs == []):
                    self.textBrowser.setText("信息不存在")
                else:
                    self.textBrowser.setText("工资号，员工号，工资时间，基本工资，请假扣除工资，处罚扣除工资，税收扣除工资，加班补贴工资，出差补贴工资，津贴工资，工资总额：\n" + str(rs))
                self.messagelabel.setText("")
                c.close()  # 关闭cursor
                conn.close()
        except cx_Oracle.DatabaseError:
            self.textBrowser.setText("")
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义根据工资号查找对应工资信息界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 533)
        self.salnolabel = QtWidgets.QLabel(Dialog) #工资号标签
        self.salnolabel.setGeometry(QtCore.QRect(50, 60, 101, 31))
        self.salnolabel.setObjectName("salnolabel")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog) #显示输出框
        self.textBrowser.setGeometry(QtCore.QRect(30, 130, 681, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.salnoEdit = QtWidgets.QLineEdit(Dialog) #工资号输入框
        self.salnoEdit.setGeometry(QtCore.QRect(140, 60, 561, 31))
        self.salnoEdit.setObjectName("salnoEdit")
        self.b_ok = QtWidgets.QPushButton(Dialog) #确定按钮
        self.b_ok.setGeometry(QtCore.QRect(500, 470, 93, 28))
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.select_sal)
        self.b_exit = QtWidgets.QPushButton(Dialog) #退出按钮
        self.b_exit.setGeometry(QtCore.QRect(620, 470, 93, 28))
        self.b_exit.setObjectName("b_exit")
        self.b_exit.clicked.connect(QCoreApplication.instance().quit)
        self.messagelabel = QtWidgets.QLabel(Dialog) #提示标签
        self.messagelabel.setGeometry(QtCore.QRect(280, 90, 161, 31))
        self.messagelabel.setObjectName("messagelabel")
        self.messagelabel.setStyleSheet("color:red")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "根据工资号查找对应工资信息"))
        self.salnolabel.setText(_translate("Dialog", "工资号："))
        self.b_ok.setText(_translate("Dialog", "确定"))
        self.b_exit.setText(_translate("Dialog", "退出"))
        self.messagelabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())
