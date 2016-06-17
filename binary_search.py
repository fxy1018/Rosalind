#!/usr/bin/python

file1 = open ("rosalind_bins.txt","r")
n = file1.readline()
m = file1.readline()
listA = file1.readline().split()
listB = file1.readline().split()
#print n,m,"this is lista \n",listA,"\n this is listb \n",listB

def binary_search(listA,number,n):
    new_list = listA
    while (len(new_list) > 0):
        n =len(new_list)/2
        median = int(new_list[n])
       # print "the median,", median
        if number == median:
       #     print listA.index(str(number))
            return listA.index(str(number))+1
        elif number > median:
            new_list = new_list[n+1:]
        #    print "large situation: ",new_list 
        elif number < median:
            new_list = new_list[0:n]
         #   print "small situation: ", new_list
    return -1

def binary_search2(searchArray, item, n):
    low = 0
    high = int(n)-1
    
    while low<=high:
        index = (low+high)/2
        if item == searchArray[index]:
            return index
        elif item <searchArray[index]:
            high = index - 1
        else:
            high = index + 1

    return -1





result_list = []
for i in range(int(m)):
    number = int(listB[i])
    result_list.append(str(binary_search(listA, number, int(n))))
    #print "update result list is: ", result_list

print " ".join(result_list)




file1.close
