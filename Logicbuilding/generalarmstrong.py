#Armstrong Number
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153, and 4679307774.

#q..What is the Armstrong number?
# =>What is the Armstrong Number? An Armstrong number is a special kind of number in math. It's a number that equals the sum of its digits, each raised to a power. For example, if you have a number like 153, it's an Armstrong number because 1^3 + 5^3 + 3^3 equals 153.

n=int(input("Enter a number="))
s=0
x=n
c=0
while(n>0):
    n=n//10
    c=c+1
n=x
while(n>0):
    r=n%10
    s=s+pow(r,c)
    n=n//10
if(x==s):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")