from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os
from account import Account
import pickle


class Ui_createNewAccount(Account):
    def setupUi(self, createNewAccountWindow):
        createNewAccountWindow.setObjectName("createNewAccountWindow")
        createNewAccountWindow.resize(232, 93)
        self.centralwidget = QtWidgets.QWidget(createNewAccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.window=createNewAccountWindow
        
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
        
        createNewAccountWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(createNewAccountWindow)
        self.statusbar.setObjectName("statusbar")
        createNewAccountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(createNewAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(createNewAccountWindow)

        self.createAccount.clicked.connect(self.create)
        self.cancelButton.clicked.connect(self.cancel)

    def retranslateUi(self, createNewAccountWindow):
        _translate = QtCore.QCoreApplication.translate
        createNewAccountWindow.setWindowTitle(_translate("createNewAccountWindow", "新增帳號"))
        self.label.setText(_translate("createNewAccountWindow", "帳號名稱"))
        self.createAccount.setText(_translate("createNewAccountWindow", "創立"))
        self.cancelButton.setText(_translate("createNewAccountWindow", "取消"))
    
    def create(self):
        accountname=self.lineEdit.text()
        if accountname=="":
            return
        
        self.fileDir=os.path.join((os.path.abspath("."))+"\\data\\")
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
        
        accounts=self.loadall('account_data.pkl')
        print(accounts)
        for accountData in accounts:
            if accountname==accountData.account_name:
                QMessageBox.about(self.window,"錯誤","已有此帳號")
                return    
        
        account=Account()
        account.create(accountname)
        account.fileDir=self.fileDir+account.account_name
        with open(self.fileDir+'account_data.pkl','ab') as file:
            pickle.dump(account,file,pickle.HIGHEST_PROTOCOL)
        self.fileDir=self.fileDir+account.account_name
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
        with open(self.fileDir+'\\account_characters.pkl','ab') as file:
            pass
        
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