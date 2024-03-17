# def add(a,b):
#     return a+b
# x=add
# print(id(x))
# print(x)


# k=(lambda a,b : a+b)(3,4)
# print(k)

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

f=lambda n: 1 if n==0 or n==1 else n*f(n-1)

f(5)