# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_police.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QMessageBox
import pandas as pd
import os
import face_rec
import reg
import face_recognition


class Ui_face_police(object):
    
    
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
        
        self.lbl_img_2.setPixmap(QPixmap(pixmap))
        self.lbl_img_2.setScaledContents(True)
        
    def rec_face(self):
        
        try:
            
            image = face_recognition.load_image_file(self.imagePath)
            face_locate = face_recognition.face_locations(image)
            
            if len(face_locate) > 0:
            
                self.name = face_rec.capture(self.imagePath)
                print(self.name)
                    
                if self.name == "not seen":
                    self.messagebox("police", "this person isn't found in the database!")
                else:
                    res = 'this is '+ self.name
                    self.messagebox("police", res)
                        
                    data = pd.read_csv('database.csv')
                    discription = data[data['Name'] == self.name.lower()]
                        
                    info = str(discription['Description'].values)
                        
                    infos = ''.join(info[2:-2])
                   
                    self.messagebox("police", infos)
                    
            elif len(face_locate) == 0:
                self.messagebox("police", "No face found. Kindly upload a valid or a clearer image!")
            
        except:
            self.messagebox("error", "Problem with image")
                
    
    def setupUi(self, face_police):
        face_police.setObjectName("face_police")
        face_police.resize(761, 282)
        self.bg = QtWidgets.QLabel(face_police)
        self.bg.setGeometry(QtCore.QRect(0, 0, 471, 211))
        self.bg.setText("")
        self.bg.setObjectName("bg")
        
        self.lbl_img = QtWidgets.QLabel(face_police)
        self.lbl_img.setGeometry(QtCore.QRect(30, 60, 210, 160))
        self.lbl_img.setText("")
        self.lbl_img.setObjectName("lbl_img")
        
        self.pushButton = QtWidgets.QPushButton(face_police)
        self.pushButton.setGeometry(QtCore.QRect(280, 14, 201, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse)
        
        self.btn_recog = QtWidgets.QPushButton(face_police)
        self.btn_recog.setGeometry(QtCore.QRect(280, 95, 200, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(68)
        self.btn_recog.setFont(font)
        self.btn_recog.setObjectName("btn_recog")
        self.btn_recog.clicked.connect(self.rec_face)
        
        self.lbl_img_2 = QtWidgets.QLabel(face_police)
        self.lbl_img_2.setGeometry(QtCore.QRect(520, 60, 210, 160))
        self.lbl_img_2.setText("")
        self.lbl_img_2.setObjectName("lbl_img_2")
        
        self.label = QtWidgets.QLabel(face_police)
        self.label.setGeometry(QtCore.QRect(0, 0, 761, 51))
        self.label.setStyleSheet("background-color: rgb(170, 0, 127);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(face_police)
        self.label_2.setGeometry(QtCore.QRect(0, 230, 761, 51))
        self.label_2.setStyleSheet("background-color: rgb(170, 0, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.bg.raise_()
        self.lbl_img.raise_()
        self.pushButton.raise_()
        self.btn_recog.raise_()
        self.lbl_img_2.raise_()
        self.label_2.raise_()

        self.retranslateUi(face_police)
        QtCore.QMetaObject.connectSlotsByName(face_police)

    def retranslateUi(self, face_police):
        _translate = QtCore.QCoreApplication.translate
        face_police.setWindowTitle(_translate("face_police", "Police"))
        self.pushButton.setText(_translate("face_police", "BROWSE IMAGE"))
        self.btn_recog.setText(_translate("face_police", "RECOGNIZE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    face_police = QtWidgets.QDialog()
    ui = Ui_face_police()
    ui.setupUi(face_police)
    face_police.show()
    sys.exit(app.exec_())
