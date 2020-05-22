#The nonlocal keyword is used to work with variables inside nested functions,
#where the variable should not belong to the inner function.

#Use the keyword nonlocal to declare that the variable is not local.

#Example 01 (with nonlocal)
def myfunc01():
  x = "John"       #x is 'John'
  def myfunc02():
    nonlocal x     #this refers to the previous x
    x = "hello"    #and now has become 'hello'
  myfunc02()
  return x          #hence this will be 'hello'

print(myfunc01())


#Example02 (without nonlocal)
def myfunc1():
  x = "John"       #this will be 'John'
  def myfunc2():
    x = "hello"    #this doesn't refer to the previous x, its a new x
  myfunc2()
  return x

print(myfunc1())

#Example03 (global scope)
global a
a = 10
def hi():
    a = 52
    print(a) #52 output
hi()
print(a)     #10 output

#Example 04 (local scope)
s = 10        #these are by default made global
def myfucn():
    b = 7     #variables inside a function are said to be local
    print(b) # displays 7
    print(s) # displays 10

myfucn()
print(b)  # displays that b is not defined since its local to the function myfunc()
