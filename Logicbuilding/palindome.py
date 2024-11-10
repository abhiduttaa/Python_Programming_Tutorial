n=int(input("Enter a number="))
s=0
x=n
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
if(s==x):
    print("Palindrome and the number is ",x)
else:
    print("Not-palindrome")