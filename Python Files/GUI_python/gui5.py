#lock min max size of screen

from tkinter import *
screen=Tk()   
screen.title("Limit Scr   een Size")
screen.geometry("500x500")
screen.wm_minsize(width=400,height=400)
screen.wm_maxsize(width=400,height=400)
screen.mainloop()

