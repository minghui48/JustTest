from tkinter import *
from tkinter.messagebox  import askokcancel,showinfo


def shut_down():

   
    if askokcancel(title='Sure?',message='Quit'):
        app.destroy()


def wm_focus():
     showinfo("title","Focus")
     
app=Tk()

app.title("Message")
app.protocol("WM_TAKE_FOCUS",wm_focus)
app.protocol("WM_DELETE_WINDOW",shut_down)

app.mainloop()
