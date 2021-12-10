import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
nombre = "alexa"
siri = pyttsx3.init()
siri.setProperty('rate',125)

def hablar(text):
    siri.say(text)
    siri.runAndWait()
def Escuchando():
    try:
        with sr.Microphone() as source :
            print("Escuchando ...")
            voice = listener.listen(source)
            grabacion = listener.recognize_google(voice)
            grabacion = grabacion.lower()
            if nombre in grabacion:
                grabacion = grabacion.replace(nombre," ")
                print(grabacion)
    except:
        pass
    return grabacion
def Reproducir():
    grabacion = Escuchando()
    if "reproduce" in grabacion:
        print("Reproduciendo")
Reproducir()       