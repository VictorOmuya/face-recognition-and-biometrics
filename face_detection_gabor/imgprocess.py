import cv2
import numpy as np
import os

from gabor import get_image_feature_vector, build_filters
from nb import get_nb_label
from jann import get_ann_label, get_brain
from nb import process_training_data, get_nb_label

from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QMessageBox

INPUT_DIR = 'data/input/'
OUTPUT_DIR = 'data/output/'

def messages(title, message):
    mess = QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    mess.setStandardButtons(QMessageBox.Ok)
    mess.exec_()

def auto_canny(image, sigma=0.33):
    # Adjust threshold values of canny based on median values of the image
    v = np.median(image)
 
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
 
    return edged

def get_objects_from_file(filename, train=False):
    # Load image
    orig = cv2.imread(INPUT_DIR + filename)
    get_objects_from_img(orig, filename, train)

def get_objects_from_img(orig, filename=".jpg", train=False, webcam=True):
    img = orig.copy()
    ann_label = 0
    # Convert to gray, equalize to improve contrast
    # imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # imgray = cv2.equalizeHist(imgray)

    # Boundaries of "skin" HSV intensities
    lower = np.array([0, 3, 0], dtype = "uint8")
    upper = np.array([60, 255, 190], dtype = "uint8")

    # Convert to HSV, get colors that are in range of earlier intensities
    converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    skinMask = cv2.inRange(converted, lower, upper)
 
    # Apply erosions and dilations to the mask using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
 
    # Blur
    skinMask = cv2.GaussianBlur(skinMask, (5, 5), 0)
 
    # Apply mask
    # skin = cv2.bitwise_and(img, img, mask = skinMask)
    # cv2.imshow("images", np.hstack([img, skin]))
    # comb = cv2.add(skinMask, imgray)

    # Perform Canny
    edges = auto_canny(skinMask)

    # Find contours
    ret,thresh = cv2.threshold(edges, 100, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    filters = build_filters()

    brain = get_brain()

    for i in range(len(contours)):
        # Draw contours
        # image = cv2.drawContours(img, contours, i, (0,255,0), 1)

        # Identify bounding boxes
        x,y,w,h = cv2.boundingRect(contours[i])

        # Arbitrary threshold height and width is 30, 30
        if h>30 and w>30: 
            cropimg = orig[y:y+h, x:x+w]
            if train:
                output_name = OUTPUT_DIR + filename[:-4] + str(i) + '.jpg'
                cv2.imwrite(output_name, cropimg)
            else:
                feature_set = get_image_feature_vector(cropimg, filters)
                ann_label = get_ann_label(feature_set, brain)
                # nb_label = get_nb_label(feature_set)
                
                print ("Found a face" if ann_label == 1 else "This is not a face")
                if ann_label == 1:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
                    messages("face", "found a face")
                    break
                
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (100,100,100,50), 2)
                    messages("face", "no face found")
                    
                    
            # To show individual images in a window:
            # cv2.imshow('Cropped Image ' + str(i), cropimg)
    
    # For manual processing
    if not train and not webcam:
        annot_name = OUTPUT_DIR + filename
        cv2.imwrite(annot_name, img)

    # For webcam
    if webcam:
        cv2.imshow('Annotated Image', img)

    # If not using with webcam and you want to display until exit
    # cv2.imshow('Annotated Image', img)
    # cv2.waitKey(0)

if __name__ == '__main__':
    for filename in os.listdir(INPUT_DIR):
        get_objects_from_file(filename, False)
