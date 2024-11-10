n=int(input("enter a no="))
s=0
x=n*n
while(x>0):
    r=n%10
    s=s+r
    n=n//10
if(s==n):
    print("neon number")
else:
    print("not neon number")