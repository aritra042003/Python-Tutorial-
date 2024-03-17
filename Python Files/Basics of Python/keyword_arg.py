# def f1(a=0,b,c=0):
#     d=a+b+c
#     print("sum is ",d)

# f1(1,8,9) 
# f1(1,7)   
# f1(12)




def f2(a,b):
    print("a=",a,"b=",b)
f2(2,3)      #positional arguement
f2(b=2,a=3)  #keywords arguement
f2(2,a=3)   
f2(b=2,3)
f2(a=4,6)
#Positional argument cannot appear after keyword arguments
