import os
import platform
import subprocess

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
    os.system("python message_window.py 1")

def popErrMsg():
    os.system("python error_window.py 1")

if __name__ == '__main__':
    main()
