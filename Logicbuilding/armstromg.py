#Armstrong Number
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153, and 4679307774.
n=int(input("Enter a number="))
s=0
x=n
while(n>0):
    r=n%10
    s=s+pow(r,3)
    n=n//10
if(x==s):
    print("Armstrong Number ")
else:
    print("Not-armstrong Number")