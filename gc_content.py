#!/usr/bin/python
import re
f1 = open ('rosalind_gc.txt','r')

def countGC(dna):
    count = 0.0
    ##can use dna.count('C') to get the number of 'C'
    for letter in dna:
        if (letter == 'C' or letter == 'G'):
            count += 1
    total = len(dna)
    value = 100.0 *(count/total)
    return value

content = f1.readlines()
string = ''
gc_dict = {}
key_old =  ""
control = 0
for line in content:
    matchobj = re.match(r'>(\w+)',line)
    if control ==0:
        key_old  = matchobj.group(1)
        gc_dict[key_old] = 0
        control =1       
        continue
    if matchobj:
        print "key:",key_old, "string:",string
        gc_dict[key_old]=countGC(string)
        string = ''
        key_old = matchobj.group(1)
        
        gc_dict[key_old] = 0

    else:
        string = string + line.rstrip('\n')
gc_dict[key_old]=countGC(string)

print gc_dict
f1.close()
get_keys = gc_dict.keys()
max_key = ''
max_value = 0
for key in get_keys:
    if gc_dict[key] > max_value:
        max_value = gc_dict[key]
        max_key = key
    
print max_key,max_value


