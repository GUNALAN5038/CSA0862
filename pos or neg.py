a=eval(input("enter the 1st numder: "))
b=eval(input("enter the 2nd numder: "))
c=eval(input("enter the 3rd numder: "))
if(a>b):
    if(a>c):
        print(a," is the greatest")
    else:
        print(c," is the greatest")
elif(b>c):
    print(b," is the greatest")
else:
    print(c," is the greatest")
