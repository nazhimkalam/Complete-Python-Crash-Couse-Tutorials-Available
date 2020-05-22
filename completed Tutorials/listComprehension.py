#List comprehension

#What exactly is list comprehension?
#---> We are able to create a list with element by simply writing a piece of code inside the []

#SYNTAX of writing a List comprehension
#--->  [ codeOfIterable  rangeOfValues  ConditionOfTheIterable ]
#NOTE: the variable used has to be the same for all (codeOfIterable, rangeOfValues, ConditionOfTheIterable)

#Example 01 (all the numbers from 0 to 9)
list1 = [x for x in range(10)]
print(str(list1) + ' all the numbers from 0 to 9')

#Example 02 (square number from the range 0 to 9)
list2 = [x**2 for x in range(10)]
print(str(list2) + ' square number from the range 0 to 9')

#Example 03 (list of all the number which are a factor of 5 from 0 to 100)
list3 = [x for x in range(101) if x%5==0]
print(str(list3) + ' list of all the number which are a factor of 5 from 0 to 100')

#Example 04 (list of numbers greater than 20 and less than 40 from numbers 0 to 50)
list4 = [x for x in range(51) if x>20 and x<40]
print(str(list4) + ' list of numbers greater than 20 and less than 40 from numbers 0 to 50')

#We can have a list in a list, since we don't have 2d arrays in python this is similar to it like a 2d list
twoDList = [[1,2,3,4,5],['a','b','c','d','e']]
print('This is the third element from the first list element ' + str(twoDList[0][2]))
print('This is the third element from the second list element ' + str(twoDList[1][2]))
