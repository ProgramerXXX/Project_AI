import cv2 
import os
import numpy as np 

cap = cv2.VideoCapture('rtsp://192.168.1.123:8080/h264_pcm.sdp')
path = 'computer_vision/'
h = s = p = e = 0
while True:
    _,frame = cap.read()
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('h'): h+=1; cv2.imwrite(path+'hamer_'+str(h)+'.png',frame)
    if key == ord('s'): s+=1; cv2.imwrite(path+'scissor_'+str(s)+'.png',frame)
    if key == ord('p'): p+=1; cv2.imwrite(path+'paper_'+str(p)+'.png',frame)
    if key == ord('e'): e+=1; cv2.imwrite(path+'else_'+str(e)+'.png',frame)
    if key == 27:
         break
    
    y = []; d = []
    for fname in os.listdir(path):
         if '.png' in fname:
             x = cv2.imread(path+fname)
             y.append(fname.split('_')[0])
             d.append(np.sum((x-frame)**2))
    if len(d) > 0 :
         ans = y[d.index(min(d))]
        
         if ans != 'else' : cv2.putText(frame,ans,(20,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
    img = cv2.resize(frame,(720,480))
    cv2.imshow('frame',img)
    

cv2.destroyAllWindows()

