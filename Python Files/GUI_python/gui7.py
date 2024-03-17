#Layout Management

from tkinter import *
root=Tk()
root.title("Layout Management pack()")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)
l1=Label(root,text="First",bg='yellow')
l2=Label(root,text="Second",bg='lightgreen')
l3=Label(root,text="Third",bg='lightblue')
l4=Label(root,text="Fourth",bg='pink')
# l1.pack(fill=X)
# l2.pack(fill=X)
# l3.pack(fill=X)
# l4.pack(fill=X)

l1.pack(padx=10,pady=20)
l2.pack(ipadx=10,ipady=20)
l3.pack()
l4.pack()

root.mainloop()
