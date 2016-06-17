#!/usr/bin/env python

#####################
#to do merge sort which is a divide and conquer strategy
#sample dataset
#10
#20 19 35 -18 17 -20 20 1 4 4
#sample output
#-20 -18 1 4 4 17 19 20 20 35
#####################

with open("rosalind_ms.txt",'r') as file1:
    num, array = file1.readlines()
    num   = int(num)
    array = array.split()
    array = [int(x) for x in array]

#to make a function to do the recursion

def merge_sort(a,b):
     sorted = []
     while a and b:
         if a[0]>b[0]:
             sorted += [b.pop(0)]
         else:
             sorted += [a.pop(0)]
     sorted += a + b
     return sorted

def divide_array(array):
    length = len(array)
    array1 = array[:length/2]
    array2 = array[(length/2):]
    return array1,array2

def mergeSort(array): 
    array1,array2 = divide_array(array)
    if len(array1)==1 and len(array2)==1:
        return merge_sort(array1,array2)
    elif len(array1)==1 and len(array2) ==2:
        if array2[0] > array2[1]:
            array2[0],array2[1] = array2[1],array2[0]
        return merge_sort(array1,array2)
    else:
        return merge_sort(mergeSort(array1),mergeSort(array2))

        

array =  mergeSort(array)
for item in array:
    print item,





