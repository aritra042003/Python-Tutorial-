from tkinter import *
root=Tk()
root.title("Label  Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)
l1=Label(root,text="First")
l1.place(x=10,y=10)
l2=Label(root,text="second",width=10,height=3,fg='lightblue',bg='navy',font=("calibri",16,'bold'))
l2.place(x=100,y=10)
pic=PhotoImage(file="thermal.jpg")
l4=Label(root,text="Fourth",fg='yellow',image=pic)
l4.place(x=10,y=200,width=200,height=200)

root.mainloop()
