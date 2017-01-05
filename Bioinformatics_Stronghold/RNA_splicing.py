#!/usr/bin/env python3
from __future__ import division
import re



'''
Created on Jun 17, 2016

@author: fanxueyi
'''
#open the file 
file = 'test.txt'
data_file = open(file)

#to check whether it is the headline
def is_headline(line):
    if (re.search(r">", line )):
        return False
    else:
        return True
        
data_lines = data_file.readlines()
dna_seqs = filter(is_headline, data_lines)

def strip_newline(line):
    line = line.rstrip('\n')
    return line

dna_seqs = map(strip_newline, dna_seqs)
dna_seqs = list(dna_seqs)
dna = dna_seqs[0]
for i in range(1,len(dna_seqs)):
    dna = dna.replace(dna_seqs[i],'')
   

dna = dna.replace('T', 'U')
print(dna)
    


#print ([dna for dna in dna_seqs])
