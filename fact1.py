def factorial(num):
    fact = 1
    for cnt in range(1, num+1):
        fact = fact*cnt
    return fact
number = int(input("Enter Number ="))
result = factorial(number)
print('factorial of %d : %d' %(number,result))
