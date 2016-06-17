#!/usr/bin/env python

######################
#to find an array whether it has a majority element
######################
#sample dataset
#4 8
#5 5 5 5 5 5 5 5
#8 7 7 7 1 7 3 7
#7 1 6 5 10 100 1000 1
#5 1 6 7 1 1 10 1
#################
#sample output
#5 7 -1 -1
#####################

#open file and change all element to interger
with open("rosalind_maj.txt", "r") as file1:
    first_line = file1.readline().split()
    first_line = [int(x) for x in first_line]
    num_list   = first_line[0]
    length     = first_line[1] 
    array      = file1.readlines()
    arr_list   = []
    for line in array:
        arr_list.append(line.split())

    

#create a function to test whether a list has majority element 
    
def whether_majority(line,length):
    for i in line:
        if line.count(i) > length/2:
            return i
    return -1

#create a function to get the list of results

def get_results(arr_list,length,num_list):
    result = []
    for line in arr_list:
        return_value = whether_majority(line,length)
        result.append(return_value)
    return result

#print out the result

result = get_results(arr_list,length, num_list)
for i in result:
    print i,

        



    
    
