import webbrowser

import pyttsx3
import speech_recognition as sr
import win32com.client
import openai
import os
from playsound import playsound
import datetime
import pywhatkit as pwt


# def chat(query):


def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    while 1:
        speaker.Speak(text)
        break

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 800
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language="en-iN")
            print(f"User said: {query}")
            return(query)
        except Exception as e:
            return("Some Error Occurred, Please Speak Again Sir..")

if __name__ == '__main__':
    say("Hi, I am Jarvis")
    while True:
        print("Listening....")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])


            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime}")
                break

            if "open camera" in query:
                os.system(f"start microsoft.windows.camera:")
                break

            if "open calculator" in query:
                os.system(f"start calc")
                break

            if "open Notepad" in query:
                os.system(f"start notepad")
                break

            if "open MS Word" in query:
                os.system(f"start winword")
                break

            if "open MS PowerPoint" in query:
                os.system(f"start powerpnt")
                break

            if "open MS Excel" in query:
                os.system(f"start excel")
                break

            if "play video" in query:
                say("Which video you want to play Sir")
                text = takeCommand()
                pwt.playonyt(text)

            if "search for me Jarvis" in query:
                say("What do you want me to search Sir")
                text = takeCommand()
                pwt.search(text)
                break

            if "find information" in query:
                say("What do you want me to find Sir")
                info = takeCommand()
                pwt.info(info)
                break

            if "send WhatsApp message for me" in query:
                say("Tell me the number sir")
                num =takeCommand()
                pnum = f"+91{num}"
                say("What message you want me to deliver sir")
                typemsg = takeCommand()
                say("Sure sir, I will send but first Tell me the timing sir...")
                say("On which hour should I send the message sir")
                hour = takeCommand()
                say("Tell me the minutes sir")
                mins = takeCommand()
                pwt.sendwhatmsg(pnum, typemsg, hour, mins)
                say("Message send successfully")
                break

            # if "shutdown my lapi" in query:
            #     pwt.shutdown(time=120)

            if "convert image for me" in query:
                pwt.image_to_ascii_art("C:\\Users\\Dell\\Downloads\\n.jpg","C:\\Users\\Dell\\Downloads\\n.txt")

            # if "convert text for me" in query:
            #     pyobj=pyttsx3.init()
            #     pyobj.say("Welcome to python ")
            #     pyobj.runAndWait()
            #     break




            # todo:write code for AWS and openai
            # else:
            #     chat(query)

        #say(query)


