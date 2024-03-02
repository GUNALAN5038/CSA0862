n=1000
a=n
sum=0
for i in range(1,n,1):
    b=n%10
    sum=sum+b*b*b
    n=n//10
if(sum==a):
    print("it is armstrong")
else:
    print("not")
