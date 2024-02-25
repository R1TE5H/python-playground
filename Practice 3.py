# Imports
import time
import random

# Function that Takes an Integer and returns the largest Prime Factor
def primeCheck(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def largestPrimeFactor(num):
    largest = 0
    for i in range(2, num + 1):
        if num % i == 0 and primeCheck(i):
            largest = i
    return largest

#number = int(input("Enter a positive number: "))
#test = largestPrimeFactor(number)
#print("The largest prime factor of", number, "is", test)

# ---------------------------------------------------------------------------------------------------------

# Create 2 Fibonacci Number Functions and compare the time complexity
    # One should use a recusion and the other an iterative loop

# Notice the time Library imported at the top
def fibonacci_1(num):
    if num <= 1:
        return num
    else: 
        return fibonacci_1(num - 1) + fibonacci_1(num - 2)
    
def fibonacci_2(num):
    if num <= 1:
        return num
    a, b = 0, 1
    for i in range (num - 1):
        a, b = b, a + b
    return b

# Measure execution time for the recursive function
startTimeF1 = time.time()
resultF1 = fibonacci_1(30)
endTimeF1 = time.time()
elapsedTime = endTimeF1 - startTimeF1

# Measure Execution time for the iterative function
startTimeF2 = time.time()
resultF2 = fibonacci_2(30)
endTimeF2 = time.time()
elapsedTime2 = endTimeF2 - startTimeF2

# Print Values
#print("The Results of both functions are", resultF1, "and", resultF2)
#print("The execution times of each are", elapsedTime, "and", elapsedTime2)

# ---------------------------------------------------------------------------------------------------------

# Create the Leibniz Equation

def leibniz(iterations):
    piApprox = 0
    sign = 1
    divisor = 1
    
    while iterations > 0:
        piApprox += sign * (1 / divisor)
        sign *= -1
        divisor += 2
        iterations -= 1 
    
    return piApprox * 4

#number = int(input("Enter the number of iterations: "))
#print(leibniz(number))

# ---------------------------------------------------------------------------------------------------------

# Create a program than takes a series of numbers and returns the sum and average

def sumFinder(numList):
    sums = 0
    for element in numList:
        sums += element
    return sums

def average(numList):
    length = len(numList)
    return sumFinder(numList)/length

nums = input("Please Enter a list of numbers separated by a comma: ")
nums = nums.split(",")

numList = []

for item in nums:
    numList.append(int(item))
    
#print("The Sum of the List is", sumFinder(numList), "and the Average is", average(numList))

# ---------------------------------------------------------------------------------------------------------

# Create a program that populates an empty dictionary where keys are user inputted names, and values are
# random numbers from 1 to 100

# Notice the random library imported at the top

studentDictionary = {}
numStudents = int(input("Please enter the number of students: "))

for i in range(numStudents):
    studentName = input("Please enter the name of a student: ")
    grade = random.randint(1, 100)
    studentDictionary[studentName] = grade
    
#print(studentDictionary)

# ---------------------------------------------------------------------------------------------------------








