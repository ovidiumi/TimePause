from tkinter import *

def countdown(i, label):
    if i > 0:
        i -= 1
        label.set(i)
        window.after(1000, lambda: countdown(i, label))
    else:
        close()

def close():
    window.destroy()

window = Tk()
window.title("Message")

counter = 10
font_label = ("Verdana", 14, 'bold')
text_label = StringVar()
text_label.set(counter)
lbl1 = Label(window, text = "It's time for a break!\nThe computer will logout in:", font=font_label).pack()
lbl2 = Label(window, textvariable=text_label,font=font_label, fg="red").pack()
lbl3 = Label(window, text = "seconds",font=font_label).pack()

countdown(counter, text_label)

window.mainloop()
