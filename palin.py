n=int(input("enter the number: "))
a=n
sum=0
while(n>0):
    b=n%10
    sum=sum*10+b
    n=n//10
if(sum==a):
    print("it is palin")
else:
    print("not")
