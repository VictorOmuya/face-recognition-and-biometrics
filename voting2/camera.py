# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:24:23 2020

@author: Touching tap
"""
#import cv2, time
#video = cv2.VideoCapture(0)
#check, frame = video.read()

#print(check)
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#cv2.imshow('capturing', gray)
#cv2.waitKey(0)
#video.release()
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import ImageGrab


def messages(title, message):
    
    mess = QtWidgets.QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
    mess.exec_()
    


def classname():
    
    path = 'registered'
    images = []
    classNames = []
    myList = os.listdir(path)
    #print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    return classNames, images
 
def findEncodings(images):
    
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
 
def markvoting(name):
    today = datetime.date(datetime.now())
    todaystr = str(today)
    filename = '%s.csv'%todaystr
        
    with open(filename,'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}, "voted"')
 
#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
def captureScreen(bbox=(300,300,690+300,530+300)):
    
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr

def capture():
    classNames, images = classname()
    encodeListKnown = findEncodings(images)
    
     
    cap = cv2.VideoCapture(0)
     
    while True:
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
     
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
     
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
     
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                #print(name)
                status = name + '(voted)'
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(170,0,0),1)
                cv2.rectangle(img,(x1,y2-20),(x2,y2),(170,0,0),cv2.FILLED)
                cv2.putText(img,status,(x1+4,y2-3),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                #markvoting(name)
                break
            else:
                unrec = 'Not Recognised'
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(170,0,0),1)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(170,0,0),cv2.FILLED)
                cv2.putText(img,unrec,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                
                
     
        cv2.imshow('Webcam',img)
        cv2.waitKey(1)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            
                    break
    cap.release()
    cv2.destroyAllWindows()
    messages('voting', 'process has been completed')
