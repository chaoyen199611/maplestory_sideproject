from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from newaccount import Ui_createNewAccount
from accountlist import Ui_accountlist
import sys


class Ui_FrontWindow(object):
    def setupUi(self, FrontWindow):
        FrontWindow.setObjectName("MainWindow")
        FrontWindow.resize(800, 400)
        self.mainwindow=FrontWindow
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Program Files (x86)/Gamania/MapleStory/MapleStory.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        
        FrontWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.newAccountButton = QtWidgets.QPushButton(self.centralwidget)
        self.newAccountButton.setGeometry(QtCore.QRect(315, 330, 80, 30))    
        self.newAccountButton.setFont(font)
        self.newAccountButton.setAutoDefault(False)
        self.newAccountButton.setObjectName("newAccountButton")
       
        self.loadAccountButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadAccountButton.setGeometry(QtCore.QRect(405, 330, 80, 30))
        self.loadAccountButton.setFont(font)
        self.loadAccountButton.setObjectName("loadAccountButton")
        
        FrontWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(FrontWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        FrontWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(FrontWindow)
        self.statusbar.setObjectName("statusbar")
        FrontWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FrontWindow)
        QtCore.QMetaObject.connectSlotsByName(FrontWindow)

        
        self.newAccountButton.clicked.connect(self.create_account)
        self.loadAccountButton.clicked.connect(self.load_account)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "新楓之谷記帳"))
        self.newAccountButton.setText(_translate("MainWindow", "新帳號"))
        self.loadAccountButton.setText(_translate("MainWindow", "開啟帳號"))

    def create_account(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_createNewAccount()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def load_account(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_accountlist()
        self.ui.setupUi(self.window,self.mainwindow)
        self.window.show()
    
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    FrontPage = QtWidgets.QMainWindow()
    ui = Ui_FrontWindow()
    ui.setupUi(FrontPage)
    FrontPage.show()
    sys.exit(app.exec_())