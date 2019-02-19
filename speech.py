import speech_recognition as sr
import pyaudio
r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))

    except:
        print('say it again,cant recognize')