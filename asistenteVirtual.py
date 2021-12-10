import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

siri = pyttsx3.init()

try:
    with sr.Microphone() as source :
        print("Escuchando ...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
        siri.say(rec)
        siri.runAndWait()
except:
    pass