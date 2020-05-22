# FILE HANDLING

# # Write into a file (In write mode we override the existing data)
# file = open('sample.txt','w')
# file.write('My name is Nazhim kalam\nI am 18 years old')
# file.close()

# # Appending data into a file
# file = open('sample.txt','a')
# file.write('\nI am a Data Scientist')
# file.close()

# # Reading from file using "readline()" this will return the a line from the file
# file = open('sample.txt','r')
# line = file.readline()
# print(line)

# # Reading from file using "readlines()" this will return a list of lines with \n at the end of each line
# file = open('sample.txt','r')
# line = file.readlines()
# print(line)

# # Reading from file using "read()" will return the entire file in a one string with the same format
# file = open('sample.txt','r')
# line = file.read()
# print(line)

# # Reading from file using "read(n)" this will return the number of characters specified within the brackets of read
# file  = open('sample.txt','r')
# line  = file.read(10)
# line1 = file.read(10)
# print(line)
# print(line1)

# # You can iterate and print
# file = open('sample.txt','r')
# for line in file:
#     print(line, end="")
# file.close()

# # Opening and  Automatic closing file using context manager
# with open('sample.txt','r') as file:
#     data = file.read()
# print(data)

