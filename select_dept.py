from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义一个根据部门号或部门名称查找对应部门信息的函数
    def select_dept(self):
        try:
            var_deptno = self.deptnoEdit.text()
            var_dname = self.dnameEdit.text()
            if var_dname=='' and var_deptno!='':
                if "'" in var_deptno:
                    self.textBrowser.setText("")
                    self.messagelabel.setText("输入有误，请重新输入！")
                else:
                    conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                    c = conn.cursor()  # 获取cursor
                    x = c.execute('select * from dept where deptno={}'.format(var_deptno))  # 使用cursor进行各种操作
                    rs = x.fetchall()
                    if (rs == []):
                        self.textBrowser.setText("信息不存在")
                    else:
                        self.textBrowser.setText("部门号，部门名称，经理姓名：\n" + str(rs))
                    self.messagelabel.setText("")
                    c.close()  # 关闭cursor
                    conn.close()
            elif var_deptno=='' and var_dname!='':
                conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                c = conn.cursor()  # 获取cursor
                x = c.execute('select * from dept where dname={}'.format(var_dname))  # 使用cursor进行各种操作
                rs = x.fetchall()
                if (rs == []):
                    self.textBrowser.setText("信息不存在")
                else:
                    self.textBrowser.setText("部门号，部门名称，经理姓名：\n" + str(rs))
                self.messagelabel.setText("")
                c.close()  # 关闭cursor
                conn.close()
            else:
                if "'" in var_deptno:
                    self.textBrowser.setText("")
                    self.messagelabel.setText("输入有误，请重新输入！")
                else:
                    conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                    c = conn.cursor()  # 获取cursor
                    x = c.execute('select * from dept where deptno={} and dname={}'.format(var_deptno,var_dname))  # 使用cursor进行各种操作
                    rs = x.fetchall()
                    if (rs == []):
                        self.textBrowser.setText("信息不存在")
                    else:
                        self.textBrowser.setText("部门号，部门名称，经理姓名：\n" + str(rs))
                    self.messagelabel.setText("")
                    c.close()  # 关闭cursor
                    conn.close()
        except cx_Oracle.DatabaseError:
            self.textBrowser.setText("")
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义根据部门号或部门名称查找对应部门信息界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 533)
        self.deptnolabel = QtWidgets.QLabel(Dialog) #部门号标签
        self.deptnolabel.setGeometry(QtCore.QRect(50, 10, 101, 31))
        self.deptnolabel.setObjectName("deptnolabel")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog) #显示输出框
        self.textBrowser.setGeometry(QtCore.QRect(30, 130, 681, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.deptnoEdit = QtWidgets.QLineEdit(Dialog) #部门号输入框
        self.deptnoEdit.setGeometry(QtCore.QRect(140, 10, 561, 31))
        self.deptnoEdit.setObjectName("deptnoEdit")
        self.dnamelabel = QtWidgets.QLabel(Dialog) #部门名称标签
        self.dnamelabel.setGeometry(QtCore.QRect(50, 50, 101, 31))
        self.dnamelabel.setObjectName("dnamelabel")
        self.dnameEdit = QtWidgets.QLineEdit(Dialog) #部门名称输入框
        self.dnameEdit.setGeometry(QtCore.QRect(140, 50, 561, 31))
        self.dnameEdit.setObjectName("dnameEdit")
        self.b_ok = QtWidgets.QPushButton(Dialog) #确定按钮
        self.b_ok.setGeometry(QtCore.QRect(500, 470, 93, 28))
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.select_dept)
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
        Dialog.setWindowTitle(_translate("Dialog", "根据部门号或部门名称查找对应部门信息"))
        self.deptnolabel.setText(_translate("Dialog", "部门号："))
        self.dnamelabel.setText(_translate("Dialog", "部门名称："))
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
