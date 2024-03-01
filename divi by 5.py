n=eval(input("enter the number: "))
for i in range(1,n+1,1):
    if(i%5==0):
        print(i," divisible by 5")
    else:
        print(i," not divisible by 5")
