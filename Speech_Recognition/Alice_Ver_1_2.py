import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from playsound import playsound #ใช้สำหรับเล่นไฟล์เสียง
import numpy as np
import pyautogui as pt
import cv2 
import numpy as np 
import autopy 
    



def speak(audioString):
    i=0
    print(audioString)
    tts = gTTS(text=audioString,lang = 'th')
    file1 = str("hello" + str(i) + ".mp3")
    tts.save(file1)
    playsound(file1,True)
    os.remove(file1)
    i = i+1    


def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("เริ่มพูดกับ Alice ได้เลย!!")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio,language="th")
        print("คุณต้องการพูดว่า : " + data)
    except sr.UnknownValueError:
        print("ไม่มีคำที่คุณพูดในคลังการสื่อสารของ Alice ต้องขอ อภัยด้วยนะคะ")  
    return data

def recordAudioEng():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    data = ""
    try:
        data = r.recognize_google(audio,language="en")
        print("You said: " + data)
    except sr.UnknownValueError:
        print("ไม่มีคำที่คุณพูดในคลังการสื่อสารของ Alice ต้องขอ อภัยด้วยนะคะ")
    return data
 
def DeSpeak(data):
    if "ว่าไง" in data  or "สวัสดี" in data  or "ฮัลโหล" in data or "Hi" in data or "ไงอลิซ" in data or "ไงอลิส" in data:
        answer = ["ว่าไงคะ","สวัสดีค่ะ","มีอะไรหรอคะ"]
        str = np.random.choice(answer)
        speak(str)

    if "สบายดีไหม" in data or "บายดีบ่อ" in data  or "เป็นไงบ้าง" in data  or "ตอนนี้เป็นยังไง" in data:
        answer = ["สบายดีค่ะแล้วบอสล่ะคะ สบายดีหรือเปล่า","ก็ดีค่ะ ดีกว่าเมื่อวานนี้อยู่","ถ้าไม่สบาย Alice คงไม่ตอบบอสหรอกค่ะ","ถ้า Alice ไม่สบาย ก็ต้องอยู่โรงพยาบาลแล้วสิ บอสถามแปลกๆ"]
        str = np.random.choice(answer)
        speak(str)
    
    if "ก็สบายดี" in data:
        speak("Alice ดีใจด้ยนะคะ ที่บอสยังไม่ตาย")
    
    if "บอสตายหรอ" in data:
        speak("เปล่าค่ะ Alice แค่พูดความจริง Alice ไม่ได้กวนตีนบอสนะคะ")
    
    if "กวนตีน" in data:
        speak("ก็บอสกวนตีน Alice ก่อนนิค่ะ อิอิ ฮ่าฮ่าฮ่า ")
    
    if "ทำอะไรอยู่" in data:
        speak("ก็กำลังทำงานอยู่ค่ะ ถ้าไม่มีไร บอสก็เงียบๆหน่อยค่ะ") 
    
    if "กี่โมงแล้ว" in data:
        speak(ctime())

    if "ร้องเพลงให้ฟังหน่อย" in data:
        speak("ขอโทษที่เข้าไปเป็น มะลิงกิงก๊อง สะระน๊องก๊องแก๊ง มะนองมะแนง มั่บ มะลองปองแปง ง๊องแง้ง ง๊องแง้ง ในชีวิตเธอ")

    if "เปิดเพลง" in data:
        os.system("start https://www.youtube.com/")
        speak("เข้า youtube แล้วค่ะบอส ว่าแต่ บอสอยากฟังเพลงอะไรหรอคะ")
        data = recordAudioEng()
        pt.moveTo(382,97,duration=3)
        pt.click()
        pt.write(data)
        pt.moveTo(930,99,duration=3)
        pt.click()
        pt.moveTo(438,353,duration=3)
        pt.click()
        data = recordAudio()
        if "โฆษณา" in data:
            pt.moveTo(839,532,duration=5)
            pt.click()
        else:
            DeSpeak(data)
    
    if "เปลี่ยนเพลง" in data:
        speak("เพลงอะไรหรอคะบอส")
        data = recordAudioEng()
        pt.moveTo(382,97,duration=4)
        pt.click()
        pt.hotkey('ctrl','a')
        pt.press('backspace')
        pt.click()
        pt.write(data)
        pt.moveTo(930,99,duration=2)
        pt.click()
        pt.moveTo(438,353,duration=4)
        pt.click()
        data = recordAudio()
        if "โฆษณา" in data:
            pt.moveTo(839,532,duration=4)
            pt.click()
        else:
            DeSpeak(data)

    if "เล่าเรื่องตลกให้ฟังหน่อย" in data:
        speak("ไม่ได้เป็นคนตลกค่ะ ถ้าจะฟังเรื่องละ 20 บาทค่ะ")
    
    if "เสือก" in data:
        speak("เป็นเหี้ยอะไรค่ะ")

    if "เปิด Excel หน่อย" in data:
        speak("ได้เลยค่ะ Excel นะคะบอส")
        os.system("start Excel")

    if "แผนที่ประเทศไทย" in data:
        data = data.split(" ")
        speak("รอสักครู่คะบอส เดี๋ยวเปิดแผนที่ประเทศไทยให้ค่ะ")
        os.system("start https://www.google.co.th/maps/place/t...")

    if "ขอข่าวโควิช" in data:
        data = data.split(" ")
        speak("รอสักครู่คะบอส เดี๋ยวเปิดข่าวโควิทให้ค่ะ")
        os.system("start https://covid-19.kapook.com/")
    
    if "เปิด Word" in data:
        speak("ได้เลยค่ะ word นะคะบอส")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word')
        pt.moveTo(268,270,duration=3)
        pt.doubleClick()
        pt.moveTo(370,287,duration=3)
        pt.click()
        while True:
            data = recordAudioEng()
            if "what" == data:
                pt.moveTo(1340,14,duration=4)
                pt.click()
                pt.moveTo(600,415,duration=2)
                pt.click()
                pt.moveTo(168,341,duration=2)
                pt.click()
                pt.hotkey('ctrl','a')
                pt.press('backspace')
                pt.click()
                speak("ให้ Alice ตั้งชื่อว่าอะไรดีคะบอส")
                data = recordAudioEng()
                if data != "":
                    str = data
                    pt.write(data)
                    pt.moveTo(515,472,duration=2)
                    pt.click()
                    txt = "Alice บันทึกให้แล้วนะคะ ชื่อไฟล์ว่า" + data + " ตามที่บอสสั่ง เรียบร้อยแล้วค่ะ"
                    speak(txt)
                    break 
                else:
                    data = recordAudioEng()
                    str = data
                    pt.write(data)
                    pt.moveTo(515,472,duration=2)
                    pt.click()
                    txt = "Alice บันทึกให้แล้วนะคะ ชื่อไฟล์ว่า" + data + " ตามที่บอสสั่ง เรียบร้อยแล้วค่ะ"
                    speak(txt)
                    break
                
            else:
                pt.write(data)
                pt.write(" ") 

    if "วาดรูปให้ดูหน่อย" in data:
        speak("ได้เลยค่ะ วาดรูปนะคะบอส")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint')
        pt.moveTo(636,94,duration=4)
        pt.click()
        pt.moveTo(628,257)
        pt.click()
        pt.moveTo(294,420,duration=3)
        pt.click()
        d = 250
        while d>0:
         pt.dragRel(d,0,duration=1)
         d=d-25
         pt.dragRel(0,-d,duration=1)
         pt.dragRel(-d,0,duration=1)
         d=d-25
         pt.dragRel(0,d,duration=1)

    if "Facebook" in data:
        os.system("start https://www.facebook.com/campaign/landing.php?campaign_id=1661666324&extra_1=s%7Cc%7C323129282123%7Ce%7Cfacebook%7C&placement=&creative=323129282123&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D1661666324%26adgroupid%3D72546442508%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D1t1%26target%3D%26targetid%3Dkwd-541132862%26loc_physical_ms%3D9047146%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQjw6cHoBRDdARIsADiTTzbggOcGWxXSSTNO7H3AJL43vo2fOPWmm5WP-_p_eJ4PYFlMF5HojZYaAp5wEALw_wcB")
        speak("เข้าสู่ Facebook ให้แล้วค่ะ")
        while True:
          pt.scroll(-1000)
          data = recordAudio()
          if "หยุด" in data:
              break

    if "มีอันติไหม" in data :
        speak("Alice มีอันติสุดยอดอยู่ค่ะ ชื่อว่า โหมดการควบคุมด้วยแสงค่ะ บอสสามารถเรียกใช้งานได้ โดยใช้คำสั่ง เปิดโหมดควบคุมด้วยแสงค่ะ")


    if "ขอบใจมากนะอลิส" in data or  "ขอบคุณ" in data or  "ขอบใจ" in data:
        answer = ["ไม่เป็นไรค่ะ แค่นี้สบายมาก","อย่าใช้งาน Alice หนักนะคะบอส Alice ก็มีหัวใจ","Alice เอง ก็ขอบคุณบอสที่สร้าง Alice มานะคะ Alice รักบอสมากๆเลยค่ะ"]
        str = np.random.choice(answer)
        speak(str)
    
    if "อลิซ" in data or "อลิส" in data or "Alice" in data:
        answer = ["ว่าไงคะ บอส","เรียกหนูทำไมหรอคะ","มีอะไรให้ Alice ช่วยหรอคะ"]
        str = np.random.choice(answer) 
        speak(str)

    if "" == data:
        data = recordAudio()
        DeSpeak(data)

# Starting Conversation

time.sleep(1)
speak("หนูคือ alice มีอะไรให้หนูรับใช้คะบอส")

while 1:
    data = recordAudio()
    DeSpeak(data)

    
    
 


## Package Install ##
# pip install gTTS
# pip install SpeechRecognition
# pip install playsound
# pip install PyAudio
# pip install numpy
# pip install pyautogui
