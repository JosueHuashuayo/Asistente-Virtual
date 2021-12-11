import speech_recognition as sr
import pyttsx3
import pywhatkit


listener = sr.Recognizer()
nombre = "alexa"
alexa = pyttsx3.init()
alexa.setProperty('rate',125)

def hablar(text):
    alexa.say(text)
    alexa.runAndWait()
def Escuchando():
    try:
        with sr.Microphone() as source :
            print("Escuchando ...")
            voice = listener.listen(source)
            grabacion = listener.recognize_google(voice,language="es-ES")
            grabacion = grabacion.lower()
            if nombre in grabacion:
                grabacion = grabacion.replace(nombre,"")
                
    except:
        pass
    return grabacion
    
def Youtube():
    grabacion = Escuchando()
    if "reproduce" in grabacion:
        musica = grabacion.replace("reproduce","")
        print(musica)
        hablar("Reproduciendo" + musica)
        pywhatkit.playonyt(musica)
Youtube()