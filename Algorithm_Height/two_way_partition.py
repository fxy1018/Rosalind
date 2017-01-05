#!/usr/bin/env python3
from __future__ import division

'''
Created on Jun 22, 2016

@author: fanxueyi
'''

file = "test.txt"
with open(file) as file_data:
    length = int(file_data.readline().rstrip("\n"))
    array = file_data.readline().rstrip("\n").split(" ")
    array = [int(i) for i in array]
    
#method1
def two_way_partition(array,length):
    pivot = array[0]
    less = []
    greater = []
    equal = [pivot]
    for i in range(1,length):
        if array[0] < array[i]:
            greater.append(array[i])
        elif array[0] > array[i]:
            less.append(array[i])
        else:
            equal.append(array[i])
    return(less+equal+greater)

#use filter
#"""a is the list of numbers"""
#par3 = list(filter(lambda i:i<a[0], a)) + list(filter(lambda i:i==a[0], a)) + list(filter(lambda i:i>a[0], a))


#method 2
def partition(array,num):
    for i in range(0,len(array)):
        current_num = array[i]
        if current_num <= num:
            del array[i]
            array.insert(0,current_num)
    return array

#method3
def par(A, i, a, b):
    while a < b:
        if A[b] > A[i]:
            b -= 1
        elif A[a] <= A[i]:
            a += 1
        else:
            A[a], A[b] = A[b], A[a]
    A[i],A[a] = A[a],A[i]
    return A


newarray = two_way_partition(array, length)  
print(*newarray, sep=" ")