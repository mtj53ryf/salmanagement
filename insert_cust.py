from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义一个添加客户信息的函数
    def insert_cust(self):
        try:
            var_custno = self.custnoEdit.text()
            var_custname = self.custnameEdit.text()
            var_sex = self.sexEdit.text()
            var_birthdate = self.birthdateEdit.text()
            var_phone = self.phoneEdit.text()
            if "'" in var_custno or "'" in var_phone:
                self.messagelabel.setText("输入有误，请重新输入！")
            else:
                conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                c = conn.cursor()  # 获取cursor
                c.execute('insert into cust values({},{},{},{},{})'.format(var_custno, var_custname, var_sex, var_birthdate,var_phone))  # 使用cursor进行各种操作
                self.messagelabel.setText("")
                conn.commit()
                c.close()  # 关闭cursor
                conn.close()
                QApp = QCoreApplication.instance()
                QApp = quit()
        except cx_Oracle.DatabaseError:
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义添加客户信息界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 533)
        self.custnolabel = QtWidgets.QLabel(Dialog) #客户号标签
        self.custnolabel.setGeometry(QtCore.QRect(50, 60, 101, 31))
        self.custnolabel.setObjectName("custnolabel")
        self.custnoEdit = QtWidgets.QLineEdit(Dialog) #客户号输入框
        self.custnoEdit.setGeometry(QtCore.QRect(140, 60, 561, 31))
        self.custnoEdit.setObjectName("custnoEdit")
        self.b_ok = QtWidgets.QPushButton(Dialog) #确定按钮
        self.b_ok.setGeometry(QtCore.QRect(500, 470, 93, 28))
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.insert_cust)
        self.b_exit = QtWidgets.QPushButton(Dialog) #退出按钮
        self.b_exit.setGeometry(QtCore.QRect(620, 470, 93, 28))
        self.b_exit.setObjectName("b_exit")
        self.b_exit.clicked.connect(QCoreApplication.instance().quit)
        self.custnameEdit = QtWidgets.QLineEdit(Dialog) #客户姓名输入框
        self.custnameEdit.setGeometry(QtCore.QRect(140, 150, 561, 31))
        self.custnameEdit.setObjectName("custnameEdit")
        self.custnamelabel = QtWidgets.QLabel(Dialog) #客户姓名标签
        self.custnamelabel.setGeometry(QtCore.QRect(50, 150, 101, 31))
        self.custnamelabel.setObjectName("custnamelabel")
        self.sexlabel = QtWidgets.QLabel(Dialog) #性别标签
        self.sexlabel.setGeometry(QtCore.QRect(50, 240, 101, 31))
        self.sexlabel.setObjectName("sexlabel")
        self.sexEdit = QtWidgets.QLineEdit(Dialog) #性别输入框
        self.sexEdit.setGeometry(QtCore.QRect(140, 240, 561, 31))
        self.sexEdit.setObjectName("sexEdit")
        self.birthdatelabel = QtWidgets.QLabel(Dialog) #出生日期标签
        self.birthdatelabel.setGeometry(QtCore.QRect(50, 330, 101, 31))
        self.birthdatelabel.setObjectName("birthdatelabel")
        self.birthdateEdit = QtWidgets.QLineEdit(Dialog) #出生日期输入框
        self.birthdateEdit.setGeometry(QtCore.QRect(140, 330, 561, 31))
        self.birthdateEdit.setObjectName("birthdateEdit")
        self.phonelabel = QtWidgets.QLabel(Dialog) #电话标签
        self.phonelabel.setGeometry(QtCore.QRect(50, 420, 101, 31))
        self.phonelabel.setObjectName("phonelabel")
        self.phoneEdit = QtWidgets.QLineEdit(Dialog) #电话输入框
        self.phoneEdit.setGeometry(QtCore.QRect(140, 420, 561, 31))
        self.phoneEdit.setObjectName("phoneEdit")
        self.messagelabel = QtWidgets.QLabel(Dialog) #提示标签
        self.messagelabel.setGeometry(QtCore.QRect(280, 460, 161, 31))
        self.messagelabel.setObjectName("messagelabel")
        self.messagelabel.setStyleSheet("color:red")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加客户信息"))
        self.custnolabel.setText(_translate("Dialog", "客户号："))
        self.b_ok.setText(_translate("Dialog", "确定"))
        self.b_exit.setText(_translate("Dialog", "退出"))
        self.custnamelabel.setText(_translate("Dialog", "客户姓名："))
        self.sexlabel.setText(_translate("Dialog", "性别："))
        self.birthdatelabel.setText(_translate("Dialog", "出生日期："))
        self.phonelabel.setText(_translate("Dialog", "电话："))
        self.messagelabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())