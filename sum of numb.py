a=eval(input("enter the number: "))
sum=0
for i in range(1,a,1):
    sum+=a%10
    a//=10
    print(sum)
