from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os
from account import Account
import pickle

from accountlist import Ui_accountlist



class Ui_createNewAccount(Ui_accountlist):
    def setupUi(self, createNewAccount):
        createNewAccount.setObjectName("createNewAccount")
        createNewAccount.resize(232, 93)
        self.centralwidget = QtWidgets.QWidget(createNewAccount)
        self.centralwidget.setObjectName("centralwidget")
        self.window=createNewAccount
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 130, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label.setObjectName("label")
        
        self.createAccount = QtWidgets.QPushButton(self.centralwidget)
        self.createAccount.setGeometry(QtCore.QRect(30, 40, 75, 23))
        self.createAccount.setObjectName("createAccount")
        
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(110, 40, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        
        createNewAccount.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(createNewAccount)
        self.statusbar.setObjectName("statusbar")
        createNewAccount.setStatusBar(self.statusbar)

        self.retranslateUi(createNewAccount)
        QtCore.QMetaObject.connectSlotsByName(createNewAccount)

        self.createAccount.clicked.connect(self.create)
        self.cancelButton.clicked.connect(self.cancel)

    def retranslateUi(self, createNewAccount):
        _translate = QtCore.QCoreApplication.translate
        createNewAccount.setWindowTitle(_translate("createNewAccount", "新增帳號"))
        self.label.setText(_translate("createNewAccount", "帳號名稱"))
        self.createAccount.setText(_translate("createNewAccount", "創立"))
        self.cancelButton.setText(_translate("createNewAccount", "取消"))
    
    def create(self):
        accountname=self.lineEdit.text()
        if accountname=="":
            return
        account=Account(accountname)
        self.fileDir=os.path.join((os.path.abspath("."))+"\\data\\")
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
        
        accounts=self.loadall('account_data.pkl')
        print(accounts)
        for accountData in accounts:
            if accountname==accountData.account_name:
                QMessageBox.about(self.window,"錯誤","已有此帳號")
                return    
        
        with open(self.fileDir+'account_data.pkl','ab') as file:
            pickle.dump(account,file,pickle.HIGHEST_PROTOCOL)
        self.fileDir=self.fileDir+account.account_name
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
        self.window.close()


    def cancel(self):
        self.window.close()


""" if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createNewAccount = QtWidgets.QMainWindow()
    ui = Ui_createNewAccount()
    ui.setupUi(createNewAccount)
    createNewAccount.show()
    sys.exit(app.exec_())
 """