import tkinter as tki

window = tki.Tk()

window.title("First GUI Program")
window.minsize(500,300)
mylabel = tki.Label(text="Hello world")
mylabel.pack()
window.mainloop()