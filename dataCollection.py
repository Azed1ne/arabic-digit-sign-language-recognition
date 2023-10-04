import numpy as np
import time
import math
import cv2
from cvzone.HandTrackingModule import HandDetector

OFFSET = 30
IMG_SIZE = 300
NUMBER_OF_SIGNS = 4 # since i made it recognise 4 digits/signs

capture = cv2.VideoCapture(0) #Use the webcam
detector = HandDetector(maxHands=1) #Detector object for 1 hand & 1 hand only

counter = [0]*NUMBER_OF_SIGNS # empty list with 4 elements to keep track of the number of images saved
fNumber = 0 # folder number, var to keep track of how many images we already saved
folder = 'Data/'+str(fNumber)


while True:
    success, img = capture.read()
    hands, img = detector.findHands(img)
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
                imgResized = cv2.resize(imgCropped, (w_calculated, IMG_SIZE))
                w_gap = math.ceil((IMG_SIZE-w_calculated)/2) # calculating gap to center the image
                imgWhite[:, w_gap:w_calculated+w_gap] = imgResized
                cv2.imshow("Hand cam", imgCropped)

        else: # width is bigger than height
            k = IMG_SIZE / w  # constant
            h_calculated = math.ceil(k * h) # same resize constant applied to the height
            if imgCropped.size > 0:
                imgResized = cv2.resize(imgCropped, (IMG_SIZE, h_calculated))
                h_gap = math.ceil((IMG_SIZE - h_calculated) / 2) # calculating gap to center the image
                imgWhite[h_gap:h_calculated + h_gap, :] = imgResized
                cv2.imshow("Hand cam", imgCropped)


        cv2.imshow("The image that will be saved", imgWhite)


    cv2.imshow("Number SL detector app", img) #Showing the webcam
    key = cv2.waitKey(1) #1ms delay
    if key == ord("s") or key == ord("S"): # save an image
        counter[fNumber] += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)

    if key == ord("1"):
        fNumber = 0
        print("============\nFolder is now 1, images:"+str(counter[fNumber])+"\n============")
    elif key == ord("2"):
        fNumber = 1
        print("============\nFolder is now 2, images:"+str(counter[fNumber])+"\n============")
    elif key == ord("3"):
        fNumber = 2
        print("============\nFolder is now 3, images:"+str(counter[fNumber])+"\n============")
    elif key == ord("4"):
        fNumber = 3
        print("============\nFolder is now 4, images:"+str(counter[fNumber])+"\n============")

    if key == ord("q") or key == ord("Q"): #quit
        break
