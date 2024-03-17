from tkinter import *
root=Tk()
root.title("Checkbutton example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)
cb1=Checkbutton(root)
cb1.place(x=10,y=10)

cb2=Checkbutton(root,text="Agree")
cb2.config(borderwidth=2,relief='solid')

cb2.place(x=10,y=40)
cb3=Checkbutton(root,text="Already selected")
cb3.select()
cb3.config(bg="gray")
cb3.place(x=10,y=80,width=200,height=30)
root.mainloop()