#!/usr/bin/env python3
from __future__ import division

'''
Created on Aug 18, 2016

@author: fanxueyi
'''


with open('rosalind_ini.txt','r') as f1:
    dna = f1.readline().strip("\n")
    A = dna.count("A")
    T = dna.count("T")
    C = dna.count("C")
    G = dna.count("G")
    output = " ".join(str(x) for x in [A,C,G,T])
    #print(output)
    
    
    
nums = [ 0,1,0, 3, 12]   

def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if (nums.count(0)==0):
            return(nums)
        else:
            dock = len(nums)
            index = nums.index(0)
            while (dock != index):
                for i in range(index,4):
                    nums[i]=nums[i+1]
                nums[4]=0
                dock = dock-1
                index = nums.index(0)
            return(nums)
print(moveZeroes(nums))