# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pyQts\crime.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap

import face_recognition

class Ui_Crime(object):
    
    def getImage(self):
        
        fname = QFileDialog.getOpenFileName()
        self.imagePath = fname[0]
        pixmap = QPixmap(self.imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.label.setScaledContents(True)
        
        return self.imagePath
    
    def getImage1(self):
        
        fname = QFileDialog.getOpenFileName()
        self.imagePath1 = fname[0]
        pixmap = QPixmap(self.imagePath1)
        self.label_2.setPixmap(QPixmap(pixmap))
        self.label_2.setScaledContents(True)
        
        return self.imagePath1
    
    def compare(self):
        print(self.imagePath)
        image1 = self.imagePath
        image2 = self.imagePath1
        
        known_image = face_recognition.load_image_file(image1)
        unknown_image = face_recognition.load_image_file(image2)

        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)
     
        if results == [False]:
            self.lbl_result.setText("This is a different person.")
        elif results == [True]:
            self.lbl_result.setText("This is absolutely thesame person")
    
    def setupUi(self, Crime):
        Crime.setObjectName("Crime")
        Crime.resize(572, 253)
        
        self.label = QtWidgets.QLabel(Crime)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 141))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Crime)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 161, 141))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        
        
        self.btnbrowse1 = QtWidgets.QPushButton(Crime)
        self.btnbrowse1.setGeometry(QtCore.QRect(20, 180, 161, 23))
        self.btnbrowse1.setObjectName("btnbrowse1")
        self.btnbrowse1.clicked.connect(self.getImage)
        
        self.btnbrowse2 = QtWidgets.QPushButton(Crime)
        self.btnbrowse2.setGeometry(QtCore.QRect(390, 180, 161, 23))
        self.btnbrowse2.setObjectName("btnbrowse2")
        self.btnbrowse2.clicked.connect(self.getImage1)
        
        self.btncheck = QtWidgets.QPushButton(Crime)
        self.btncheck.setGeometry(QtCore.QRect(240, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(10)
        self.btncheck.setFont(font)
        self.btncheck.setObjectName("btncheck")
        self.btncheck.clicked.connect(self.compare)
        
        self.lbl_result = QtWidgets.QLabel(Crime)
        self.lbl_result.setGeometry(QtCore.QRect(190, 219, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(60)
        self.lbl_result.setFont(font)
        self.lbl_result.setText("")
        self.lbl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_result.setObjectName("lbl_result")

        self.retranslateUi(Crime)
        QtCore.QMetaObject.connectSlotsByName(Crime)

    def retranslateUi(self, Crime):
        _translate = QtCore.QCoreApplication.translate
        Crime.setWindowTitle(_translate("Crime", "crimeDetect"))
        self.btnbrowse1.setText(_translate("Crime", "BROWSE"))
        self.btnbrowse2.setText(_translate("Crime", "BROWSE"))
        self.btncheck.setText(_translate("Crime", "CHECK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Crime = QtWidgets.QDialog()
    ui = Ui_Crime()
    ui.setupUi(Crime)
    Crime.show()
    sys.exit(app.exec_())
