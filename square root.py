import math
n=int(input("enter number: "))
s=math.sqrt(n)
if s.is_integer():
    print("perfect square")
else:
    print("not a perfect square")
