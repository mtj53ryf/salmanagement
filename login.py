from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义登录函数
    def login(self):
        var_name = self.nameEdit.text() #获取输入的用户名
        var_password = self.passwordEdit.text() #获取输入的密码
        if var_name=='system' and var_password=='980421': #判断用户名或密码是否正确或错误或为空
            self.messagelabel.setText("")
            os.system('python salmanagement.py')
            QApp=QCoreApplication.instance()
            QApp.quit()
        elif var_name=='master' and var_password=='802436':
            self.messagelabel.setText("")
            os.system('python salmanagement2.py')
            QApp=QCoreApplication.instance()
            QApp.quit()
        elif var_name=='' or var_password=='':
            self.messagelabel.setText("用户名或密码不能为空！")
        else:
            self.messagelabel.setText("用户名或密码错误！")
    #定义登录界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(590, 317)
        self.namelabel = QtWidgets.QLabel(Dialog) #用户名标签
        self.namelabel.setGeometry(QtCore.QRect(70, 70, 81, 31))
        self.namelabel.setObjectName("namelabel")
        self.passwordlabel = QtWidgets.QLabel(Dialog) #密码标签
        self.passwordlabel.setGeometry(QtCore.QRect(70, 130, 81, 31))
        self.passwordlabel.setObjectName("passwordlabel")
        self.nameEdit = QtWidgets.QLineEdit(Dialog) #用户名输入框
        self.nameEdit.setGeometry(QtCore.QRect(170, 70, 341, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(Dialog) #密码输入框
        self.passwordEdit.setGeometry(QtCore.QRect(170, 130, 341, 31))
        self.passwordEdit.setObjectName("passwordEdit")
        self.b_ok = QtWidgets.QPushButton(Dialog) #确认按钮
        self.b_ok.setGeometry(QtCore.QRect(180, 240, 93, 28))
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.login)
        self.b_close = QtWidgets.QPushButton(Dialog) #取消按钮
        self.b_close.setGeometry(QtCore.QRect(320, 240, 93, 28))
        self.b_close.setObjectName("b_close")
        self.b_close.clicked.connect(QCoreApplication.instance().quit)
        self.messagelabel = QtWidgets.QLabel(Dialog) #提示标签
        self.messagelabel.setGeometry(QtCore.QRect(210, 180, 161, 31))
        self.messagelabel.setObjectName("messagelabel")
        self.messagelabel.setStyleSheet("color:red")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.namelabel.setText(_translate("Dialog", "用户名："))
        self.passwordlabel.setText(_translate("Dialog", "密码："))
        self.b_ok.setText(_translate("Dialog", "确定"))
        self.b_close.setText(_translate("Dialog", "取消"))
        self.messagelabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())