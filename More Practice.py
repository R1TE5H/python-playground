# Sort Integers into Specified Lists

my_list = [3, 7, 12, 5, 8, 2, 15, 6, 9]

g10 = []
b510 = []
l5 = []

for element in my_list:
    if element > 10:
        g10.append(element)
    elif element < 5:
        l5.append(element)
    else:
        b510.append(element)
        
#print(g10, b510, l5)

#------------------------------------------------------------------------

# Create a Dictionary with the length of the sorted lists from above

#my_list = [3, 7, 12, 5, 8, 2, 15, 6, 9]
counter1 = 0
counter2 = 0    
counter3 = 0
dictionary = {}

for element in my_list:
    if element > 10:
        counter1 += 1
    elif element < 5:
        counter2 += 1
    else:
        counter3 += 1
        
dictionary["Greater Than 10"] = counter1
dictionary["Between 5 and 10"] = counter3
dictionary["Less than 5"] = counter2

print(dictionary)

#-------------------------------------------------------------------------

my_string = ["hello", "python", "world"]
my_dict = {}


for element in my_string:
    count = 0
    for char in element:
        if char.lower() in "aeiouy":
            count += 1
    my_dict[element] = count
print(my_dict)

# -------------------------------------------------------------------------
def highest_average_score(studentName):
    highestScore = 0
    highestStudent = " "
    
    for student, scores in studentName.items():
        averageScore = sum(scores)/len(scores)
        if averageScore > highestScore:
            highestScore = averageScore
            highestStudent = student
    return highestStudent, highestScore

print(highest_average_score({"Alice": [80], "Bob": [20]}))
            
#----------------------------------------------------------------------------

def findSecond(numList):
    unique = sorted(set(numList), reverse=True)
    if len(unique) >=2:
        return unique[1]
    return "No Second Largest Number"

print(findSecond([1,2,3,4,5,6]))

#-------------------------------------------------------------------------------

def numFunction(numList):
    unique = set(numList)
    sortedNum = sorted(unique)
    
    length = len(sortedNum)
    if length % 2 == 0:
        average = sortedNum[int(length/2)] + sortedNum[int(length/2)-1]
        average /= 2
        return average
    else:
        return sortedNum[int(length/2)]
    
print(numFunction([1,2,3,5,6,6]))

#-------------------------------------------------------------------------------

def numFunction2(numList):
    evenSum = 0
    oddSum = 0
    
    highest = max(numList)
    lowest = min(numList)    
    
    for num in numList:
        if num % 2 == 0 :
            evenSum += num
        else:
            oddSum +=num
    print(highest, lowest, evenSum, oddSum)
    
numFunction2([1,2,3,4])

#-------------------------------------------------

def oddEvenSorter(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
            
    return even, odd

numList = list(
    map(
        int, 
        input("Please Enter a list of Numbers Separated by a Comma: ").split(",")))

print(oddEvenSorter(numList))