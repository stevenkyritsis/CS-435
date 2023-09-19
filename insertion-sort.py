#########################
#   insertion-sort.py   #
#   Steven Kyritsis     #
#   9-22-23             #
#   Insertion sort with #
#  a comparison counter #
#########################\

#1. import random from numy to generate random number
from numpy import random

#2. define insertion sort function
def insert_sort(a, n):
    compcount = 0
    for i in range(1,n):
        j=i
        while(j>0 and a[j]<a[j-1]):
            compcount += 1
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
            j=j-1
    return a, compcount

# Creating the array [n=32]
arr = []
for i in range(1,33):
    arr.append(i)

# Test for best case [n=32]
print("Input array:\t", arr)
sorted, count = insert_sort(arr,len(arr))
print("Sorted array:\t", sorted,
      "\nBest case comparisons:\t", count, "\n")

# Test for worst case [n=32]
arr.reverse()
print("Input array:\t", arr)
sorted, count = insert_sort(arr,len(arr))
print("Sorted array:\t", sorted,
      "\nWorst case comparisons:\t", count, "\n")

# Test for average case [n=32]
arr = random.randint(32, size=(32)) # Testing with random integers between 1-32
print("Input array:\t", arr)
sorted, count = insert_sort(arr,len(arr))
print("Sorted array:\t", sorted,
      "\nAverage case comparisons:\t", count, "\n")

# Test 