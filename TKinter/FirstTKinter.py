import tkinter as tki

window = tki.Tk()

window.title("First GUI Program")
window.minsize(500,300)
mylabel = tki.Label(text="Hello world")
mylabel.pack()

def changeLabel():
    mylabel.config(text="I got changed")

button = tki.Button(text="Click me", command=changeLabel)
button.pack()
window.mainloop()