from tkinter import *
root=Tk()
root.title("Canvas example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)
c=Canvas(root,bg="grey")
c.place(x=10,y=10,width=400,height=400)
c.create_line(20,20,200,20,fill="yellow")
c.create_rectangle(30,30,200,200,fill="lightGreen",outline="red")
c.create_oval(30,220,90,280,fill="pink")
root.mainloop()