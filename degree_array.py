#!/usr/bin/python

f1 = open('rosalind_deg.txt','r')
array = f1.readlines()
initial = 0
for i in array:
    i.strip()
    line_list = i.split(' ')
    if initial == 0:
        degree = [0]* (int(line_list[0])+1)
        initial = 1
        continue
    degree[int(line_list[0])]+=1
    degree[int(line_list[1])]+=1

degree = degree[1:]
print str(degree).replace(',','').replace('[','').replace(']','')


#array2 = []
#for j in degree:
#    array2.append(str(j))

#print " ".join(array2)









