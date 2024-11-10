n=int(input("enter a no="))
c=0
while(n>0):
    a=n%10
    n=n//10
    if(a==0):
        c=c+1
if(c>=1):
    print("Duck Number")
else:
    print("Non-Duck Number")