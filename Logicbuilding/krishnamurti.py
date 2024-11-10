#A Krishna Murty number is a number that is equal to the sum of the factorial of all its digits. For example, 1, 2, and 145 are Krishna Murty numbers. 
 
# The word "Krishnamurti" is a compound of Sanskrit words that means "in the form of Krishna". It comes from the Hindu deity Krishna and the term murti which means "form"

n=int(input("Enter a number="))
s=0
x=n
while(n>0):
    r=n%10
    n=n//10
    f=1
    while(r>1):
        f=f*r
        r=r-1
    s=s+f
if(x==s):
    print(f"{x} is a Krishnamurti Number")
else:
    print(f"{x} is not a Krishnamurti Number")