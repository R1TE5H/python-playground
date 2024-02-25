# Function to Print a Range of Numbers
def recursive(num1, num2):
    if num1 <= num2:
        print(num1)
        recursive(num1+1, num2)
    else:
        return


# Function to Add a Range of Numbers Together
def summation(num1, num2):
    if num1 > num2:
        return 0
    return num1 + summation(num1+1, num2)


# Function to Double a Number Using Lambda
double = lambda num: num*2

# print(double(10)) --> 20

# Function to Print the sum of 3 Parameters
sumFinder = lambda a,b,c: a + b + c

print(sumFinder(1,2,9))

# Function to Print Last Fibonacci Sequence Number
def fibonacci(end):
    if end == 1:
        return 0
    elif end == 2:
        return 1
    else:
        fib1, fib2 = 0, 1
        for i in range(end -2):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2


# Function to Calculate Factorial Non-Recursive
def factorial(num):
    ans = num
    while(num > 1):
        num -=1
        ans *= num
    print(ans)
    
factorial(6)

# Recursive Function to Calculate the Power of a Number
def power(base, exponent):
    if exponent == 0:
        return 1
    else: 
        return base*power(base, exponent-1)
print(power(2,4))