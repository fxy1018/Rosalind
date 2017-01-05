#!/usr/bin/env python

########################
#to merge two sorted array
#sample dataset:
#4
#2 4 10 18
#3
#-5 11 12
#sample output:
#-5 2 4 10 11 12 18
#########################

#open the dataset and convert the type of all data to interger 
with open("rosalind_mer.txt",'r') as file1:
    len_A  = int(file1.readline())
    arrayA = file1.readline().split()
    arrayA = [int(x) for x in arrayA]
    len_B  = int(file1.readline())
    arrayB = file1.readline().split()
    arrayB = [int(x) for x in arrayB]

# len_A, arrayA, len_B, arrayB = file1.readlines()


#function is to do the merge sorted arrays

def merge_array(len_A, arrayA, len_B, arrayB):
    merged_array = []
    a = 0
    b = 0
    while (a<len_A or b < len_B):
        if a>=len_A:
            merged_array = merged_array + arrayB[b:]
            break
        elif b>=len_B:
            merged_array = merged_array + arrayA[a:]
            break
        elif arrayA[a] <= arrayB[b]:
            merged_array.append(arrayA[a])
            a += 1
        else:
            merged_array.append(arrayB[b])
            b += 1
    return merged_array


def merge_sort(a,b):
    sorted = []
    while a and b:
        if a[0]>b[0]:
            sorted += [b.pop(0)]
        else:
            sorted += [a.pop(0)]
    sorted += a + b
    return sorted




merged_array = merge_array(len_A, arrayA, len_B, arrayB)
merged_array = [str(x) for x in merged_array]
print " ".join(merged_array)

#for i in merged_array:
#    print i,



    
