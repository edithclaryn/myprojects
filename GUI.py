#simple GUI
from tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Welcome")
root.geometry("200x100")

app = Frame(root)
app.grid ()
button1 = Button(app, text = "This is a button")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "click to view")

button3 = Button(app)
button3.grid()

buttom3["text"] = "cllick to exit"



#kick off the event loop
root.mainloop()