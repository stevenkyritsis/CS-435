#########################
#   insertion-sort.py   #
#   Steven Kyritsis     #
#   9-22-23             #
#   Insertion sort with #
#   a runtime timer     #
#########################
import time
start = time.time()
def insert_sort(a, n):
    for i in range(1,n):
        j=i
        while(j>0 and a[j]<a[j-1]):
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
            j=j-1
    return a

arr = [70, 40, 1, 14, 53, 21, 50, 98, 39, 3, 17, 30, 8, 93, 51, 83, 35, 18, 91, 54, 100, 75, 67, 41, 73, 61, 66, 92, 74, 85, 57, 29, 2, 72, 69, 12, 76, 31, 43, 22, 19, 58, 99, 27, 16, 42, 44, 25, 15, 96]
print("Input array:\t", arr)
print("Sorted array:\t", insert_sort(arr,len(arr)))
end = time.time()
print("Runtime: ",end-start)