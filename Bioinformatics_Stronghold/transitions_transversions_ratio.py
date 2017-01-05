#!/usr/bin/env python3
from __future__ import division


'''
Created on Jun 21, 2016

@author: fanxueyi
'''


file = "test.txt"
data= open(file).read()
data_list = data.split('>')

s1 = data_list[1].rstrip("\n").split('\n')
s1 = s1[1:]
s1 = "".join(s1)
print(s1)

s2 = data_list[2].rstrip("\n").split('\n')
s2 = s2[1:]
s2 = "".join(s2)

#data = open(file).readlines()
#s1 = data[1].rstrip("\n")
#s2 = data[3].rstrip("\n")


transition_dict = {"A":"G", "T":"C","C":"T", "G":"A"}
#transversion_dict = {"A":"C", "C":"A", "G":"C", "C":"G","G":"T", "T":"G", "A":"T","T":"A"}
count_transition = 0
count_transversion = 0
#count = 0

for i in range(len(s1)):
    if (s1[i] != s2[i]):
 #       count = count+1
  #      print(s1[i],s2[i])
        if (transition_dict.get(s1[i]) == s2[i]):
            count_transition = count_transition + 1
        else:
            count_transversion = count_transversion + 1
        
#print(count)
#print(count_transition)
#print(count_transversion)
ratio = count_transition/count_transversion
print (ratio)


#modified:
def transitionTransversionRation(s1,s2):
    trans = {"A":"G", "T":"C","C":"T", "G":"A"}
    mut = [0 if trans[b1]==b2 else 1 for b1, b2 in zip(s1,s2) if b1 is not b2]
    return mut.count(0)/float(mut.count(1))

