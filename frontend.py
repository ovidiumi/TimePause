from tkinter import *
from datetime import datetime
from KeyboardAction import keyboardDisable
import time

class Application(object):
    def __init__(self, window):
        self.window=window
        self.window.title("Time Pause")
        self.window.configure(width=800, height=650, bg ="#5F9EA0")
        self.createInterface()

    def startProgram(self):
        disable = keyboardDisable()
        disable.start()
        time.sleep(10)
        disable.stop()

    def createInterface(self):
        self.title = Label(self.window, text = 'Time for a break!')
        self.title.grid(row = 1, column = 3)

        self.time = Label(self.window, text = datetime.now().strftime("%H:%M:%S"))
        self.time.grid(row = 3, column = 3)

        self.button = Button(self.window, text = "Start", height = 1, width = 5, bg = "#8B0000",
        font = "#F0FFFF" ,command = self.startProgram)
        self.button.grid(row = 5, column =3)

window = Tk()
Application(window)
window.mainloop()
