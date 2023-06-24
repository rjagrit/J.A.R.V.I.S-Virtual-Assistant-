import speech_recognition as sr
import win32com.client

def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")

    while 1:
        speaker.Speak(text)
        break

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1



if __name__ == '__main__':
    print('Pycharm')
    say("Hello, I am Jarvis AI")