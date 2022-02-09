from PyQt5 import QtCore, QtGui, QtWidgets
import os
from os import walk
from mainwindow import Ui_MainWindow

class Ui_accountlist(object):
    def setupUi(self, accountlist,mainwindow):
        accountlist.setObjectName("accountlist")
        accountlist.resize(210, 300)
        self.centralwidget = QtWidgets.QWidget(accountlist)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 161, 191))
        self.window=accountlist
        self.mainwindow=mainwindow
        font = QtGui.QFont()
        font.setUnderline(False)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 47, 12))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        accountlist.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(accountlist)
        self.statusbar.setObjectName("statusbar")

        self.select_account=""
        accountlist.setStatusBar(self.statusbar)

        self.fileDir=os.path.join((os.path.abspath("."))+"\\account\\")
        if not os.path.exists(self.fileDir):
            os.makedirs(self.fileDir)
        f = []
        for (dirpath, dirnames, filenames) in walk(self.fileDir):
            print(dirnames)
            f.extend(dirnames)
            break
        self.listWidget.addItems(f)
        self.retranslateUi(accountlist)
        QtCore.QMetaObject.connectSlotsByName(accountlist)
        self.pushButton.clicked.connect(self.select)
        self.pushButton_2.clicked.connect(self.cancel)

    def retranslateUi(self, accountlist):
        _translate = QtCore.QCoreApplication.translate
        accountlist.setWindowTitle(_translate("accountlist", "帳號"))
        self.label.setText(_translate("accountlist", "帳號列表"))
        self.pushButton.setText(_translate("accountlist", "選擇"))
        self.pushButton_2.setText(_translate("accountlist", "取消"))

    def cancel(self):
        self.window.close()

    def select(self):
        self.select_account=self.listWidget.currentItem().text()
        self.window.close()
        self.mainwindow.close()
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window,self.select_account)
        self.window.show()

""" if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    accountlist = QtWidgets.QMainWindow()
    ui = Ui_accountlist()
    ui.setupUi(accountlist)
    accountlist.show()
    sys.exit(app.exec_()) """
