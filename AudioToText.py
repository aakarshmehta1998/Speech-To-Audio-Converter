import speech_recognition as sr
from gtts import gTTS
import os

def Audio1():
    print("Say Now")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        print("System Predicts:"+r.recognize_google(audio).capitalize())
    except Exception:
        print("Something Went Wrong")
    var=r.recognize_google(audio)    
    text=var
    speech=gTTS(text)
    speech.save("Sample_1.wav")

def Audio2():
    print("Say Now")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        print("System Predicts:"+r.recognize_google(audio).capitalize())
    except Exception:
        print("Something Went Wrong")
    var=r.recognize_google(audio)    
    text=var
    speech=gTTS(text)
    speech.save("Sample_2.wav")

def Merged():
    os.system('copy /b *.wav Merged.wav')
    
Audio1()
Audio2()
Merged()

