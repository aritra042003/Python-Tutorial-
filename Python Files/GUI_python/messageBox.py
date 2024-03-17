from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.title("Message boxes   Example")
root.geometry('500x500')
root.wm_minsize(width=300,height=300)

#print(showinfo("Information","Today is sunday"))
#showwarning("warning","you are wrong")
# showerror("error","you are error")
# askquestion("Question","do you want to proceed")
# askokcancel("Question","do you want to proceed")
# askyesno("Question","do you want to proceed")
askretrycancel("Question","do you want to proceed")
root.mainloop()
