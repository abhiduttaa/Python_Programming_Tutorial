n=int(input("enter a number="))
if(n%100!=0 and n%4==0 or n%100==0 and n%400==0):
    print("leap year")
else:
    print("not leap year")