#!/usr/bin/env python

#######################
#to test whether it is esist that A[p]=-A[q] and get the location
######################
#sample dataset
#4 5
#2 -3 4 10 5
#8 2 4 -2 -8
#-5 2 3 2 -4
#5 4 -5 6 8
#################
#sample output
#-1
#2 4
#-1
#1 3
###################

#open file 
with open('rosalind_2sum.txt', 'r') as file1:
    first_line = file1.readline().split()
    first_line = [int(x) for x in first_line]
    line_matrix= file1.readlines()
    array      = []
    for line in line_matrix:
        array.append(line.split())

def find_indices(line):
    line = [int(i) for i in line]
    result = []
    for i in range(len(line)):
        element = line[i]
        index_e = i
        sub_line = line[(index_e+1):]
        for j in range(len(sub_line)):
            i = sub_line[j]
            if element == -i:
                index1 = index_e
                index2 = j+index_e+1
        #        print line[index1]
         #       print line[index2]
                result.append(index1+1)
                result.append(index2+1)
                return result
    return -1

for line in array:
    result = find_indices(line)
    if result == -1:
        print result
    else:
        for i in result:
            print i,
        print
#modified:
#we can sort the line first with running time O(NlogN)
#then small=0, large = n-1
#if L[small] + L[large]>0 : large-1
#if L[small] + L[large]<0 : small+1
#continued until L[small]+L[large]=0 or small=large
