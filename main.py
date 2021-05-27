# Main File

import speech_recognition as sr

#Cria um reconhecedor
r = sr.Recognizer()

#abrir o microfone para captura
with sr.Microphone() as source:
   
    audio = r.listen(source) #Define microfone como fonte de áudio

    print(r.recognize_google(audio,language="pt-BR"))