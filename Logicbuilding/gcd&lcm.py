a=int(input("enter a number="))
b=int(input("enter a number="))
x=a
y=b
#r=a%b
while(a%b!=0):
    r1=a%b
    a=b
    b=r1
gcd=b
print("Gcd =",gcd)
print(f"Gcd of {x} and {y} is ",b)
lcm=(x*y)//gcd
print("Lcm= ",lcm)