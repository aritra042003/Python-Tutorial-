from tkinter import *
root=Tk()
root.title("Frame  Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)

f1=Frame(root,borderwidth=2,relief='solid')
f1.place(x=10,y=10,width=400,height=200)
l1=Label(f1,text="choose your colour",font=("Calibri",14,"bold"))
l1.place(x=10,y=10)
v=IntVar()
rb1=Radiobutton(f1,text="red",variable=v,value=1)
rb2=Radiobutton(f1,text="blue",variable=v,value=2)
rb3=Radiobutton(f1,text="green",variable=v,value=3)
rb1.place(x=50,y=60)
rb2.place(x=120,y=60)
rb3.place(x=190,y=60)
f2=Frame(root,borderwidth=2,relief='solid')
f2.place(x=10,y=240,width=400,height=200)
l2=Label(f2,text="enter your name",font=("Calibri",14,"bold"))
l2.place(x=10,y=10)
e1=Entry(f2)
e1.place(x=50,y=100)

root.mainloop()
