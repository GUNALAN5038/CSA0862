a=0
b=1
print(a,",",b)
for i in range(1,11,1):
    c=a+b
    a=b
    b=c
    print(c)
    
