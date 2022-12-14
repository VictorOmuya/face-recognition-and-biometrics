# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'police_reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QMessageBox
import reg

class Ui_admin(object):
    
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    
    def browse(self):
        fname = QFileDialog.getOpenFileName()
        self.imagePath = fname[0]
        
        pixmap = QPixmap(self.imagePath)
        self.lbl_img.setPixmap(QPixmap(pixmap))
        self.lbl_img.setScaledContents(True)
    
    def regist(self):
        try:
        
            name = self.lineEdit.text().lower()
            describe = self.plainTextEdit.toPlainText()
            
            if name != '' or describe != '' :
                
                res = reg.registeration(self.imagePath, name, describe)
                
                if res == 'registration successful':
                    self.messagebox("police", "registration successsful!")
                else:
                    self.messagebox("police", "guess the name entered already exists")
            else:
                self.messagebox("police", "kindly supply values for the fields above")
            
        except:
            self.messagebox("police", "a problem occured. make sure you have a valid image")
    
    
    def setupUi(self, admin):
        admin.setObjectName("admin")
        admin.resize(661, 226)
        self.lblback = QtWidgets.QLabel(admin)
        self.lblback.setGeometry(QtCore.QRect(0, 0, 401, 161))
        self.lblback.setText("")
        self.lblback.setObjectName("lblback")
        
        self.lbl_img = QtWidgets.QLabel(admin)
        self.lbl_img.setGeometry(QtCore.QRect(10, 60, 161, 100))
        self.lbl_img.setText("")
        self.lbl_img.setObjectName("lbl_img")
        
        self.pushButton = QtWidgets.QPushButton(admin)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse)
        
        self.lineEdit = QtWidgets.QLineEdit(admin)
        self.lineEdit.setGeometry(QtCore.QRect(190, 8, 240, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(admin)
        self.plainTextEdit.setGeometry(QtCore.QRect(189, 40, 461, 151))
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.btn_reg = QtWidgets.QPushButton(admin)
        self.btn_reg.setGeometry(QtCore.QRect(600, 200, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reg.setFont(font)
        self.btn_reg.setObjectName("btn_reg")
        self.btn_reg.clicked.connect(self.regist)
        
        self.label = QtWidgets.QLabel(admin)
        self.label.setGeometry(QtCore.QRect(0, -8, 661, 41))
        self.label.setStyleSheet("background-color: rgb(170, 0, 127);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(admin)
        self.label_2.setGeometry(QtCore.QRect(0, 196, 661, 31))
        self.label_2.setStyleSheet("background-color: rgb(170, 0, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.lblback.raise_()
        self.lbl_img.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.plainTextEdit.raise_()
        self.btn_reg.raise_()

        self.retranslateUi(admin)
        QtCore.QMetaObject.connectSlotsByName(admin)

    def retranslateUi(self, admin):
        _translate = QtCore.QCoreApplication.translate
        admin.setWindowTitle(_translate("admin", "admin"))
        self.pushButton.setText(_translate("admin", "browse image"))
        self.lineEdit.setPlaceholderText(_translate("admin", "Name"))
        self.plainTextEdit.setPlaceholderText(_translate("admin", "Give a description of this person"))
        self.btn_reg.setText(_translate("admin", "SAVE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin = QtWidgets.QDialog()
    ui = Ui_admin()
    ui.setupUi(admin)
    admin.show()
    sys.exit(app.exec_())
