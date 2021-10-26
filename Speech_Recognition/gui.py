from tkinter import *
from tkinter import ttk 
import speech_recognition as spr 
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import googletrans
import time
import os

gui = Tk()
gui.geometry('500x500')
gui.title('Translate')

def SpecchTransLanguese(lang1='en',lang2='th'):

    time.sleep(1)
    print("Recodnizer....")
    #### Recognition ####
    rec = spr.Recognizer()
    with spr.Microphone() as speak:
        audio = rec.listen(speak)

    #### Speech To Text ####
    try:
        result = rec.recognize_google(audio,language=lang1)
        print(result)
    except:
        print("error")
        result = "มีบางอย่างผิดพลาดค่ะ"  

    #### Translator ####
    LAMs = Translator()
    word = LAMs.translate(result,dest=lang2)
    print(word.text)


    #### Text To MP3 ####
    i = 0
    tts = gTTS(text=word.text,lang=lang2)
    file1 = 'result '+str(i)+'.mp3'
    tts.save(file1)
    i = i +1
    

    #### Play MP3 #### 
    playsound(file1,True)
    os.remove(file1)

def SpeakThai():
    print('กรุณาพูดภาษาไทยค่ะ')
    SpecchTransLanguese('th','en')

def SpeakEng():
    print('Your speak english')
    SpecchTransLanguese('en','th')

f1 = Frame(gui)
f1.place(x=120,y=370)
b1 = ttk.Button(f1,text='speake thai',command=SpeakThai)
b1.pack(ipadx=20,ipady=10)

f2 = Frame(gui)
f2.place(x=270,y=370)
b2 = ttk.Button(f2,text='speake english',command=SpeakEng)
b2.pack(ipadx=20,ipady=10)

gui.mainloop()