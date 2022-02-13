from PyQt5 import QtCore, QtGui, QtWidgets
import os

from sqlalchemy import false, true

from account import Acount

class Ui_create_character_window(Acount):
    def setupUi(self, create_character_window,account,table):
        create_character_window.setObjectName("create_character_window")
        create_character_window.resize(193, 134)
        self.window=create_character_window
        self.account=account
        self.table=table
        self.filedir=os.path.join((os.path.abspath("."))+"\\account\\"+self.account.account_name)
        print(self.filedir)

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
        create_character_window.setWindowTitle(_translate("create_character_window", "新增角色"))
        self.create_charater_button.setText(_translate("create_character_window", "新增"))
        self.cancelButton.setText(_translate("create_character_window", "取消"))
        self.label_charater_name.setText(_translate("create_character_window", "角色名稱"))
        self.label_role.setText(_translate("create_character_window", "角色職業"))
        self.role_selection_box.setItemText(0, _translate("create_character_window", "英雄"))
        self.role_selection_box.setItemText(1, _translate("create_character_window", "聖騎士"))
        self.role_selection_box.setItemText(2, _translate("create_character_window", "黑騎士"))
        self.role_selection_box.setItemText(3, _translate("create_character_window", "冰雷"))
        self.role_selection_box.setItemText(4, _translate("create_character_window", "火毒"))
        self.role_selection_box.setItemText(5, _translate("create_character_window", "主教"))
        self.role_selection_box.setItemText(6, _translate("create_character_window", "箭神"))
        self.role_selection_box.setItemText(7, _translate("create_character_window", "神射手"))
        self.role_selection_box.setItemText(8, _translate("create_character_window", "開拓者"))
        self.role_selection_box.setItemText(9, _translate("create_character_window", "夜使者"))
        self.role_selection_box.setItemText(10, _translate("create_character_window", "暗影神偷"))
        self.role_selection_box.setItemText(11, _translate("create_character_window", "影武者"))
        self.role_selection_box.setItemText(12, _translate("create_character_window", "拳霸"))
        self.role_selection_box.setItemText(13, _translate("create_character_window", "槍神"))
        self.role_selection_box.setItemText(14, _translate("create_character_window", "重砲指揮官"))
        self.role_selection_box.setItemText(15, _translate("create_character_window", "墨玄"))
        self.role_selection_box.setItemText(16, _translate("create_character_window", "聖魂劍士"))
        self.role_selection_box.setItemText(17, _translate("create_character_window", "烈焰巫師"))
        self.role_selection_box.setItemText(18, _translate("create_character_window", "破風使者"))
        self.role_selection_box.setItemText(19, _translate("create_character_window", "暗影行者"))
        self.role_selection_box.setItemText(20, _translate("create_character_window", "閃雷悍將"))
        self.role_selection_box.setItemText(21, _translate("create_character_window", "米哈逸"))
        self.role_selection_box.setItemText(22, _translate("create_character_window", "爆拳槍神"))
        self.role_selection_box.setItemText(23, _translate("create_character_window", "煉獄巫師"))
        self.role_selection_box.setItemText(24, _translate("create_character_window", "狂暴獵人"))
        self.role_selection_box.setItemText(25, _translate("create_character_window", "傑諾"))
        self.role_selection_box.setItemText(26, _translate("create_character_window", "機甲戰神"))
        self.role_selection_box.setItemText(27, _translate("create_character_window", "狂狼勇士"))
        self.role_selection_box.setItemText(28, _translate("create_character_window", "龍魔導士"))
        self.role_selection_box.setItemText(29, _translate("create_character_window", "夜光"))
        self.role_selection_box.setItemText(30, _translate("create_character_window", "精靈遊俠"))
        self.role_selection_box.setItemText(31, _translate("create_character_window", "幻影俠盜"))
        self.role_selection_box.setItemText(32, _translate("create_character_window", "隱月"))
        self.role_selection_box.setItemText(33, _translate("create_character_window", "惡魔殺手"))
        self.role_selection_box.setItemText(34, _translate("create_character_window", "惡魔復仇者"))
        self.role_selection_box.setItemText(35, _translate("create_character_window", "凱薩"))
        self.role_selection_box.setItemText(36, _translate("create_character_window", "卡蒂娜"))
        self.role_selection_box.setItemText(37, _translate("create_character_window", "天使破壞者"))
        self.role_selection_box.setItemText(38, _translate("create_character_window", "劍豪"))
        self.role_selection_box.setItemText(39, _translate("create_character_window", "陰陽師"))
        self.role_selection_box.setItemText(40, _translate("create_character_window", "阿戴爾"))
        self.role_selection_box.setItemText(41, _translate("create_character_window", "伊利恩"))
        self.role_selection_box.setItemText(42, _translate("create_character_window", "亞克"))
        self.role_selection_box.setItemText(43, _translate("create_character_window", "神之子"))
        self.role_selection_box.setItemText(44, _translate("create_character_window", "虎影"))
        self.role_selection_box.setItemText(45, _translate("create_character_window", "幻獸師"))
        self.role_selection_box.setItemText(46, _translate("create_character_window", "菈菈"))

    def create(self):
        check=true
        rowPosition = self.table.rowCount()
        role=self.role_selection_box.currentText()
        with open(self.filedir+"\\character_list.txt",mode='a+',encoding='utf-8') as file:
            character_name=self.lineEdit.text()
            while true:    
                for line in file:
                    if character_name == line:
                        check=false
                if check:
                    file.write(character_name+" ")
                    file.write(role)
                    file.write("\n")
                    self.table.insertRow(rowPosition)
                    self.table.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(character_name))
                    self.table.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(role))
                    self.table.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(0))
                    break
        print(character_name)
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