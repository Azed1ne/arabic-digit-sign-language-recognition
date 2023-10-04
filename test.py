import numpy as np
import math
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

OFFSET = 30
IMG_SIZE = 300

capture = cv2.VideoCapture(0) #Use the webcam
detector = HandDetector(maxHands=1) #Detector object for 1 hand & 1 hand only
classifier = Classifier('Model/keras_model_.h5', 'Model/labels.txt')

with open('Model/labels.txt','r') as f:
    labels = [x.split()[1] for x in f.readlines()] #retrieving the labels from the text file

while True:
    success, img = capture.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)#draw=False
    if hands:
        hand = hands[0] # becoz we know we gonna detect only 1 hand
        x, y, w, h = hand["bbox"] # retreiving coords and size; bbox = bounding box

        imgWhite = np.ones((IMG_SIZE, IMG_SIZE, 3), np.uint8) * 255 # unsigned int of 8: 0-255 for colors
        imgCropped = img[y-OFFSET:y+h+OFFSET, x-OFFSET:x+w+OFFSET] # added the offset we insure it detects the full hand

        aspectRatio = h/w

        if aspectRatio > 1: # height is bigger than width
            k = IMG_SIZE/h # constant
            w_calculated = math.ceil(k*w) # same resize constant applied to the width
            if imgCropped.size > 0:
                imgResized = cv2.resize(imgCropped,(w_calculated, IMG_SIZE))
                w_gap = math.ceil((IMG_SIZE-w_calculated)/2) # calculating gap to center the image
                imgWhite[:, w_gap:w_calculated+w_gap] = imgResized
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                cv2.putText(imgOutput, labels[index], (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)
                cv2.rectangle(imgOutput, (x - OFFSET, y - OFFSET), (x + w + OFFSET, y + h + OFFSET), (255, 0, 255), 4)
                cv2.imshow("Hand cam", imgCropped)
                #print(prediction, index)

        else: # width is bigger than height
            k = IMG_SIZE / w  # constant
            h_calculated = math.ceil(k * h) # same resize constant applied to the height
            if imgCropped.size > 0:
                imgResized = cv2.resize(imgCropped, (IMG_SIZE, h_calculated))
                h_gap = math.ceil((IMG_SIZE - h_calculated) / 2) # calculating gap to center the image
                imgWhite[h_gap:h_calculated + h_gap, :] = imgResized
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                cv2.putText(imgOutput, labels[index], (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)
                cv2.rectangle(imgOutput, (x - OFFSET, y - OFFSET), (x + w + OFFSET, y + h + OFFSET), (255, 0, 255), 4)
                cv2.imshow("Hand cam", imgCropped)




        cv2.imshow("custom img", imgWhite)


    cv2.imshow("Number SL detector app", imgOutput) #Showing the webcam
    key = cv2.waitKey(1) #1ms delay
    if key == ord("q") or key == ord("Q"): #quit
        break