x=10
def f1():
    # global x
    x=5 # local  variable 
    g=globals()
    print("Local x =",x)
    print("global x =",g['x'])
#f1()
print("global x=",x)
f1()
