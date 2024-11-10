n=int(input("Enter The Number= "))
s=0
x=n
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
print("The Reverse number is =",s)