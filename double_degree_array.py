#!/usr/bin/env phthon

with open('rosalind_ddeg.txt', 'r') as file1:
    first_line = file1.readline().split()
    first_line = [int(x) for x in first_line]
    array = file1.readlines()
    array2 = []
    for item in array:        
        item = item.strip('\n')
        item = item.split(" ")
        item = [int(x) for x in item]
        array2.append(item)

def get_degree(array,first_line):
    degree_dict = {}
    for i in range(first_line[0]):
        keynumber = i+1
        degree_dict[str(keynumber)]= 0 
    for lis in array:
        degree_dict[str(lis[0])]+=1
        degree_dict[str(lis[1])]+=1
    return degree_dict


def get_neighbor(array,first_line):
    neighbor_list = []
    for i in range(first_line[0]):
        neighbor_list.append([]) 
    for pair in array:
        neighbor_list[pair[0]-1].append(pair[1]-1)
        neighbor_list[pair[1]-1].append(pair[0]-1)
    return neighbor_list




def get_sum_of_degree(array,first_line):
    degree_dict = get_degree (array, first_line)
    neighbor_list = get_neighbor(array,first_line)
    sumDegree = []
    for lis in neighbor_list:
        if lis == []:
            sumDegree.append(0)
            continue
        total = 0
        for item in lis:
            total += degree_dict[str(item+1)]
        sumDegree.append(total)
    return sumDegree

sumDegree = get_sum_of_degree(array2,first_line)
sumDegree = [str(x) for x in sumDegree]
print " ".join(sumDegree)
    



        
