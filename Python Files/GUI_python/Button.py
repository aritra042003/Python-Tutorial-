from tkinter import *
root=Tk()
root.title("Button Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)
b1=Button(root,text='First')
b1.place(x=10,y=10)
b2=Button(root,text='Second')
b2.config(width=20,height=3)
b2.place(x=100,y=10)
b3=Button(root,text='Third')
b3.place(x=10,y=100,width=80,height=20)
b4=Button(root,text='Forth',bg='green',fg='white')
b4.place(x=100,y=100,width=100,height=30)

root.mainloop()