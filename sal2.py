from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_MainWindow(object):
    #浏览工资信息
    def view_sal(self):
        conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')
        c = conn.cursor()  # 获取cursor
        x = c.execute('select * from sal')  # 使用cursor进行各种操作
        rs = x.fetchall()
        if (rs == []):
            self.textBrowser.setText("信息不存在")
        else:
            self.textBrowser.setText("工资号，员工号，工资时间，基本工资，请假扣除工资，处罚扣除工资，税收扣除工资，加班补贴工资，出差补贴工资，津贴工资，工资总额：\n"+str(rs))
        c.close()  # 关闭cursor
        conn.close()
    #查找工资信息
    def select_sal(self):
        os.system('python select_sal.py')
    #定义工资管理系统界面
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 520, 801, 81))
        self.groupBox.setObjectName("groupBox")
        self.b_view_sal = QtWidgets.QPushButton(self.groupBox) #浏览数据按钮
        self.b_view_sal.setGeometry(QtCore.QRect(220, 20, 93, 28))
        self.b_view_sal.setObjectName("b_view_sal")
        self.b_view_sal.clicked.connect(self.view_sal)
        self.b_select_sal = QtWidgets.QPushButton(self.groupBox) #查找数据按钮
        self.b_select_sal.setGeometry(QtCore.QRect(470, 20, 93, 28))
        self.b_select_sal.setObjectName("b_select_sal")
        self.b_select_sal.clicked.connect(self.select_sal)
        self.b_close_sal = QtWidgets.QPushButton(self.centralwidget) #退出按钮
        self.b_close_sal.setGeometry(QtCore.QRect(690, 20, 93, 28))
        self.b_close_sal.setObjectName("b_close_sal")
        self.b_close_sal.clicked.connect(QCoreApplication.instance().quit)
        self.label = QtWidgets.QLabel(self.centralwidget)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "工资管理系统"))
        self.groupBox.setTitle(_translate("MainWindow", "数据库操作"))
        self.b_view_sal.setText(_translate("MainWindow", "浏览数据"))
        self.b_select_sal.setText(_translate("MainWindow", "查找数据"))
        self.b_close_sal.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">工资管理系统</p></body></html>"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())