n=int(input("enter a number:\n"))
found=0
for i in range(2,n):
    if(n%i==0):
        found=1
        break
if(found==0):
    print("prime")
else:
    print("not prime")
