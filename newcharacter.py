from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pickle
from sqlalchemy import false, true

from account import Account
from character import Character

class Ui_create_character_window(Account):
    def setupUi(self, create_character_window,account,table):
        create_character_window.setObjectName("create_character_window")
        create_character_window.resize(193, 134)
        self.window=create_character_window
        self.account=account
        self.table=table

        self.centralwidget = QtWidgets.QWidget(create_character_window)
        self.centralwidget.setObjectName("centralwidget")
        
        self.create_charater_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_charater_button.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.create_charater_button.setObjectName("create_charater_button")
        
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        
        self.label_charater_name = QtWidgets.QLabel(self.centralwidget)
        self.label_charater_name.setGeometry(QtCore.QRect(10, 20, 47, 12))
        self.label_charater_name.setObjectName("label_charater_name")
        
        self.label_role = QtWidgets.QLabel(self.centralwidget)
        self.label_role.setGeometry(QtCore.QRect(10, 50, 47, 12))
        self.label_role.setObjectName("label_role")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.role_selection_box = QtWidgets.QComboBox(self.centralwidget)
        self.role_selection_box.setGeometry(QtCore.QRect(70, 50, 111, 21))
        self.role_selection_box.setObjectName("role_selection_box")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        self.role_selection_box.addItem("")
        create_character_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(create_character_window)
        self.statusbar.setObjectName("statusbar")
        create_character_window.setStatusBar(self.statusbar)

        self.retranslateUi(create_character_window)
        QtCore.QMetaObject.connectSlotsByName(create_character_window)

        self.cancelButton.clicked.connect(self.cancel)
        self.create_charater_button.clicked.connect(self.create)

    def retranslateUi(self, create_character_window):
        _translate = QtCore.QCoreApplication.translate
        create_character_window.setWindowTitle(_translate("create_character_window", "????????????"))
        self.create_charater_button.setText(_translate("create_character_window", "??????"))
        self.cancelButton.setText(_translate("create_character_window", "??????"))
        self.label_charater_name.setText(_translate("create_character_window", "????????????"))
        self.label_role.setText(_translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(0, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(1, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(2, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(3, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(4, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(5, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(6, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(7, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(8, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(9, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(10, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(11, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(12, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(13, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(14, _translate("create_character_window", "???????????????"))
        self.role_selection_box.setItemText(15, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(16, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(17, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(18, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(19, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(20, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(21, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(22, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(23, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(24, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(25, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(26, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(27, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(28, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(29, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(30, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(31, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(32, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(33, _translate("create_character_window", "????????????"))
        self.role_selection_box.setItemText(34, _translate("create_character_window", "???????????????"))
        self.role_selection_box.setItemText(35, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(36, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(37, _translate("create_character_window", "???????????????"))
        self.role_selection_box.setItemText(38, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(39, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(40, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(41, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(42, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(43, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(44, _translate("create_character_window", "??????"))
        self.role_selection_box.setItemText(45, _translate("create_character_window", "?????????"))
        self.role_selection_box.setItemText(46, _translate("create_character_window", "??????"))

    def create(self):
        check=true
        rowPosition = self.table.rowCount()
        role=self.role_selection_box.currentText()

        character_name=self.lineEdit.text()
        if character_name=="":
            return
        
        new_character=Character(character_name,role)
        self.account.addCharacter(new_character)
        print(self.account.fileDir)
        with open(self.account.fileDir+'\\account_characters.pkl','ab') as file:
            pickle.dump(new_character,file,pickle.HIGHEST_PROTOCOL)

        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(new_character.name))
        self.table.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(new_character.role))
        self.table.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(new_character.income))

        self.window.close()
    
    def cancel(self):
        self.window.close()


""" if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_character_window = QtWidgets.QMainWindow()
    ui = Ui_create_character_window()
    ui.setupUi(create_character_window)
    create_character_window.show()
    sys.exit(app.exec_())
 """