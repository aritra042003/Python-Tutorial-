from tkinter import *
root=Tk()
root.title("Add 2 numbers Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)



def sum():
    a=int(e1.get())
    b=int(e2.get())
    s=a+b
    l4.config(text="sum of %d and %d is %d "%(a,b,s))

l1=Label(root,text="Addition of 2 numbers",fg='blue')
l1.config(font=("Calibri",14,"bold"))
l1.place(x=50,y=50)


l2=Label(root,text="First Number",fg='blue')
l2.config(font=("Calibri",14,"bold"))
l2.place(x=30,y=100)


l3=Label(root,text="second number",fg='blue')
l3.config(font=("Calibri",14,"bold"))
l3.place(x=30,y=150)


e1=Entry(root,borderwidth=2,relief='solid')
e2=Entry(root,borderwidth=2,relief='solid')
e1.place(x=180,y=100)
e2.place(x=180,y=150)

b1=Button(root,text='Add',command=sum)
b1.place(x=50,y=180)

l4=Label(root,text="result will come here")
l4.place(x=30,y=240)

root.mainloop()
