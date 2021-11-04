import cv2 as cv
from cv2 import CascadeClassifier
import pickle
import numpy as np

im = cv.v
faceDetaction = CascadeClassifier('E:/FaceRecog/facedetect.xml')
svmmodel = pickle.load(open('E:/FaceRecog/gendermodelpca.mol','rb'))
facepca = pickle.load(open('E:/FaceRecog/gendermodelpca.pca','rb'))

while(True):
    frame = cv.imread('Test3.jpg')
    im = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    faces = faceDetaction.detectMultiScale(im)
    
    for f in faces:
        x,y,w,h = f
        face = im[y:y+h, x:x+w]
        face = cv.resize(face, (100,100))
        face = np.array(face).reshape((1,10000))
        x_face = facepca.transform(face)
        result = svmmodel.predict(x_face)
        gender = ''
        if (result == 1):
            gender = 'Aiw'
        elif (result == 2):
            gender = 'Dream'
        elif (result == 3):
            gender = 'Joy'
        elif (result == 4):
            gender = 'Mak'
        elif (result == 5):
            gender = 'Nong'
        elif (result == 6):
            gender = 'Pang'
        elif (result == 7):
            gender = 'Pon'
        elif (result == 8):
            gender = 'Sa'
        elif (result == 9):
            gender = 'Kim'
        elif (result == 10):
            gender = 'M'
        elif (result == 11):
            gender = 'Tran'
        elif (result == 12):
            gender = 'Big'
        else:
            gender = 'UnKnow'
           
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255))
        cv.putText(frame, f'{gender}', (x, y-15), cv.FONT_HERSHEY_PLAIN, 1, (0,0,255),2)
    k = cv.waitKey(1)
    cv.imshow('frame', frame)
    if(k == 27):
        cv.release()
        cv.destroyAllWindows()
        