#########################
#   insertion-sort.py   #
#   Steven Kyritsis     #
#   11-10-23            #
#   Sorting Strings LSD #
#########################
import sys
# 1. Read the strings from a text file "f.txt"
# Assume that each string starts at the beginning of a new line and ends with one or more white space characters
f = open(sys.argv[1], "r")
lines = f.read().splitlines()

# Store the strings in a two-dimensional array S with n rows and k columns
n = len(lines)
k = max(len(line) for line in lines)
S = [[''] * k for _ in range(n)]
for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        S[i][j] = char

def radix_sort(S):
    # Find the maximum length of a string in S
    max_len = max(len(s) for s in S)
    for i in range(len(S)):
        if len(S[i]) < max_len:
            S[i] = S[i] + ' ' * (max_len - len(S[i]))

    indexes = list(range(len(S)))
    for index in range(max_len):
        buckets = [[] for _ in range(256)]
        for i in indexes:
            if(S[i][index] != ''):
                buckets[ord(S[i][index])].append(i)
            else:
                buckets[0].append(i)

        indexes = [i for bucket in buckets for i in bucket]

    return indexes

# second output file openning in write mode
g = open(sys.argv[2], "w")

# writing the output to the output file
for i in radix_sort(S):
    g.write(lines[i] + "\n")
g.close()