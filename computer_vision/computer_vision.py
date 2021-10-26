import cv2

cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    R = frame[:,:,2]
    G = frame[:,:,1]
    B = frame[:,:,0]
    mask = (R<50) & (G<50) & (B>120)
    
    cv2.imshow('frame',mask*1.0)
    cv2.imshow('frame2',frame)
    if cv2.waitKey(1) & 0xff == 27:
        break


cv2.destroyAllWindows()
