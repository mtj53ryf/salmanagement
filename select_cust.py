from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义一个根据客户号或客户姓名查找对应客户信息的函数
    def select_cust(self):
        try:
            var_custno = self.custnoEdit.text()
            var_custname = self.custnameEdit.text()
            if var_custname=='' and var_custno!='':
                if "'" in var_custno:
                    self.textBrowser.setText("")
                    self.messagelabel.setText("输入有误，请重新输入！")
                else:
                    conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                    c = conn.cursor()  # 获取cursor
                    x = c.execute('select * from cust where custno={}'.format(var_custno))  # 使用cursor进行各种操作
                    rs = x.fetchall()
                    if (rs == []):
                        self.textBrowser.setText("信息不存在")
                    else:
                        self.textBrowser.setText("客户号，客户姓名，性别，出生日期，电话：\n" + str(rs))
                    self.messagelabel.setText("")
                    c.close()  # 关闭cursor
                    conn.close()
            elif var_custno=='' and var_custname!='':
                conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                c = conn.cursor()  # 获取cursor
                x = c.execute('select * from cust where custname={}'.format(var_custname))  # 使用cursor进行各种操作
                rs = x.fetchall()
                if (rs == []):
                    self.textBrowser.setText("信息不存在")
                else:
                    self.textBrowser.setText("客户号，客户姓名，性别，出生日期，电话：\n" + str(rs))
                self.messagelabel.setText("")
                c.close()  # 关闭cursor
                conn.close()
            else:
                if "'" in var_custno:
                    self.textBrowser.setText("")
                    self.messagelabel.setText("输入有误，请重新输入！")
                else:
                    conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                    c = conn.cursor()  # 获取cursor
                    x = c.execute('select * from cust where custno={} and custname={}'.format(var_custno,var_custname))  # 使用cursor进行各种操作
                    rs = x.fetchall()
                    if (rs == []):
                        self.textBrowser.setText("信息不存在")
                    else:
                        self.textBrowser.setText("客户号，客户姓名，性别，出生日期，电话：\n" + str(rs))
                    self.messagelabel.setText("")
                    c.close()  # 关闭cursor
                    conn.close()
        except cx_Oracle.DatabaseError:
            self.textBrowser.setText("")
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义一个根据客户号或客户姓名查找对应客户信息界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 533)
        self.custnolabel = QtWidgets.QLabel(Dialog) #客户号标签
        self.custnolabel.setGeometry(QtCore.QRect(50, 10, 101, 31))
        self.custnolabel.setObjectName("custnolabel")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog) #显示输出框
        self.textBrowser.setGeometry(QtCore.QRect(30, 130, 681, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.custnoEdit = QtWidgets.QLineEdit(Dialog) #客户号输入框
        self.custnoEdit.setGeometry(QtCore.QRect(140, 10, 561, 31))
        self.custnoEdit.setObjectName("custnoEdit")
        self.custnamelabel = QtWidgets.QLabel(Dialog)  #客户姓名标签
        self.custnamelabel.setGeometry(QtCore.QRect(50, 50, 101, 31))
        self.custnamelabel.setObjectName("custnamelabel")
        self.custnameEdit = QtWidgets.QLineEdit(Dialog)  #客户姓名输入框
        self.custnameEdit.setGeometry(QtCore.QRect(140, 50, 561, 31))
        self.custnameEdit.setObjectName("custnameEdit")
        self.b_ok = QtWidgets.QPushButton(Dialog) #确定按钮
        self.b_ok.setGeometry(QtCore.QRect(500, 470, 93, 28))
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.select_cust)
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
        Dialog.setWindowTitle(_translate("Dialog", "根据客户号或客户名称查找对应客户信息"))
        self.custnolabel.setText(_translate("Dialog", "客户号："))
        self.custnamelabel.setText(_translate("Dialog", "客户姓名："))
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

