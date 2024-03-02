a=0
b=0
n=int(input("enter the number: "))
for i in range(1,n+1,1):
  if(i%2==0):
      a+=i
  else:
      b+=i
print(a,"sum of even: ")
print(b,"sum of odd: ")
