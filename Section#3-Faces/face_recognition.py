import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('./haar_face.xml') # This will load the xml file

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy', allow_pickle=True) # This will load the features
# labels = np.load('labels.npy') # This will load the labels


face_recognizer = cv.face.LBPHFaceRecognizer_create() # This will create the face recognizer object
face_recognizer.read('face_trained.yml') # This will read the trained model

img = cv.imread(r'../Resources/Faces/val/ben_afflek/5.jpg') # This will read the image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # This will convert the image to gray scale
cv.imshow('Person', gray)


# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w] # This will get the region of interest of the face

    label, confidence = face_recognizer.predict(faces_roi) # This will predict the face
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)


cv.imshow('Detected Face', img)

cv.waitKey(0)