#There are 3 ways of formatting when printing
name ='Nazhim'
age = 19    
 
#Method 01
print('%s is %d years old'%(name,age))  #there are special formatting characters used such as (s,d) & order of the variables matters

#Method 02
print('{} is {} years old'.format(name,age)) #if the position is not mentioned then the order of the variables matters

#Method 03
print(f'{name} is {age} years old')     #variables names goes into the {}

#Rounding up decimal values
val = 12.63356449
print(f'{val:.2f}')
print(f'{val:.5f}')

#Width specifier
for i in range (1,6):
    print(f'{i : 2} {i*i : 3} {i*i*i : 10}')

#by default strings are left justified, by using '>' character we can move it to right
s1 = 'a'
s2 = 'ab'
print(f'{s1:>10}') #we move 'a' by 10 charatcers to the right
print(f'{s2:>50}') #we move 'a' by 50 charatcers to the right
