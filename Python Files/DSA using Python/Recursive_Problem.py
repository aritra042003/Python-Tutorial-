#Print First N natural Number

def PrintN(n):
    if n>0:
        PrintN(n-1)
        print(n,end=' ')
PrintN(10)
print()

#Print First N natural Number in Reverse Order

def printN_Reverse(n):
    if n>0:
        print(n,end=' ')
        printN_Reverse(n-1)
printN_Reverse(10)

print()


#Print First N ODD natural Number
def PrintN_ODD(n):
    if n>0:
        PrintN_ODD(n-1)
        print(2*n-1,end=' ')
PrintN_ODD(10)
print()

#Print First N Even natural Number
def PrintN_Even(n):
    if n>0:
        PrintN_Even(n-1)
        print(2*n,end=' ')
PrintN_Even(10)
print()
#Print First N ODD natural Number in reverse order
def PrintN_ODD_reverse(n):
    if n>0:
        print(2*n-1,end=' ')
        PrintN_ODD_reverse(n-1)
       
PrintN_ODD_reverse(10)
print()

#Print First N Even natural Number  in reverse order
def PrintN_Even_reverse(n):
    if n>0:
        print(2*n,end=' ')
        PrintN_Even_reverse(n-1)
        
PrintN_Even_reverse(10)
print()
#Sum of first N natural Number

def Sum_N(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n+Sum_N(n-1)
r=Sum_N(6)
print(r)
print()

#Sum of first N  odd natural Number
def Sum_N_odd(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return 2*n-1 + Sum_N_odd(n-1)
r=Sum_N_odd(10)
print(r)
print()

#Sum of first N  Even natural Number
def Sum_N_Even(n):
    
    if n==1:
        return 2
    return 2*n + Sum_N_Even(n-1)
r=Sum_N_Even(1)
print(r)




#Factorial of a  Number

def Fact(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return n*Fact(n-1)
r=Fact(3)
print(r)


#Sum of Squares first N natural Number

def Sum_N_Squares(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n*n+Sum_N_Squares(n-1)
r=Sum_N_Squares(3)
print(r)