n=int(input("enter a no:"))
flag=0
for i in range(2,n//2,1):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print(f"{n} is prime Number")
else:
    print(f"{n} is not a prime number")