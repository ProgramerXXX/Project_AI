import cv2 
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
tracker = cv2.TrackerMedianFlow_create()
ontracking = False

while True:
    _,frame = cap.read()
    if not ontracking:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray,1.4,4)
        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            if tracker.init(frame,(x,y,w,h)) :
                ontracking = True
    else:
        ok,bbox = tracker.update(frame)
        if ok:
            p1 = (int(bbox[0]),int(bbox[1]))
            p2 = (int(bbox[0]+bbox[2]),int(bbox[1])+bbox[3])
            cv2.rectangle(frame,p1,p2,(0,255,0),2)
        else:
            ontracking = False
            tracker = cv2.TrackerMedianFlow_create()


    cv2.imshow('video',frame)
    cv2.waitKey(1)
    



  

