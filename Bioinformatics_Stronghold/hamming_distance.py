#!/usr/bin/perl


file1 = 'rosalind_hamm.txt'
f1 = open (file1,'r')
content = f1.read()
str_arr = content.split('\n')
print str_arr
str1 = str_arr[0]
str2 = str_arr[1]
count = 0;
for i in range(len(str1)):
    if (str1[i]!= str2[i]):
        count +=1

print count
