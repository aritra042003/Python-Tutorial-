#Layout Management

from tkinter import *
root=Tk()
root.title("Layout Management place() and grid()")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)
l1=Label(root,text="First",bg='yellow')
l2=Label(root,text="Second",bg='lightgreen')
l3=Label(root,text="Third",bg='lightblue')
l4=Label(root,text="Fourth",bg='pink')

# l1.place(x=10,y=10,width=80,height=30)
# l2.place(x=10,y=100)
# l3.place(x=200,y=10)
# l4.place(x=200,y=100)
l1.config(width=20,height=5)
l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=1,column=0)
l4.grid(row=1,column=1)

root.mainloop()
