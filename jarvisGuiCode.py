import sys
from subprocess import call
from jarvis import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QTime, QDate
from PyQt5.uic import loadUiType
import jarvis_AI
class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        call(["python","jarvis_AI.py"])

# class for moving GIF
startExe= MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui= Ui_Form()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.gui.label1= QtGui.QMovie("GIF//giphy.gif")
        self.gui.label.setMovie(self.gui.label1)
        self.gui.label1.start()


        timer= QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()

    def showTimeLive(self):
        t_ime= QTime.currentTime()
        time= t_ime.toString()
        d_ate= QDate.currentDate()
        date= d_ate.toString()
        label_time= time
        label_date= date
        self.gui.Textime.setText(label_time)
        self.gui.Textdate.setText(label_date)



GuiApp= QApplication(sys.argv)
jarvis_gui= Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())




