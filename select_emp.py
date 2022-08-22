from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义一个根据员工号或员工姓名查找对应员工信息、经理和基本工资的函数
    def select_emp(self):
        try:
            var_empno = self.empnoEdit.text()
            var_ename = self.enameEdit.text()
            if var_ename=='' and var_empno!='':
                if "'" in var_empno:
                    self.textBrowser.setText("")
                    self.messagelabel.setText("输入有误，请重新输入！")
                else:
                    conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                    c = conn.cursor()  # 获取cursor
                    x = c.execute('select * from emp where empno={}'.format(var_empno))  # 使用cursor进行各种操作
                    rs = x.fetchall()
                    x1 = c.execute('select mgrname from emp_mgr where empno={}'.format(var_empno))
                    rs1 = x1.fetchall()
                    x2 = c.execute('select basedsal from emp_sal where empno={}'.format(var_empno))
                    rs2 = x2.fetchall()
                    if (rs == []):
                        self.textBrowser.setText("信息不存在")
                    else:
                        self.textBrowser.setText("员工号，员工姓名，性别，出生日期，职业，工资，雇佣日期，部门号，经理姓名，基本工资：\n" + str(rs) + str(rs1) + str(rs2))
                    self.messagelabel.setText("")
                    c.close()  # 关闭cursor
                    conn.close()
            elif var_empno=='' and var_ename!='':
                conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                c = conn.cursor()  # 获取cursor
                x = c.execute('select * from emp where ename={}'.format(var_ename))  # 使用cursor进行各种操作
                rs = x.fetchall()
                x1 = c.execute('select mgrname from emp_mgr where ename={}'.format(var_ename))
                rs1 = x1.fetchall()
                x2 = c.execute('select basedsal from emp_sal where ename={}'.format(var_ename))
                rs2 = x2.fetchall()
                if (rs == []):
                    self.textBrowser.setText("信息不存在")
                else:
                    self.textBrowser.setText("员工号，员工姓名，性别，出生日期，职业，工资，雇佣日期，部门号，经理姓名，基本工资：\n" + str(rs) + str(rs1) + str(rs2))
                self.messagelabel.setText("")
                c.close()  # 关闭cursor
                conn.close()
            else:
                if "'" in var_empno:
                    self.textBrowser.setText("")
                    self.messagelabel.setText("输入有误，请重新输入！")
                else:
                    conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                    c = conn.cursor()  # 获取cursor
                    x = c.execute('select * from emp where empno={} and ename={}'.format(var_empno,var_ename))  # 使用cursor进行各种操作
                    rs = x.fetchall()
                    x1 = c.execute('select mgrname from emp_mgr where empno={} and ename={}'.format(var_empno,var_ename))
                    rs1 = x1.fetchall()
                    x2 = c.execute('select basedsal from emp_sal where empno={} and ename={}'.format(var_empno,var_ename))
                    rs2 = x2.fetchall()
                    if (rs == []):
                        self.textBrowser.setText("信息不存在")
                    else:
                        self.textBrowser.setText("员工号，员工姓名，性别，出生日期，职业，工资，雇佣日期，部门号，经理姓名，基本工资：\n" + str(rs) + str(rs1) + str(rs2))
                    self.messagelabel.setText("")
                    c.close()  # 关闭cursor
                    conn.close()
        except cx_Oracle.DatabaseError:
            self.textBrowser.setText("")
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义根据员工号或员工姓名查找对应员工信息界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 533)
        self.empnolabel = QtWidgets.QLabel(Dialog) #员工号标签
        self.empnolabel.setGeometry(QtCore.QRect(50, 10, 101, 31))
        self.empnolabel.setObjectName("empnolabel")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog) #显示输出框
        self.textBrowser.setGeometry(QtCore.QRect(30, 130, 681, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.empnoEdit = QtWidgets.QLineEdit(Dialog) #员工号输入框
        self.empnoEdit.setGeometry(QtCore.QRect(140, 10, 561, 31))
        self.empnoEdit.setObjectName("empnoEdit")
        self.enamelabel = QtWidgets.QLabel(Dialog)  #员工姓名标签
        self.enamelabel.setGeometry(QtCore.QRect(50, 50, 101, 31))
        self.enamelabel.setObjectName("enamelabel")
        self.enameEdit = QtWidgets.QLineEdit(Dialog)  #员工姓名输入框
        self.enameEdit.setGeometry(QtCore.QRect(140, 50, 561, 31))
        self.enameEdit.setObjectName("enameEdit")
        self.b_ok = QtWidgets.QPushButton(Dialog) #确定按钮
        self.b_ok.setGeometry(QtCore.QRect(500, 470, 93, 28))
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.select_emp)
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
        Dialog.setWindowTitle(_translate("Dialog", "根据员工号或员工姓名查找对应员工信息"))
        self.empnolabel.setText(_translate("Dialog", "员工号："))
        self.enamelabel.setText(_translate("Dialog", "员工姓名："))
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

