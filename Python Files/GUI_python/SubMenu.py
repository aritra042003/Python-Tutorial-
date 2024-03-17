from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.title("Sub Menu    Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)


def ShowCity(city):
    l1.config(text=city)
def showcolor(col):
    l1.config(fg=col)
mainmenu=Menu(root)
root.config(menu=mainmenu)


l1=Label(root,font=('Calibri',14,'bold'))
citymenu=Menu(mainmenu)
colormenu=Menu(mainmenu)
citymenu.add_command(label="basirhat",command=(lambda c="basirhat" : ShowCity(c)))
citymenu.add_command(label="Kolkata",command=(lambda c="kolkata" : ShowCity(c)))
citymenu.add_command(label="Durgapur",command=(lambda c="durgapur" : ShowCity(c)))

colormenu.add_command(label="red",command=(lambda c="red": showcolor(c)))
colormenu.add_command(label="green",command=(lambda c="green": showcolor(c)))
colormenu.add_command(label="blue",command=(lambda c="blue": showcolor(c)))

mainmenu.add_cascade(label="city",menu=citymenu)
mainmenu.add_cascade(label="color",menu=colormenu)

root.mainloop()