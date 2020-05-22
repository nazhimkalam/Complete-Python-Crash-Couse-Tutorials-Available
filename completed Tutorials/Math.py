# --> Python has a set of built-in math functions, including an extensive math module,
# that allows you to perform mathematical tasks on numbers.

# Built-in Math Functions

# MAX & MIN FUNCTION
x = min(5, 10, 25)  # used to return the minimum number from the given range
y = max(5, 10, 25)  # used to return the maximum number from the given range

print(x)
print(y)

# ABS FUNCTION
# -->  The abs() function returns the absolute (positive) value of the specified number
print(abs(-2.5516))  # gives you 2.5516

# POW FUNCTION
# -->  The pow(x, y) function returns the value of x to the power of y (x^y)
print(pow(2, 10))  # 2 to the power 10 gives 1024

# -----------------------------------------------------------------------------------------------------------

# Math Module
# -->  Python has also a built-in module called "math", which extends the list of mathematical functions.
# -->  To use it, you must import the math module:
# -->  When you have imported the math module, you can start using functions and constants of the module.

import math

# The math.sqrt() function, returns the square root of a number:
print(math.sqrt(64))   # returns 8.0
print(math.sqrt(100))  # returns 10.0

# The math.ceil() method rounds a number upwards to its nearest integer
# The math.floor() method rounds a number downwards to its nearest integer and returns the result
print(math.ceil(2.111))   # this returns 3
print(math.floor(2.999))  # this returns 2

# The math.pi constant, returns the value of PI (3.14...)
print(math.pi)            # 3.141592653589793

