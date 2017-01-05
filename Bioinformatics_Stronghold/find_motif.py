#!/usr/bin/python

f1 = open ('rosalind_subs.txt','r')
string = f1.read()
(s,t) = string.split()
f1.close()
s='GATATATGCATATACTT'
#t='ATAT'
l=len(t)
print l
location = []
for i in range(len(s)-l):
    if s[i:(i+l)]==t:
        print s[i:(i+l)]
        location.append(i+1)
    else:
        continue

print ' '.join(str(n) for n in location)

