#!/usr/bin/env python3
from __future__ import division

#import two_way_partition

'''
Created on Jun 22, 2016

@author: fanxueyi
'''
#use median finding algorithm which use dived and conquer strategy


file = "test.txt"
with open(file) as file_data:
    length = int(file_data.readline().rstrip("\n"))
    array = file_data.readline().rstrip("\n").split(" ")
    array = [int(i) for i in array]
    k_th = int(file_data.readline().rstrip("\n"))

def three_way_partition(array,length):
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
    return(less,equal,greater)


def find_k_th_element(array, length, k_th):
    (less,equal,greater) = three_way_partition(array,length)
    if len(less)+len(equal)< k_th:
        k_th = k_th - len(less) - len(equal)
        length = len(greater)
        return find_k_th_element(greater, length, k_th)
    elif len(less) + len(equal) > k_th:
        if len(equal) == 0:
            new_list = less
        elif len(less) == 0:
            new_list= equal
        else:
            new_list = less+equal
        length= len(new_list)
        return find_k_th_element(new_list,length , k_th)
    else:
        final = less + equal
        k_th_num = final[-1]   
        return(k_th_num)   
print(find_k_th_element(array, length, k_th))
    