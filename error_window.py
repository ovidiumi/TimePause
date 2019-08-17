from tkinter import *

window = Tk()
window.title("Error Message")
message = "Sorry!It seems that this doesn't work for your PC"

label_font = ("Verdana", 14, 'bold')
label = Label(window, text = message ,font = label_font)
label.pack(side = 'top', fill = 'x', pady = 10)
window.after(5000, lambda: window.destroy())
window.mainloop()
