from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义一个根据客户号删除客户信息的函数
    def delete_cust(self):
        try:
            var_custno = self.custnoEdit.text()
            if "'" in var_custno:
                self.messagelabel.setText("输入有误，请重新输入！")
            else:
                conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                c = conn.cursor()  # 获取cursor
                x = c.execute('select * from cust where custno={}'.format(var_custno))  # 使用cursor进行各种操作
                rs = x.fetchall()
                if (rs == []):
                    self.messagelabel.setText("信息不存在")
                else:
                    c.execute('delete from cust where custno={}'.format(var_custno))  # 使用cursor进行各种操作
                    self.messagelabel.setText("")
                    conn.commit()
                    c.close()  # 关闭cursor
                    conn.close()
                    QApp = QCoreApplication.instance()
                    QApp = quit()
        except cx_Oracle.DatabaseError:
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义根据客户号删除客户信息界面
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
        self.b_ok.clicked.connect(self.delete_cust)
        self.b_exit = QtWidgets.QPushButton(Dialog) #退出按钮
        self.b_exit.setGeometry(QtCore.QRect(620, 470, 93, 28))
        self.b_exit.setObjectName("b_exit")
        self.b_exit.clicked.connect(QCoreApplication.instance().quit)
        self.messagelabel = QtWidgets.QLabel(Dialog) #提示标签
        self.messagelabel.setGeometry(QtCore.QRect(280, 200, 161, 31))
        self.messagelabel.setObjectName("messagelabel")
        self.messagelabel.setStyleSheet("color:red")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "根据客户号删除对应客户信息"))
        self.custnolabel.setText(_translate("Dialog", "客户号："))
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

