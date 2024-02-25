# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:55:20 2023

@author: Owner
"""

# Create a Function that Takes in Numbers and returns the average

def calculate_average(numList):
    sumVal = sum(numList)
    return sumVal / len(numList)

print(calculate_average([1,2,2.5,4.5,5]))

#---------------------------------------------------------------------------------------

# Reverse a String

def reverse_string(string):
    newList = []
    newString = ""
    
    for element in string:
        newList.insert(0, element)
    for element in newList:
        newString += element 
    
    print(newString)

reverse_string("NoWay")

#-----------------------------------------------------------------

def merge_dictionaries(dict1, dict2):

    newDictionary = dict(dict1)
    newDictionary.update(dict2)  
    return newDictionary

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

result = merge_dictionaries(dict1, dict2)
print(result)


