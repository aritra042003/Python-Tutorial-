from tkinter import *
root=Tk()
root.title("Mouse Motion  Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)

def fun1(event):
    l1.config(text=("x= "+str(event.x)+" y="+str(event.y)))

l1=Label(root,fg="blue",font=("Calibri",14,"bold"))
l1.place(x=10,y=10)

root.bind('<Control-Motion>',fun1)

root.mainloop()