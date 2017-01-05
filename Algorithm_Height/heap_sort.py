#!/usr/bin/env python3
from __future__ import division


'''
Created on Jun 21, 2016

@author: fanxueyi
'''
#The heap sort algorithm first transforms a given array into a max heap (recall the problem “Building a Heap”). It then repeats the following two simple steps
# n-1 times:
#Swap the last element of the heap with its root and decrease the size of the heap by 1.
#"Sift-down" the new root element to its proper place.



file = "test.txt"
with open(file) as file_data:
    length = int(file_data.readline().rstrip("\n"))
    array = file_data.readline().rstrip("\n").split(" ")
    array = [int(i) for i in array]

def add(heap_list,value):
    count = len(heap_list)
    heap_list.append(value)
    count = count + 1
    maxHeapify(count, heap_list) 
    return heap_list

def swap_value(a,b):
    a,b =b,a
    return (a,b)


    
def maxHeapify(count, heap_list):
    i = count-1
    while (i>0 and heap_list[int(i)] > heap_list[int((i-1)/2)]):
        (heap_list[int(i)], heap_list[int((i-1)/2)]) = swap_value(heap_list[int(i)], heap_list[int((i-1)/2)]) 
        i = (i-1)/2



#bulid the max heap
heap_list = []
heap_list.append(array[length-1])

for i in range((length-2), -1,-1):
    heap_list = add(heap_list, array[i])



###heap sort

def siftDown(count, heap_list):
    i = int(0)
    while (i+1)*2-1 <count:
        if heap_list[i] < heap_list[(i+1)*2-1] or heap_list[i] < heap_list[(i+1)*2]:
            if (i+1)*2 >count-1:
                (heap_list[i],heap_list[(i+1)*2-1]) = swap_value(heap_list[i], heap_list[(i+1)*2-1])
                i= (i+1)*2-1
            else:
                if heap_list[(i+1)*2-1] > heap_list[(i+1)*2]:
                    (heap_list[i],heap_list[(i+1)*2-1]) = swap_value(heap_list[i], heap_list[(i+1)*2-1])
                    i= (i+1)*2-1
                else:
                    (heap_list[i],heap_list[(i+1)*2]) = swap_value(heap_list[i], heap_list[(i+1)*2])
                    i = (i+1)*2
        else:
            return


def heap_sort(heap_list, length):
    end = length-1
    for i in range(1,length):
        if end > 0:
            (heap_list[0],heap_list[end]) = swap_value(heap_list[0], heap_list[end])
            siftDown(end,heap_list)
            end = end-1
    return heap_list  
print(*heap_sort(heap_list,length), sep= ' ')