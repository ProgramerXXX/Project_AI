import cv2 

cap = cv2.VideoCapture('rtsp://192.168.1.7:8080/h264_pcm.sdp')

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(780,450))
    cv2.imshow('frame',frame)

    cv2.waitKey(1)
