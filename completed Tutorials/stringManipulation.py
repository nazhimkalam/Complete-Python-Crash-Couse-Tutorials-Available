myString = 'Mohammed Nazhim Kalam'


#Ordering of index of a string example:
#------------------------    0 1 2 3 4 5 6 7    --------------------
#--------------------------  M o h a m m e d  ----------------------
#------------------------   -8-7-6-5-4-3-2-1    --------------------

#you can find the position of a string or character from the starting position as well but if you left it blank it starts from the default value 0
#if value not found it will return -1
print(myString.find('m'))
print(myString.find('m',15))


#accessing a character from a string
print(myString[0])      #this will display 'M'

#SLCIING A STRING

#POSITIVE NUMBER SLICING (starts with 0 and goes on)

#A part of a string from a string [starting character : one character after stop]
print(myString[0:8])    #this will display 'Mohammed'

#if you need all the elements at start but stops at a point [ : one character after stop]
print(myString[:16])    #this will display 'Mohammed Nazhim'

#if you need all the elements from a point till the end [starting character :]
print(myString[9:])    #this will display 'Nazhim Kalam'

#when you use [:] this means it starts at 0 and gives you all characters till the end
print(myString[:])

#NEGATIVE NUMBER SLICING (starts with the negative length number)
length_of_the_string = len(myString)
print(myString[-length_of_the_string]) #this will display 'M'
print(myString[-1])                    #this will display 'm'

tempString = 'Mohammed'
#if I need to extract 'ham' from tempString by Positive slicing
print(tempString[2:5])
#if I need to extract 'ham' from tempString by Negative slicing
print(tempString[-6:-3])

#STEPPING OR JUMP SLICING [start : end : step]
#NOTE: The slice step can never be zero

#So what happens is that it jump the number of times and takes that value with it 
print(tempString[0:8:1])  #this will display 'Mohammed'
print(tempString[0:8:2])  #this will display 'Mhme'
print(tempString[0:8:3])  #this will display 'Mae'
print(tempString[0:8:4])  #this will display 'Mm'

#SPLITTING A STRING

#during splitting it returns a list of splitted strings
#NOTE: always the first and the last character splitting will return an empty space into the list
#NOTE: when you have repeated characters such as example 'mm' if you split by 'm' it will return an extra empty space as well

newString = 'Mohammmed Nazzhimm kalam'
print(newString.split())
print(newString.split(' '))

print(newString.split('m'))
print(newString.split('M'))

#STRIPPING A STRING
#stripping means removing the excess whitespaces from the left ends and right ends
name = '          Nazhim            '      
print(name + ' kalam')                  #no stripping
print(name.strip() + ' kalam')          #strips both the ends
print(name.rstrip() + ' kalam')         #stripping the right end 
print(name.lstrip() + ' kalam')         #stripping the left end

#triple quote string format

para = '''My name is Nazhim kalam
I am 18 years old
I love Harry Potter'''

print(para)

#GETTING THE LENGTH OF THE STRING
print(len(para))


#converting all the characters into a lowercase()
print(para.lower())

#converting all the characters into a uppercase()
print(para.upper())

#converting the first character of every word in the text content to capital
print(para.title())

#converting only the first character of the first word in a string 
print(para.capitalize())

#replacing characters or part of a string from the main string
print(para.replace('Nazhim','Hashim'))

#checks if a character or a part of a string is present in another string
x = 'Nazhim' in para
y = 'Abdul' in para
print(x) #this returns True because 'Nazhim' is present in the string para
print(y) #this returns False because 'Abdul' is not present in the string para

#string concatination
name1 = 'Cristiano'
name2 = 'Ronaldo'
fullName = name1 + ' ' + name2

name2
print(fullName)

#we can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
age = 18            # index 0
player = 'Bolt'     # index 1
planet = 'Earth'    # index 2

txt = 'I am the fastest person on earth and I am {} years old'    #we can't place more than one {} for the same variable
print(txt.format(age))

newTxt = 'I am the fastest person on {}. My name is {} and I am {} old'
print(newTxt.format(planet,player,age))                           #order of the format variables entered matters if you don't put the index of the variables in the {}

nextNewTxt = 'I am the fastest person on {2}. My name is {1} and I am {0} old'
print(nextNewTxt.format(age,player,planet))                       #In this order doesn't matter because the indexes are placed within the {}

#ESCAPE CHARACTER
print("This is an \"escape\" character \"\\\" ")                  #displays This is an "escape" character "\"

#count() method counts the number of characters or a part of a string in a string
sample = "hello hello hi hi bye bye" 
print(sample.count('h'))                #this returns the number of 'h' characters in the string sample
print(sample.count('hi'))               #this returns the number of 'hi' string part in the string sample
print(sample.count('bye'))              #this returns the number of 'bye' string part in the string sample









