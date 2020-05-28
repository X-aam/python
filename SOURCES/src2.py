import cv2
import numpy as np
import os, os.path
source1 = "WIN_20191226_19_21_19_Pro.mp4"
def my_function():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    name = 1;
# To capture video from webcam. 
#cap = cv2.VideoCapture("http://192.168.0.14:8080/video")
    cap = cv2.VideoCapture(0)
    while True:
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Displa
        imgCrop = img[y:y+h,x:x+w]
        imgCropgray = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY)
        cv2.imshow('imgCropgray', imgCropgray)
           # cv2.imshow('imgCrop', imgCrop)
        cv2.imshow('img', img)
        name += 1
        print (name)
            # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff  
        if k==27:
            print(k)
            break
            return None
        
    # Release the VideoCapture object
    cap.release()



my_function()