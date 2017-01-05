#!/usr/bin/env python3
from __future__ import division


'''
Created on Jun 21, 2016

@author: fanxueyi
'''

def swap(i,j):
    i,j = j,i
    
def heapify(end, i, array):
    left = 2*i+1
    right =2*(i+1)
    maxi = i
    if left < end and array[i] < array[left]:
        maxi = left
    if right < end and array[max] < array[right]:
        maxi = right
    if maxi != i:
        swap(i,max)
        heapify(end,max, array)

#array = [2,7,1,-2,56,5,3]
#heapify(6,)
print(6//3)