import platform
import subprocess
import time

from tkinter import *

def startProgram():
    popMsg()
    if platform.system() == "Linux":
        subprocess.call("xdg-screensaver lock", shell = True)
    elif platform.system() == "Windows":
        subprocess.call("xrundll32.exe user32.dll, LockWorkStation", shell = True)
    elif platform.system() == "Darwin":
        subprocess.call('tell application "System Events" to log out', shell = True)
    else:
        popErrMsg()

def popMsg():
    window = Tk()
    window.title("Message")

    message = "It's time for a break!\nYour computer will logout in: "
    remaining = 0

    label_font = ("Verdana", 14, 'bold')
    label1 = Label(window, text = message ,font = label_font).grid(row = 0)
    label2 = Label(window, text = "10" ,fg = "red", font = label_font).grid(row = 1)
    label3 = Label(window, text = "seconds" ,font = label_font).grid(row = 2)
    #countdown(10)

    window.after(10000, lambda: window.destroy())
    window.mainloop()

    #NOT WORKING.FURTHER WORK
    '''
    def countdown(remaining = None):
        if remaining is not None:
            remaining = remaining
        if remaining == 0:
            label2 = Label(window, text = "0" ,fg = "red", font = label_font).grid(row = 1)
        else:
            label2 = Label(window, text = "%d"%remaining ,fg = "red", font = label_font).grid(row = 1)
            remaining = remaining - 1
            label2.after(1000,countdown(remaining))
    '''

def popErrMsg():
    window = Tk()
    window.title("Error")
    message = "Sorry!It seems that this doesn't work for your PC"

    label_font = ("Verdana", 14, 'bold')
    label = Label(window, text = message ,font = label_font)
    label.pack(side = 'top', fill = 'x', pady = 10)
    window.after(10000, lambda: window.destroy())
    window.mainloop()

if __name__ == '__main__':
    main()
