#!/usr/bin/env python3
from __future__ import division

'''
Created on Jun 17, 2016

@author: fanxueyi
'''


#open the file 
file = 'test.txt'
data_file = open(file)
num = int(data_file.readline().rstrip("\n"))
data = data_file.read().rstrip('\n').split(' ')
data = [int(i) for i in data]

print(data)


heap_list = []
heap_list.append(data[num-1])

def add(heap_list,value):
    count = len(heap_list)
    heap_list.append(value)
    count = count + 1
    maxHeapify(count, heap_list) 
    return heap_list

def swap_value(a,b):
    med = a
    a = b
    b = med
    return (a,b)
    
    
def maxHeapify(count, heap_list):
    i = count-1
    while (i>0 and heap_list[int(i)] > heap_list[int((i-1)/2)]):
        (heap_list[int(i)], heap_list[int((i-1)/2)]) = swap_value(heap_list[int(i)], heap_list[int((i-1)/2)]) 
        i = (i-1)/2

for i in range((num-2), -1,-1):
    #print(data[i])
    heap_list = add(heap_list, data[i])

print(*heap_list, ' ')