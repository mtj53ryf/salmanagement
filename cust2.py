from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_MainWindow(object):
    #浏览客户信息
    def view_cust(self):
        conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')
        c = conn.cursor()  # 获取cursor
        x = c.execute('select * from cust')  # 使用cursor进行各种操作
        rs = x.fetchall()
        if (rs == []):
            self.textBrowser.setText("信息不存在")
        else:
            self.textBrowser.setText("客户号，客户姓名，性别，出生日期，电话：\n"+str(rs))
        c.close()  # 关闭cursor
        conn.close()
    #查找客户信息
    def select_cust(self):
        os.system('python select_cust.py')
    #定义客户管理系统界面
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 520, 801, 81))
        self.groupBox.setObjectName("groupBox")
        self.b_view_cust = QtWidgets.QPushButton(self.groupBox) #浏览数据按钮
        self.b_view_cust.setGeometry(QtCore.QRect(220, 20, 93, 28))
        self.b_view_cust.setObjectName("b_view_cust")
        self.b_view_cust.clicked.connect(self.view_cust)
        self.b_select_cust = QtWidgets.QPushButton(self.groupBox) #查找数据按钮
        self.b_select_cust.setGeometry(QtCore.QRect(470, 20, 93, 28))
        self.b_select_cust.setObjectName("b_select_cust")
        self.b_select_cust.clicked.connect(self.select_cust)
        self.b_close_cust = QtWidgets.QPushButton(self.centralwidget) #退出按钮
        self.b_close_cust.setGeometry(QtCore.QRect(690, 20, 93, 28))
        self.b_close_cust.setObjectName("b_close_cust")
        self.b_close_cust.clicked.connect(QCoreApplication.instance().quit)
        self.label = QtWidgets.QLabel(self.centralwidget) #客户管理系统标签
        self.label.setGeometry(QtCore.QRect(270, -20, 261, 151))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "客户管理系统"))
        self.groupBox.setTitle(_translate("MainWindow", "数据库操作"))
        self.b_view_cust.setText(_translate("MainWindow", "浏览数据"))
        self.b_select_cust.setText(_translate("MainWindow", "查找数据"))
        self.b_close_cust.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">客户管理系统</p></body></html>"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())