n=int(input("enter a no="))
s=0
p=1
x=n
while n>0:
    r=n%10
    s=s+r
    p=p*r
    n=n//10
if s+p == x:
    print("special number")
else:
    print("non-special number")