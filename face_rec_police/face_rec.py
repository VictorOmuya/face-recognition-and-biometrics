import cv2

import numpy as np
import face_recognition
import os

from PIL import ImageGrab
import matplotlib as plt

def classname():
        
    path = 'registered'
    images = []
    classNames = []
    myList = os.listdir(path)
        
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


def capture(imag):
    classNames, images = classname()
    encodeListKnown = findEncodings(images)
    
    test_img1 = cv2.imread(imag)     
    img = test_img1
            #img = captureScreen()
    #imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    #imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    

         
    facesCurFrame = face_recognition.face_locations(img)
    encodesCurFrame = face_recognition.face_encodings(img,facesCurFrame)
         
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)   
        
        if matches[matchIndex] or max(faceDis) >= 0.85:
                
            name = classNames[matchIndex].upper()
           
                
        else:
            name = "not seen"
        
        return name
    #cv2.imshow(img)
            #cv2.waitKey(1)

#capture("C:/Users/HP/Documents/vics/spyders/voting/registered/michael bolton.jpg")
