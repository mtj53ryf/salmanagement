from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_MainWindow(object):
    #定义打开部门管理系统的函数
    def dept(self):
        os.system('python dept2.py')
    #定义打开员工管理系统的函数
    def emp(self):
        os.system('python emp2.py')
    #定义打开客户管理系统的函数
    def cust(self):
        os.system('python cust2.py')
    #定义打开工资管理系统的函数
    def sal(self):
        os.system('python sal2.py')
    #定义主界面
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b_dept = QtWidgets.QPushButton(self.centralwidget) #部门管理系统按钮
        self.b_dept.setGeometry(QtCore.QRect(140, 230, 181, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.b_dept.setFont(font)
        self.b_dept.setObjectName("b_dept")
        self.b_dept.clicked.connect(self.dept)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 531, 121))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.b_emp = QtWidgets.QPushButton(self.centralwidget) #员工管理系统按钮
        self.b_emp.setGeometry(QtCore.QRect(470, 230, 181, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.b_emp.setFont(font)
        self.b_emp.setObjectName("b_emp")
        self.b_emp.clicked.connect(self.emp)
        self.b_cust = QtWidgets.QPushButton(self.centralwidget) #客户管理系统按钮
        self.b_cust.setGeometry(QtCore.QRect(140, 380, 181, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.b_cust.setFont(font)
        self.b_cust.setObjectName("b_cust")
        self.b_cust.clicked.connect(self.cust)
        self.b_sal = QtWidgets.QPushButton(self.centralwidget) #工资管理系统按钮
        self.b_sal.setGeometry(QtCore.QRect(470, 380, 181, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.b_sal.setFont(font)
        self.b_sal.setObjectName("b_sal")
        self.b_sal.clicked.connect(self.sal)
        self.b_close = QtWidgets.QPushButton(self.centralwidget) #退出按钮
        self.b_close.setGeometry(QtCore.QRect(310, 480, 181, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.b_close.setFont(font)
        self.b_close.setObjectName("b_close")
        self.b_close.clicked.connect(QCoreApplication.instance().quit)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "员工工资管理系统"))
        self.b_dept.setText(_translate("mainWindow", "部门管理系统"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">欢迎使用员工工资管理系统</p></body></html>"))
        self.b_emp.setText(_translate("mainWindow", "员工管理系统"))
        self.b_cust.setText(_translate("mainWindow", "客户管理系统"))
        self.b_sal.setText(_translate("mainWindow", "工资管理系统"))
        self.b_close.setText(_translate("mainWindow", "退出"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())