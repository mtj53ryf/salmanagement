from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cx_Oracle
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QCoreApplication

class Ui_Dialog(object):
    #定义一个显示工资税信息的函数
    def show_taxsal(self):
        try:
            var_basedsal = self.basedsalEdit.text()
            salary = eval(var_basedsal) - 3500
            if salary > 80000:
                cal_salary = salary * 0.45 - 13504
            elif salary > 55000:
                cal_salary = salary * 0.35 - 5505
            elif salary > 35000:
                cal_salary = salary * 0.3 - 2755
            elif salary > 9000:
                cal_salary = salary * 0.25 - 1005
            elif salary > 4500:
                cal_salary = salary * 0.2 - 555
            elif salary > 1500:
                cal_salary = salary * 0.1 - 105
            else:
                cal_salary = salary * 0.03
            var_taxsal=round(cal_salary,2)
            if var_taxsal<0:
                var_taxsal=0
            if "'" in var_basedsal:
                self.taxsalEdit.setText("")
                self.messagelabel.setText("输入有误，请重新输入！")
            else:
                self.taxsalEdit.setText(str(var_taxsal))
                self.messagelabel.setText("")
        except SyntaxError:
            self.totalsalEdit.setText("")
            self.messagelabel.setText("输入有误，请重新输入！")
        except TypeError:
            self.totalsalEdit.setText("")
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义一个显示工资总额信息的函数
    def show_totalsal(self):
        try:
            var_basedsal = self.basedsalEdit.text()
            var_deductionsal = self.deductionsalEdit.text()
            var_penaltysal = self.penaltysalEdit.text()
            var_taxsal = self.taxsalEdit.text()
            var_latesal = self.latesalEdit.text()
            var_travelsal = self.travelsalEdit.text()
            var_titlesal = self.titlesalEdit.text()
            var_totalsal = eval(var_basedsal)-eval(var_deductionsal)-eval(var_penaltysal)-eval(var_taxsal)+eval(var_latesal)+eval(var_travelsal)+eval(var_titlesal)
            if "'" in var_basedsal or "'" in var_deductionsal or "'" in var_penaltysal or "'" in var_taxsal or "'" in var_latesal or "'" in var_travelsal or "'" in var_titlesal:
                self.totalsalEdit.setText("")
                self.messagelabel.setText("输入有误，请重新输入！")
            else:
                self.totalsalEdit.setText(str(var_totalsal))
                self.messagelabel.setText("")
        except SyntaxError:
            self.totalsalEdit.setText("")
            self.messagelabel.setText("输入有误，请重新输入！")
        except TypeError:
            self.totalsalEdit.setText("")
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义一个添加工资信息的函数
    def insert_sal(self):
        try:
            var_salno = self.salnoEdit.text()
            var_empno = self.empnoEdit.text()
            var_saltime = self.saltimeEdit.text()
            var_basedsal = self.basedsalEdit.text()
            var_deductionsal = self.deductionsalEdit.text()
            var_penaltysal = self.penaltysalEdit.text()
            var_taxsal = self.taxsalEdit.text()
            var_latesal = self.latesalEdit.text()
            var_travelsal = self.travelsalEdit.text()
            var_titlesal = self.titlesalEdit.text()
            var_totalsal = eval(var_basedsal) - eval(var_deductionsal) - eval(var_penaltysal) - eval(var_taxsal) + eval(var_latesal) + eval(var_travelsal) + eval(var_titlesal)
            if "'" in var_salno or "'" in var_empno or "'" in var_basedsal or "'" in var_deductionsal or "'" in var_penaltysal or "'" in var_taxsal or "'" in var_latesal or "'" in var_travelsal or "'" in var_titlesal:
                self.messagelabel.setText("输入有误，请重新输入！")
            else:
                conn = cx_Oracle.connect('system/bc1234567897@localhost:1521/orcl')  # 连接数据库
                c = conn.cursor()  # 获取cursor
                c.execute('insert into sal values({},{},{},{},{},{},{},{},{},{},{})'.format(var_salno, var_empno, var_saltime,var_basedsal, var_deductionsal,var_penaltysal, var_taxsal,var_latesal,var_travelsal,var_titlesal,var_totalsal))  # 使用cursor进行各种操作
                self.messagelabel.setText("")
                conn.commit()
                c.close()  # 关闭cursor
                conn.close()
                QApp = QCoreApplication.instance()
                QApp = quit()
        except cx_Oracle.DatabaseError:
            self.messagelabel.setText("输入有误，请重新输入！")
        except SyntaxError:
            self.messagelabel.setText("输入有误，请重新输入！")
        except TypeError:
            self.messagelabel.setText("输入有误，请重新输入！")
    #定义添加工资信息界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 812)
        self.salnolabel = QtWidgets.QLabel(Dialog) #工资号标签
        self.salnolabel.setGeometry(QtCore.QRect(50, 60, 101, 31))
        self.salnolabel.setObjectName("salnolabel")
        self.salnoEdit = QtWidgets.QLineEdit(Dialog) #工资号输入框
        self.salnoEdit.setGeometry(QtCore.QRect(140, 60, 561, 31))
        self.salnoEdit.setObjectName("salnoEdit")
        self.b_ok = QtWidgets.QPushButton(Dialog) #确定按钮
        self.b_ok.setGeometry(QtCore.QRect(500, 730, 93, 28))
        self.b_ok.setObjectName("b_ok")
        self.b_ok.clicked.connect(self.insert_sal)
        self.b_exit = QtWidgets.QPushButton(Dialog) #退出按钮
        self.b_exit.setGeometry(QtCore.QRect(620, 730, 93, 28))
        self.b_exit.setObjectName("b_exit")
        self.b_exit.clicked.connect(QCoreApplication.instance().quit)
        self.b_showtotalsal = QtWidgets.QPushButton(Dialog) #显示总工资按钮
        self.b_showtotalsal.setGeometry(QtCore.QRect(380, 730, 93, 28))
        self.b_showtotalsal.setObjectName("b_showtotalsal")
        self.b_showtotalsal.clicked.connect(self.show_totalsal)
        self.b_showtaxsal = QtWidgets.QPushButton(Dialog) #显示工资税按钮
        self.b_showtaxsal.setGeometry(QtCore.QRect(260, 730, 93, 28))
        self.b_showtaxsal.setObjectName("b_showtaxsal")
        self.b_showtaxsal.clicked.connect(self.show_taxsal)
        self.empnoEdit = QtWidgets.QLineEdit(Dialog) #员工号输入框
        self.empnoEdit.setGeometry(QtCore.QRect(140, 120, 561, 31))
        self.empnoEdit.setObjectName("empnoEdit")
        self.empnolabel = QtWidgets.QLabel(Dialog) #员工号标签
        self.empnolabel.setGeometry(QtCore.QRect(50, 120, 101, 31))
        self.empnolabel.setObjectName("empnolabel")
        self.saltimelabel = QtWidgets.QLabel(Dialog) #工资时间标签
        self.saltimelabel.setGeometry(QtCore.QRect(50, 180, 101, 31))
        self.saltimelabel.setObjectName("saltimelabel")
        self.saltimeEdit = QtWidgets.QLineEdit(Dialog) #工资时间输入框
        self.saltimeEdit.setGeometry(QtCore.QRect(140, 180, 561, 31))
        self.saltimeEdit.setObjectName("saltimeEdit")
        self.basedsallabel = QtWidgets.QLabel(Dialog) #基本工资标签
        self.basedsallabel.setGeometry(QtCore.QRect(50, 240, 101, 31))
        self.basedsallabel.setObjectName("basedsallabel")
        self.basedsalEdit = QtWidgets.QLineEdit(Dialog) #基本工资输入框
        self.basedsalEdit.setGeometry(QtCore.QRect(140, 240, 561, 31))
        self.basedsalEdit.setObjectName("basedsalEdit")
        self.deductionsallabel = QtWidgets.QLabel(Dialog) #请假扣除工资标签
        self.deductionsallabel.setGeometry(QtCore.QRect(30, 300, 101, 31))
        self.deductionsallabel.setObjectName("deductionsallabel")
        self.deductionsalEdit = QtWidgets.QLineEdit(Dialog) #请假扣除工资输入框
        self.deductionsalEdit.setGeometry(QtCore.QRect(140, 300, 561, 31))
        self.deductionsalEdit.setObjectName("deductionsalEdit")
        self.penaltysallabel = QtWidgets.QLabel(Dialog) #处罚扣除工资标签
        self.penaltysallabel.setGeometry(QtCore.QRect(30, 360, 101, 31))
        self.penaltysallabel.setObjectName("penaltysallabel")
        self.penaltysalEdit = QtWidgets.QLineEdit(Dialog) #处罚扣除工资输入框
        self.penaltysalEdit.setGeometry(QtCore.QRect(140, 360, 561, 31))
        self.penaltysalEdit.setObjectName("penaltysalEdit")
        self.taxsallabel = QtWidgets.QLabel(Dialog) #税收扣除工资标签
        self.taxsallabel.setGeometry(QtCore.QRect(30, 420, 101, 31))
        self.taxsallabel.setObjectName("taxsallabel")
        self.taxsalEdit = QtWidgets.QLineEdit(Dialog) #税收扣除工资输入框
        self.taxsalEdit.setGeometry(QtCore.QRect(140, 420, 561, 31))
        self.taxsalEdit.setObjectName("taxsalEdit")
        self.latesallabel = QtWidgets.QLabel(Dialog) #加班补贴工资标签
        self.latesallabel.setGeometry(QtCore.QRect(30, 480, 101, 31))
        self.latesallabel.setObjectName("latesallabel")
        self.latesalEdit = QtWidgets.QLineEdit(Dialog) #加班补贴工资输入框
        self.latesalEdit.setGeometry(QtCore.QRect(140, 480, 561, 31))
        self.latesalEdit.setObjectName("latesalEdit")
        self.travelsallabel = QtWidgets.QLabel(Dialog) #出差补贴工资标签
        self.travelsallabel.setGeometry(QtCore.QRect(30, 540, 101, 31))
        self.travelsallabel.setObjectName("travelsallabel")
        self.travelsalEdit = QtWidgets.QLineEdit(Dialog) #出差补贴工资输入框
        self.travelsalEdit.setGeometry(QtCore.QRect(140, 540, 561, 31))
        self.travelsalEdit.setObjectName("travelsalEdit")
        self.titlesallabel = QtWidgets.QLabel(Dialog) #津贴工资标签
        self.titlesallabel.setGeometry(QtCore.QRect(50, 600, 101, 31))
        self.titlesallabel.setObjectName("titlesallabel")
        self.titlesalEdit = QtWidgets.QLineEdit(Dialog) #津贴工资输入框
        self.titlesalEdit.setGeometry(QtCore.QRect(140, 600, 561, 31))
        self.titlesalEdit.setObjectName("titlesalEdit")
        self.totalsallabel = QtWidgets.QLabel(Dialog) #工资总额标签
        self.totalsallabel.setGeometry(QtCore.QRect(50, 660, 101, 31))
        self.totalsallabel.setObjectName("totalsallabel")
        self.totalsalEdit = QtWidgets.QLineEdit(Dialog) #工资总额输入框
        self.totalsalEdit.setGeometry(QtCore.QRect(140, 660, 561, 31))
        self.totalsalEdit.setObjectName("totalsalEdit")
        self.messagelabel = QtWidgets.QLabel(Dialog) #提示标签
        self.messagelabel.setGeometry(QtCore.QRect(280, 690, 161, 31))
        self.messagelabel.setObjectName("messagelabel")
        self.messagelabel.setStyleSheet("color:red")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加工资信息"))
        self.salnolabel.setText(_translate("Dialog", "工资号："))
        self.b_ok.setText(_translate("Dialog", "确定"))
        self.b_exit.setText(_translate("Dialog", "退出"))
        self.empnolabel.setText(_translate("Dialog", "员工号："))
        self.saltimelabel.setText(_translate("Dialog", "工资时间："))
        self.basedsallabel.setText(_translate("Dialog", "基本工资："))
        self.deductionsallabel.setText(_translate("Dialog", "请假扣除工资："))
        self.penaltysallabel.setText(_translate("Dialog", "处罚扣除工资："))
        self.b_showtotalsal.setText(_translate("Dialog", "显示总工资"))
        self.b_showtaxsal.setText(_translate("Dialog", "显示工资税"))
        self.messagelabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.taxsallabel.setText(_translate("Dialog", "税收扣除工资："))
        self.latesallabel.setText(_translate("Dialog", "加班补贴工资："))
        self.travelsallabel.setText(_translate("Dialog", "出差补贴工资："))
        self.titlesallabel.setText(_translate("Dialog", "津贴工资："))
        self.totalsallabel.setText(_translate("Dialog", "工资总额："))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(m)
    m.show()
    sys.exit(app.exec_())