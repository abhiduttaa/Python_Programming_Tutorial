def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def square(a,b):
    x=a**2
    print("square of a is ",x)
    y=b**2
    print("square of b is ",y)
def squareroot(a,b):
    m=a**0.5
    print("squareroot of a is ",m)
    n=b**0.5
    print("squareroot of b is ",n)
a=float(input("enter 1st number="))
b=float(input("enter 2nd number="))
s=sum(a,b)
print("sum =",s)
subtration=sub(a,b)
print("subtration =",subtration)
multiplication=mult(a,b)
print("multiplication =",multiplication)
division=div(a,b)
print("division =",division)
square(a,b)
squareroot(a,b)