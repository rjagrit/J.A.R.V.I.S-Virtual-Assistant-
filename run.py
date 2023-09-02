from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
# module for moving gif
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime

flags= QtCore.Qt.WindowFlags(QtCore.Qt.FrameLessWindowHint)

Assistant= pyttsx3.init('sapi5')
voices= Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',180)

def say(text):
    Assistant.say(text)
    Assistant.runAndWait()

def wish():
    hour= int(datetime.datetime.now.hour)
    if hour>=0 and hour <12:
        say("Good Morning Sir")
    elif hour >= 12 and hour <18:
        say("Good Afternoon Sir")
    else:
        say("Good Night")


class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    @pyqtSlot()
    def run(self):
        self.JARVIS()


    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.energy_threshold = 800
            r.pause_threshold = 0.8
            audio = r.listen(source)
            try:
                print("Recognizing..")
                query = r.recognize_google(audio, language="en-iN")
                print(f"User said: {query}")
                return (query)
            except Exception as e:
                return ("Some Error Occurred, Please Speak Again Sir..")

    def JARVIS(self):
        wish()
        while True:
            self.query= self.takeCommand()
            if 'good bye' in self.query:
                sys.exit()

            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
            elif 'open youtube' in self.query


