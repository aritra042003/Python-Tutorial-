from tkinter import *
root=Tk()
root.title("Radiobutton example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)
v1=IntVar()
rb1=Radiobutton(root,text="Tea",variable=v1,value=1)
rb2=Radiobutton(root,text="Cofee",variable=v1,value=2)
rb1.place(x=100,y=10)
rb2.place(x=100,y=30)

v2=IntVar()
v2.set(1)
rb3=Radiobutton(root,text="Tea",variable=v2,value=1)
rb4=Radiobutton(root,text="Cofee",variable=v2,value=2)
rb3.place(x=200,y=10)
rb4.place(x=200,y=30)

v3=IntVar()

rb5=Radiobutton(root,text="Tea",variable=v3,indicator=0,value=1)
rb6=Radiobutton(root,text="Cofee",variable=v3,indicator=0,value=2)
rb5.config(bg="lightgreen")
rb6.config(bg="lightgreen")


rb5.place(x=300,y=10)
rb6.place(x=300,y=30)
root.mainloop()

