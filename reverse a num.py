a=input("enter the number: ")
x=len(a)
a=int(a)
sum=0
for i in range(0,x,1):
    n=a%10
    sum=sum*10+n
    a=a//10
print(sum)

    
