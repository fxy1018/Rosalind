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

def swap(a,b):
    a,b = b,a
    return (a,b)

def bubble_sort(array,length):
    for i in range(length-1):
        for j in range(length-1):
            #ascending order
            if array[j] > array[j+1]:
                (array[j],array[j+1]) = swap(array[j], array[j+1]) 
            #descending order
            #if array[j] < array[j+1]:
            #  (array[j],array[j+1]) = swap(array[j], array[j+1])                
    return array

print(bubble_sort(array,length))