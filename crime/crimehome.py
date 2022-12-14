# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pyQts\crimehome.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from crime import *

class Ui_crime(object):
    
    def cont(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Crime()
        self.ui.setupUi(self.window)
        self.window.show()
        crime.hide()
    
    def setupUi(self, crime):
        crime.setObjectName("crime")
        crime.resize(1159, 253)
        self.label = QtWidgets.QLabel(crime)
        self.label.setGeometry(QtCore.QRect(0, 230, 1161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(crime)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1161, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(7, 5, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(crime)
        self.commandLinkButton.setGeometry(QtCore.QRect(460, 130, 185, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.cont)

        self.retranslateUi(crime)
        QtCore.QMetaObject.connectSlotsByName(crime)

    def retranslateUi(self, crime):
        _translate = QtCore.QCoreApplication.translate
        crime.setWindowTitle(_translate("crime", "Dialog"))
        self.label.setText(_translate("crime", "Thanks for using this platform, we will appreciate a feedback. "))
        self.label_2.setText(_translate("crime", "<html><head/><body><p>Welcome to our Criminal Face Detection Service</p></body></html>"))
        self.commandLinkButton.setText(_translate("crime", "click me to continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    crime = QtWidgets.QDialog()
    ui = Ui_crime()
    ui.setupUi(crime)
    crime.show()
    sys.exit(app.exec_())
