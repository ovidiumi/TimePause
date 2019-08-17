from tkinter import *
from controllers import *
import time

window = Tk()
window.title("Time Pause")
window.geometry("200x100")
time1 = ''
clock = Label(window, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
tick()

def start():
    window.destroy()
    startProgram()

button = Button(window, text = "Start", height = 1, width = 5, bg = "#8B0000",
    font = "#F0FFFF" ,command = start).pack()

window.mainloop()
