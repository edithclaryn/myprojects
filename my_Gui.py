#simple GUI
from tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Welcome")
root.geometry("200x50")

app = Frame(root)
app.grid ()
label = Label (app, text = "Hello there!")

label.grid()

#kick off the event loop
root.mainloop()