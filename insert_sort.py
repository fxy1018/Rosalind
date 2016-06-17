#!/usr/bin/env python

with open('rosalind_ins.txt','r') as f1:
    n = int(f1.readline())
    A = f1.readline().split()

def insertionsort(n,A):
    count = 0
    for i in range(1,n):
        k = i
        while (k > 0 and int(A[k]) < int(A[k-1])):
            A[k-1], A[k] = A[k],A[k-1]
            count +=1
            k = k-1
    return count

print insertionsort(n,A)
