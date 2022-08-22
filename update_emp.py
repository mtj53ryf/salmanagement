from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义一个根据员工号修改对应员工信息的函数
    def update_emp(self):
        try:
            var_empno = self.empnoEdit.text()
            var_ename = self.enameEdit.text()
            var_sex = self.sexEdit.text()
            var_birthdate = self.birthdateEdit.text()
            var_job = self.jobEdit.text()
            var_sal = self.salEdit.text()
            var_hiredate = self.hiredateEdit.text()
            var_deptno = self.deptnoEdit.text()
            if "'" in var_empno or "'" in var_sal or "'" in var_deptno or var_ename=='' or var_sex=='' or var_birthdate=='' or var_job==''  or var_sal=='' or var_hiredate=='' or var_deptno=='':
                self.messagelabel.setText("输入有误，请重新输入！")
            else:
                conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                c = conn.cursor()  # 获取cursor
                x = c.execute('select * from emp where empno={}'.format(var_empno))  # 使用cursor进行各种操作
                rs = x.fetchall()
                if (rs == []):
                    self.messagelabel.setText("信息不存在")
                else:
                    c.execute('update emp set ename={},sex={},birthdate={},job={},sal={},hiredate={},deptno={} where empno={}'.format(var_ename,var_sex,var_birthdate,var_job,var_sal,var_hiredate,var_deptno,var_empno))  # 使用cursor进行各种操作
                    self.messagelabel.setText("")
                    conn.commit()
                    c.close()  # 关闭cursor
                    conn.close()
                    QApp = QCoreApplication.instance()
                    QApp = quit()
        except cx_Oracle.DatabaseError:
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义根据员工号修改对应员工信息界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 533)
        self.empnolabel = QtWidgets.QLabel(Dialog)  #员工号标签
        self.empnolabel.setGeometry(QtCore.QRect(50, 10, 101, 31))
        self.empnolabel.setObjectName("empnolabel")
        self.enameEdit = QtWidgets.QLineEdit(Dialog)  #员工姓名输入框
        self.enameEdit.setGeometry(QtCore.QRect(140, 60, 561, 31))
        self.enameEdit.setObjectName("enameEdit")
        self.b_ok = QtWidgets.QPushButton(Dialog) #确定按钮
        self.b_ok.setGeometry(QtCore.QRect(500, 470, 93, 28))
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.update_emp)
        self.b_exit = QtWidgets.QPushButton(Dialog) #退出按钮
        self.b_exit.setGeometry(QtCore.QRect(620, 470, 93, 28))
        self.b_exit.setObjectName("b_exit")
        self.b_exit.clicked.connect(QCoreApplication.instance().quit)
        self.sexEdit = QtWidgets.QLineEdit(Dialog)  #性别输入框
        self.sexEdit.setGeometry(QtCore.QRect(140, 110, 561, 31))
        self.sexEdit.setObjectName("sexEdit")
        self.enamelabel = QtWidgets.QLabel(Dialog)  #员工姓名标签
        self.enamelabel.setGeometry(QtCore.QRect(50, 60, 101, 31))
        self.enamelabel.setObjectName("enamelabel")
        self.sexlabel = QtWidgets.QLabel(Dialog)  #性别标签
        self.sexlabel.setGeometry(QtCore.QRect(50, 110, 101, 31))
        self.sexlabel.setObjectName("sexlabel")
        self.birthdateEdit = QtWidgets.QLineEdit(Dialog)  #出生日期输入框
        self.birthdateEdit.setGeometry(QtCore.QRect(140, 160, 561, 31))
        self.birthdateEdit.setObjectName("birthdateEdit")
        self.birthdatelabel = QtWidgets.QLabel(Dialog)  #出生日期标签
        self.birthdatelabel.setGeometry(QtCore.QRect(50, 160, 101, 31))
        self.birthdatelabel.setObjectName("birthdatelabel")
        self.jobEdit = QtWidgets.QLineEdit(Dialog)  #职业输入框
        self.jobEdit.setGeometry(QtCore.QRect(140, 210, 561, 31))
        self.jobEdit.setObjectName("jobEdit")
        self.joblabel = QtWidgets.QLabel(Dialog)  #职业标签
        self.joblabel.setGeometry(QtCore.QRect(50, 210, 101, 31))
        self.joblabel.setObjectName("joblabel")
        self.salEdit = QtWidgets.QLineEdit(Dialog)  #工资输入框
        self.salEdit.setGeometry(QtCore.QRect(140, 260, 561, 31))
        self.salEdit.setObjectName("salEdit")
        self.sallabel = QtWidgets.QLabel(Dialog)  #工资标签
        self.sallabel.setGeometry(QtCore.QRect(50, 260, 101, 31))
        self.sallabel.setObjectName("sallabel")
        self.hiredateEdit = QtWidgets.QLineEdit(Dialog)  #雇佣日期输入框
        self.hiredateEdit.setGeometry(QtCore.QRect(140, 310, 561, 31))
        self.hiredateEdit.setObjectName("hiredateEdit")
        self.empnoEdit = QtWidgets.QLineEdit(Dialog)  #员工号输入框
        self.empnoEdit.setGeometry(QtCore.QRect(140, 10, 561, 31))
        self.empnoEdit.setObjectName("empnoEdit")
        self.hiredatelabel = QtWidgets.QLabel(Dialog)  #雇佣日期标签
        self.hiredatelabel.setGeometry(QtCore.QRect(50, 310, 101, 31))
        self.hiredatelabel.setObjectName("hiredatelabel")
        self.deptnolabel = QtWidgets.QLabel(Dialog)  #部门号标签
        self.deptnolabel.setGeometry(QtCore.QRect(50, 360, 101, 31))
        self.deptnolabel.setObjectName("deptnolabel")
        self.deptnoEdit = QtWidgets.QLineEdit(Dialog)  #部门号输入框
        self.deptnoEdit.setGeometry(QtCore.QRect(140, 360, 561, 31))
        self.deptnoEdit.setObjectName("deptnoEdit")
        self.messagelabel = QtWidgets.QLabel(Dialog)  #提示标签
        self.messagelabel.setGeometry(QtCore.QRect(280, 400, 161, 31))
        self.messagelabel.setObjectName("messagelabel")
        self.messagelabel.setStyleSheet("color:red")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "根据员工号修改对应员工信息"))
        self.empnolabel.setText(_translate("Dialog", "员工号："))
        self.b_ok.setText(_translate("Dialog", "确定"))
        self.b_exit.setText(_translate("Dialog", "退出"))
        self.enamelabel.setText(_translate("Dialog", "员工姓名："))
        self.sexlabel.setText(_translate("Dialog", "性别："))
        self.birthdatelabel.setText(_translate("Dialog", "出生日期："))
        self.joblabel.setText(_translate("Dialog", "职业："))
        self.sallabel.setText(_translate("Dialog", "工资："))
        self.hiredatelabel.setText(_translate("Dialog", "雇佣日期："))
        self.deptnolabel.setText(_translate("Dialog", "部门号："))
        self.messagelabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())

