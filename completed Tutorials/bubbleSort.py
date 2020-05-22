#The main difference between bubble sort and insertion sort is that
#bubble sort performs sorting by checking the neighboring data elements and swapping them if they are in wrong order
#while insertion sort performs sorting by transferring one element to a partially sorted array at a time.

#BUBBLE SORT
myList = [15,24,62,53,25,12,51]
maxIndex = 6  #remember its maxIndex not max number of elements
print('This is the unsorted list ' + str(myList))
n = maxIndex
for i in range(maxIndex):
    for j in range (n):
        if (myList[j] > myList[j+1]):
            temp = myList[j]
            myList[j] = myList[j+1]
            myList[j+1] = temp
    n-=1

print('This is the sorted list ' + str(myList))
