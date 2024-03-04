uppercase=0
lowercase=0
number=0
print("enter * to exit")
while True:
    char=input("Enter any character: ")
    if char=='*':
        break
    elif char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        number+=1
print("\nTotal count of lower case:", lowercase)
print("Total count of upper case:",uppercase)
print("Total count of numbers:",number)
