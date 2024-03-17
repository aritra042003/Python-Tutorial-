from tkinter import *
root=Tk()
root.title("Radio button event Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)


def setColor():
    c=['red','blue','green']
    e1.config(fg=c[v.get()-1])

l1=Label(root,text="select your colour",font=("Calibri",14,"bold"))
l1.place(x=50,y=40)
v=IntVar()
v.set(1)
rb1=Radiobutton(root,text="red",fg='red',variable=v,value=1,command=setColor)
rb2=Radiobutton(root,text="blue",fg='blue',variable=v,value=2,command=setColor)
rb3=Radiobutton(root,text="green",fg='green',variable=v,value=3,command=setColor)
rb1.place(x=50,y=80,width=80)
rb2.place(x=150,y=80,width=80)
rb3.place(x=250,y=80,width=80)

l2=Label(root,text="Enter your name ",font=("Calibri",14,"bold"))
l2.place(x=50,y=150)
e1=Entry(root,borderwidth=2,relief='solid')
e1.place(x=50,y=200)
root.mainloop()