import cv2 
import numpy as np 
import HandsTrackingModule as ht
import time 
import autopy 
import pyautogui as pt 


#กำหนดขนาดของ หน้าจอแสดงผล
Wcam , Hcam = 600 , 480 
frameR = 100 #ขนาดของการจับภาพรอบๆเพื่อ detec การเคลื่อนไหว
smootlenght = 5
#อ่านภาพจากกล้อง notebook

plocX,plocY = 0,0
clocX,clocY = 0,0

cap = cv2.VideoCapture(0)
cap.set(3,Wcam)
cap.set(4,Hcam)
pTime = 0
detector = ht.handDetector(maxHands=1)
Wscr , hscr = autopy.screen.size()
print(Wscr,hscr)

while True:
    #รับภาพมาแบบต่อเนื่องและค่อยๆแสดงไป พร้อมกับวาดกรอบของมันรอบๆมือ ไปด้วย 
    #โดยใช้ funtion จาก Hands
    success , frame = cap.read()
    frame = detector.findHands(frame)
    lmList , bbox = detector.findPosition(frame)
    #ตรวจสอบ position ของนิ้วชี้และนิ้วกลาง 
    if len(lmList) != 0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]

        finger = detector.fingersUp()
    #ตรวจจับภาพการเคลื่อนไหวแทนอื่นๆ เช่น เวลเลื่อนเมาท์ลง มือที่ detected ไว้ อาจหายได้
        cv2.rectangle(frame,(frameR+50,frameR+50),(Wcam-frameR+50,Hcam-frameR+50),(255,0,255),2)
    #จับการเคลื่อนไหวของนิ้วมือ และลบ framR ออกไปเพื่อ ให้เมาท์เคลื่อนไหวตามกรอบที่วางไว้
        if finger[1] == 1 and finger[2] == 0 :
    
            x3 = np.interp(x1,(frameR,Wcam-frameR),(0,Wscr))
            y3 = np.interp(y1,(frameR,Hcam-frameR),(0,Wscr))

            clocX = plocX + (x3 - plocX)/smootlenght
            clocY = plocY + (y3 - plocY)/smootlenght
        

    #เคลื่อนโดยการกดปุ่มแป้นพิมพ์ เทียบกับ position ของมือที่ขยับไปตามค่าตำแหน่งที่กำหนดไว้  
            print(clocX,clocY)   
            if clocX >830:
                pt.press('right')  #กดปุ่มลูกศรเลื่อนขวา --->
            if clocX <770:
                pt.press('left')   #กดปุ่มลูกศรเลื่อนซ้าย <---

            #autopy.mouse.move(Wscr-clocX,clocY)  อันนี้เป็นโค้ดไว้ขยับเมาท์ตามนิ้ว แต่กรณีนี้ไม่ใช้ 

    #วาดวงกลมรอบหัวนิ้วชี้ ทำเครื่องหมายให้เหมือน pointer
            cv2.circle(frame,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocX, plocY = clocX , clocY    

        
        if finger[1] == 1 and finger[2] == 1 :  #หากพบนิ้วค่อยสร้างกรอบสี่เหลี่ยมขึ้นมา
            lenght , frame , lineInfo = detector.findDistance(8,12,frame)
            print(lenght)
            disTance = lenght  #หาระยะห่างระหว่างนิ้ว ชี้กับนิ้วกลาง
    #ใช้คำสั่งในกดแป้นพิมพ์ 
            if disTance <50:  #หากนิ้วชี้กับนิ้วโป้งติดกัน 
              cv2.circle(frame,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
              pt.press('space') #ให้ทำการกดปุ่ม space bar หรือในเกมส์คือปุ่มเร่งความเร็ว 

    cTime = time.time()
    fbs = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame,str(int(fbs)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("frame",frame)
    cv2.waitKey(1)

