#!/usr/bin/env python3
from __future__ import division




'''
Created on Jun 22, 2016

@author: fanxueyi
'''

#quick sort using pivot median strtegy

file = "test.txt"
with open(file) as file_data:
    length = int(file_data.readline().rstrip("\n"))
    array = file_data.readline().rstrip("\n").split(" ")
    array = [int(i) for i in array]


def quick_sort(array):
    equal = []
    greater = []
    less=[]
    length = len(array)
    if length == 0:
        empty = []
        return empty
    if length == 1:
        return array
    pivot = array[length//2]
    for i in range(0,length):
        if array[i] == pivot:
            equal.append(array[i])
        if array[i] < pivot:
            less.append(array[i])
        if array[i] > pivot:
            greater.append(array[i])
    return (quick_sort(less)+equal+quick_sort(greater))
    
result = quick_sort(array)
print(*result)
