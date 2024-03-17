from tkinter import *
root=Tk()
root.title("Button Click  Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)

def msg1():
    l1.config(text="Hello")
def msg2():
    l1.config(text="Good Bye")
l1=Label(root,text="choose your colour",font=("Calibri",14,"bold"),fg='blue')
l1.place(x=100,y=30)
b1=Button(root,text="Text 1",command=msg1)
b2=Button(root,text="Text 2",command=msg2)
b1.place(x=80,y=200)
b2.place(x=180,y=200)


root.mainloop()