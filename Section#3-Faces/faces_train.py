import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('./haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'../Resources/Faces/train'


features = [] # This will store the faces
labels = [] # This will store the labels
def create_train():
    for person in people: # This will loop through all the people in the directory
        path = os.path.join(DIR, person) # os.path.join is used to join the path of the directory with the person's name
        label = people.index(person) # This will give the index of the person in the list of people

        for img in os.listdir(path): # This will loop through all the images in the directory
            img_path = os.path.join(path, img) # This will join the path of the person with the image

            img_array = cv.imread(img_path) # This will read the image
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect =  haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y, w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi) # This will append the face to the features list
                labels.append(label) # This will append the label to the labels list


create_train()
print("----------------Training Done----------------")


features = np.array(features, dtype='object')
labels = np.array(labels)

# print(f"Length of the features = {len(features)}")
# print(f"Length of the labels = {len(labels)}")


face_recognizer = cv.face.LBPHFaceRecognizer_create() # This will create the face recognizer object

#Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)


face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
