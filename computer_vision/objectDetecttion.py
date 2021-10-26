import cv2
import parinya

cap = cv2.VideoCapture(0)
yolo = parinya.YOLOv3('computer_vision/coco.names','computer_vision/yolov3-tiny.cfg','computer_vision/yolov3-tiny.weights')

while True:
    _,frame = cap.read()
    obj = yolo.detect(frame,draw=False)
    for d in obj:
        label,left,top,width,height = d
        print(d)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)