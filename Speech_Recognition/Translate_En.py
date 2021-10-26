import speech_recognition as spr 
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import googletrans
import time

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
    tts = gTTS(text=word.text,lang=lang2)
    tts.save('result.mp3')

    #### Play MP3 #### 
    playsound('result.mp3')

SpecchTransLanguese('en','th')

