n=int(input("enter a number \n"))
temp=n
rev=0
num=0
while(n!=0):
    num=n%10
    rev=rev*10
    rev+=num
    n=n//10
print(rev)
