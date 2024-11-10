n=int(input("enter a no="))
s=0
x=n
while(n>0):
    r=n%10
    s=s+r
    n=n//10
if(x%s==0):
    print("harshad number")
else:
    print("not harshad number")