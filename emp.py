from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_MainWindow(object):
    #浏览员工信息
    def view_emp(self):
        conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')
        c = conn.cursor()  # 获取cursor
        x = c.execute('select * from emp')  # 使用cursor进行各种操作
        rs = x.fetchall()
        if (rs == []):
            self.textBrowser.setText("信息不存在")
        else:
            self.textBrowser.setText("员工号，员工姓名，性别，出生日期，职业，工资，雇佣日期，部门号：\n"+str(rs))
        c.close()  # 关闭cursor
        conn.close()
    #查找员工信息
    def select_emp(self):
        os.system('python select_emp.py')
    #添加员工信息
    def insert_emp(self):
        os.system('python insert_emp.py')
    #删除员工信息
    def delete_emp(self):
        os.system('python delete_emp.py')
    #修改员工信息
    def update_emp(self):
        os.system('python update_emp.py')
    #定义员工管理系统界面
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 520, 801, 81))
        self.groupBox.setObjectName("groupBox")
        self.b_view_emp = QtWidgets.QPushButton(self.groupBox) #浏览数据按钮
        self.b_view_emp.setGeometry(QtCore.QRect(0, 20, 93, 28))
        self.b_view_emp.setObjectName("b_view_emp")
        self.b_view_emp.clicked.connect(self.view_emp)
        self.b_select_emp = QtWidgets.QPushButton(self.groupBox) #查找数据按钮
        self.b_select_emp.setGeometry(QtCore.QRect(170, 20, 93, 28))
        self.b_select_emp.setObjectName("b_select_emp")
        self.b_select_emp.clicked.connect(self.select_emp)
        self.b_insert_emp = QtWidgets.QPushButton(self.groupBox) #添加数据按钮
        self.b_insert_emp.setGeometry(QtCore.QRect(350, 20, 93, 28))
        self.b_insert_emp.setObjectName("b_insert_emp")
        self.b_insert_emp.clicked.connect(self.insert_emp)
        self.b_delete_emp = QtWidgets.QPushButton(self.groupBox) #删除数据按钮
        self.b_delete_emp.setGeometry(QtCore.QRect(520, 20, 93, 28))
        self.b_delete_emp.setObjectName("b_delete_emp")
        self.b_delete_emp.clicked.connect(self.delete_emp)
        self.b_update_emp = QtWidgets.QPushButton(self.groupBox) #修改数据按钮
        self.b_update_emp.setGeometry(QtCore.QRect(700, 20, 93, 28))
        self.b_update_emp.setObjectName("b_update_emp")
        self.b_update_emp.clicked.connect(self.update_emp)
        self.b_close_emp = QtWidgets.QPushButton(self.centralwidget) #退出按钮
        self.b_close_emp.setGeometry(QtCore.QRect(690, 20, 93, 28))
        self.b_close_emp.setObjectName("b_close_emp")
        self.b_close_emp.clicked.connect(QCoreApplication.instance().quit)
        self.label = QtWidgets.QLabel(self.centralwidget) #员工管理系统标签
        self.label.setGeometry(QtCore.QRect(260, -20, 261, 151))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget) #显示输出框
        self.textBrowser.setGeometry(QtCore.QRect(0, 100, 801, 411))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "员工管理系统"))
        self.groupBox.setTitle(_translate("MainWindow", "数据库操作"))
        self.b_view_emp.setText(_translate("MainWindow", "浏览数据"))
        self.b_select_emp.setText(_translate("MainWindow", "查找数据"))
        self.b_insert_emp.setText(_translate("MainWindow", "添加数据"))
        self.b_delete_emp.setText(_translate("MainWindow", "删除数据"))
        self.b_update_emp.setText(_translate("MainWindow", "修改数据"))
        self.b_close_emp.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">员工管理系统</p></body></html>"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())
