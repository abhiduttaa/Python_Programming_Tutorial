a = int(input("enter 1st Number="))
b = int(input("enter 2nd Number="))
c = int(input("enter 3rd Number="))
# z=max(a,b,c)
# print(z ,"is a maximum Number")
if(a>b and a>c):
    print("a is greater that is =" , a)
elif(b>c and b>a):
    print("b is greater that is =" , b)
else:
    print("c is greater that is =" , c)