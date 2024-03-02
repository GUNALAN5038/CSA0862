#n=eval(input("enter the year: "))
for i in range(1500,2401,1):
    if(i%400==0)or(i%4==0 and i%100!=0):
        print("it is leap year",i)
else:
    print("not a leap year")
