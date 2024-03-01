n=int(input("enter a nmber: "))
temp=n
d=0
arm=0
while n!=0:
    d=d+1
    n=n//10
n=temp
while n!=0:
    a=n%10
    arm+=pow(a,d)
    n=n//10
if (arm==temp):
    print("ARMSTRONG NUMBER")
else:
    print("not a armstrong number")
