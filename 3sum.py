#!/usr/bin/env python

#####################
#3sum algorithm
####################

def indices_3sum(line,ele_num):
    for i in range(ele_num-3):
        a = line[i]
        start = i + 1
        end = ele_num-1
        while (start < end):
            b = line[start]
            c = line[end]
            if (a+b+c ==0):
                return (a,b,c)
            elif (a+b+c >0):
                end = end-1;
            else:
                start = start+1
    return -1

with open("rosalind_3sum.txt", 'r') as file1:
    firstline = file1.readline().split()
    line_num  = int(firstline[0])
    ele_num   = int(firstline[1])
    for i in range(line_num):
        line = file1.readline().split() 
        line = [int(i) for i in line]
        line_o = line[:]
        line.sort()
        result = indices_3sum(line,ele_num)    
        if result == -1:
            print -1,
        else:
            array = []
            for j in result:
                array.append(line_o.index(j)+1)
            array.sort()
            for z in  array:
                print z,
        print
