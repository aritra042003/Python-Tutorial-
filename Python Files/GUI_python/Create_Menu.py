from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.title("Menu    Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)
def ShowName():
    l1.config(text="Aritra Pain")
def ShowUrl():
    l1.config(text="Linkdin")
def ShowCity():
    l1.config(text="Basirhat")


l1=Label(root,font=("calibri",14,'bold'),fg="blue")
l1.place(x=50,y=100)
mainmenu=Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="Myname",command=ShowName)
mainmenu.add_command(label="Website",command=ShowUrl)
mainmenu.add_command(label="City",command=ShowCity)

root.mainloop()