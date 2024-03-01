for num in range(1, 10001):
    temp = num
    sum= 0
    for i in range(1, num):
        if num % i == 0:
            sum+= i
    if sum== temp:
        print(num, "is a perfect number")
