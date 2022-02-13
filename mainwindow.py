from tokenize import Double
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from decimal import Decimal
from account import Acount
from newcharacter import Ui_create_character_window


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,selected_account):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 499)
        self.window=MainWindow
        self.account=selected_account
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 470))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/main_background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 211, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(240, 10, 181, 151))
        self.groupBox.setTabletTracking(False)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.incomeButton = QPushButton(self.groupBox)
        self.incomeButton.setGeometry(QtCore.QRect(20, 110, 75, 20))
        self.incomeButton.setObjectName("incomeButton")

        self.expenseButton=QPushButton(self.groupBox)
        self.expenseButton.setGeometry(QtCore.QRect(100,110,75,20))
        self.expenseButton.setObjectName("expenseButton")

        self.create_charater_button=QPushButton(MainWindow)
        self.create_charater_button.setGeometry(QtCore.QRect(240, 200, 60, 25))
        self.create_charater_button.setObjectName("label_create_charater_button")

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 47, 12))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 47, 20))
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(240, 200, 75, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionNew_Accouont = QAction(MainWindow)
        self.actionNew_Accouont.setObjectName("actionNew_Accouont")
        self.actiona = QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.menu.addAction(self.actionNew_Accouont)
        self.menu.addAction(self.actiona)
        self.menubar.addAction(self.menu.menuAction())

        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(240, 210, 321, 251))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.characterlist = QTableWidget(self.frame)
        self.characterlist.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.characterlist.setSelectionMode(QAbstractItemView.SingleSelection)
        self.characterlist.setGeometry(QtCore.QRect(10, 10, 301, 192))
        self.characterlist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.characterlist.setObjectName("characterlist")
        self.characterlist.setColumnCount(3)
        self.characterlist.setRowCount(0)
        
        item = QTableWidgetItem()
        self.characterlist.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.characterlist.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.characterlist.setHorizontalHeaderItem(2, item)
        
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 210, 91, 31))
        self.pushButton.setObjectName("pushButton")
        
        self.selectButton = QPushButton(self.frame)
        self.selectButton.setGeometry(QtCore.QRect(120, 210, 91, 31))
        self.selectButton.setObjectName("selectButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.incomeButton.clicked.connect(self.income)
        self.create_charater_button.clicked.connect(self.create_character)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.account.account_name+"的記帳本"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "品項"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "價格"))
        self.groupBox.setTitle(_translate("MainWindow", "新增花費/收入"))
        self.incomeButton.setText(_translate("MainWindow", "收入"))
        self.expenseButton.setText(_translate("MainWindow", "支出"))
        self.label_2.setText(_translate("MainWindow", "品項"))
        self.label_3.setText(_translate("MainWindow", "價格"))
        self.create_charater_button.setText(_translate("MainWindow", "建立角色"))
        self.menu.setTitle(_translate("MainWindow", "帳號"))
        self.actionNew_Accouont.setText(_translate("MainWindow", "新增帳號"))
        self.actiona.setText(_translate("MainWindow", "切換帳號"))
        item = self.characterlist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "角色名稱"))
        item = self.characterlist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "職業"))
        item = self.characterlist.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "收益"))
        self.pushButton.setText(_translate("MainWindow", "刪除角色"))
        self.selectButton.setText(_translate("MainWindow", "選擇角色"))

    def create_character(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_create_character_window()
        self.ui.setupUi(self.window,self.account,self.characterlist)
        self.window.show()

    def show_characterlist(self):
        self.characterlist=self.account.character

    def income(self):
        rowPosition = self.characterlist.rowCount()
        if self.lineEdit.text()!="" and self.lineEdit_2.text()!="":
            self.characterlist.insertRow(rowPosition)
            self.characterlist.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(self.lineEdit.text()))
            self.characterlist.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(self.lineEdit_2.text()))
        else:
            pass



""" if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) """
