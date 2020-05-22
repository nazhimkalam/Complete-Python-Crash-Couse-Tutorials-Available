import time                            #WE IMPORT THE TIME MODULE
import calendar
# Modules can be classes, functions, variables where you have python code already written into it and then you call them when needed

#getting current time
local = time.localtime(time.time())
print('Local current time ' + str(local))

#getting formatted time
formattedTime = time.asctime(time.localtime(time.time()))
print('\nLocal current time ' + str(formattedTime))

#producing a calender for a month
cal = calendar.month(2008,1)
print('\nHere is the calender\n')
print(cal)


