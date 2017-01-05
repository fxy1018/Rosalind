#!/usr/bin/python

f1 = open("rosalind_iev.txt","r")
num_list = f1.read().split()
#num_list = [1,0,0,1,0,1]
f1.close

prob = [1,1,1,0.75,0.5,0]
count = 0
for i in range(6):
    count = count+(2 * int( num_list[i] )* prob[i])


print count
