n=int(input("enter a no="))
x=n
s=0
while(x>0):
    r=x%10
    s=s*10+r
    x=x//10
if(s==n):
    print("palindorme")
else:
    print("non-palindrome")