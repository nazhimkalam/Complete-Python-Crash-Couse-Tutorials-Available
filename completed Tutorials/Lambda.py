# A lambda function is a small 'anonymous function'.
# A lambda function can take 'any number of arguments, but can only have one expression'.

# SYNTAX :
#    functionName = lambda arguments: expression

# The "expression" is executed and the "result is returned"
# Since lambda uses anonymous functions we don't declare it as def functionName()

# Example 01 (A lambda function that adds 10 to the number passed in as an argument, and print the result):
x = lambda a: a + 10  # x is the "anonymous function", (a: a +10) in this the first 'a' is the parameter we send,
# the rest is the code expression
print(x(5))  # This will return 15 because "a + 10" means 5 + 10, the result 15 is returned to the variable x

# Example 02 (A lambda function that multiplies argument a with argument b and print the result):
result = lambda a, b: a * b
print(result(2, 3))

# Example 03 (A lambda function that sums argument a, b, and c and print the result):
sumOfTheNumbers = lambda a, b, c: a + b + c
print(sumOfTheNumbers(10, 20, 50))

# ----------------------------------------------------------------------------------------------------------------------
# VERY IMPORTANT NOTE: The power of lambda is better shown when you use them as an anonymous function inside another function.
# example for an anonymous function is x = lambda a: a + 10

# Example 01
# Using this function to make a function that always doubles the number you send in:
def myFunc(n):
    return lambda a: a * n

myDoubler = myFunc(2)  # myDouble behaves like an Anonymous function, so it will have direct access to the lambda expression
# the "2" gets fixed to the "n", and that function belongs to myDouble
print(myDoubler(4))    # this will return 8
print(myDoubler(20))   # this will return 40
print(myDoubler(5))    # this will return 10
print(myDoubler(45))   # this will return 90

myTriple = myFunc(3)
print(myTriple(2))  # 6
print(myTriple(5))  # 15
print(myTriple(1))  # 3
print(myTriple(10)) # 30
print(myTriple(50)) # 150

