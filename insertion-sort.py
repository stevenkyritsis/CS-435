#########################
#   insertion-sort.py   #
#   Steven Kyritsis     #
#   9-22-23             #
#   Insertion sort with #
#  a comparison counter #
#########################\

# Import random from numy to generate random number
from numpy import random

# Define insertion sort function
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

print("##########PART 1##########\n")

# 1a Test for best case [n=32]
print("Input array:\t", arr, "\n")
sorted, count = insert_sort(arr,len(arr))
print("Sorted array:\t", sorted,
      "\nBest case comparisons: ", count, "\n")

# 1b Test for worst case [n=32]
arr.reverse()
print("Input array:\t", arr, "\n")
sorted, count = insert_sort(arr,len(arr))
print("Sorted array:\t", sorted,
      "\nWorst case comparisons: ", count, "\n")

# 1c Test for average case [n=32]
arr = random.choice(range(33), 32, replace=False) # Testing with random integers between 1-32
print("Input array:\t", arr, "\n")
sorted, count = insert_sort(arr,len(arr))
print("Sorted array:\t", sorted,
      "\nAverage case comparisons: ", count, "\n")

#######################################################################################

print("\n##########PART 2##########\n")

# 2a Test random integers array[n=100]
arr = random.choice(range(101), 100, replace=False) # Testing with random integers between 1-100
sorted, count = insert_sort(arr,len(arr))
print("Comparisons for 100 integers: ", count, "\n")

# 2b Test random integers array[n=1000]
arr = random.choice(range(1001), 1000, replace=False) # Testing with random integers between 1-1000
sorted, count = insert_sort(arr,len(arr))
print("Comparisons for 1,000 integers: ", count, "\n")

# 2c Test random integers array[n=10000]
arr = random.choice(range(10001), 10000, replace=False) # Testing with random integers between 1-10,000
sorted, count = insert_sort(arr,len(arr))
print("Comparisons for 10,000 integers: ", count, "\n")