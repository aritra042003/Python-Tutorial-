from tkinter import *

# Fields for the loan calculator
fields = ("loan amount", "Number of installments", "rate of interest", "Installment")

def calculate_installment(entries):
    # Calculate the installment based on user inputs
    r = (float(entries[fields[2]].get()) / 100) / 12
    p = float(entries[fields[0]].get())
    n = float(entries[fields[1]].get())
    i = p * r * (1 + r) ** n / ((1 + r) ** n - 1)
    
    # Format the result and update the Installment entry
    i = ("%8.2f" % i).strip()
    entries[fields[3]].delete(0, END)
    entries[fields[3]].config(state=NORMAL)
    entries[fields[3]].insert(0, i)
    entries[fields[3]].config(state=DISABLED)

def makeform(root, fields):
    entries = {}
    for field in fields:
        # Create a row for each field with a label and entry widget
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor="w")
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        entries[field] = ent
    
    # Disable the last entry (Installment) initially
    entries[field].config(state=DISABLED)
    return entries

if __name__ == '__main__':
    # Create the main Tkinter window
    root = Tk()
    
    # Create entry widgets and get a reference to them
    ents = makeform(root, fields)
    
    # Add "Calculate Installment" button with associated command
    b1 = Button(root, text="Calculate Installment", command=(lambda e=ents: calculate_installment(e)))
    b1.pack(side=LEFT, padx=5, pady=5)

    # Add "Exit" button to quit the application
    b2 = Button(root, text="Exit", command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)

    # Start the Tkinter main loop
    root.mainloop()
