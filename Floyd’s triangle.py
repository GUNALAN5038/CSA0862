n=int(input("enter a number: "))
a=0
for i in range(1,n+1):
    for j in range(1,i+1):
        a=a+1
        print(a,end=' ')
    print( )
