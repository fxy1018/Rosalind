#!/usr/bin/env python3
from __future__ import division

file = "test.txt"
data = open(file).read().rstrip("\n")
mono_table = {"A":71.03711,  "C":103.00919, "D":115.02694,
              "E":129.04259, "F":147.06841, "G":57.02146,
              "H":137.05891, "I":113.08406, "K":128.09496,
              "L":113.08406, "M":131.04049, "N":114.04293,
              "P":97.05276,  "Q":128.05858, "R":156.10111,
              "S":87.03203,  "T":101.04768, "V":99.06841,
              "W":186.07931, "Y":163.06333}
total = 0

for i in data:
    if mono_table.get(i):
        total = total + mono_table.get(i)

print(total)
    
##modified: create a dictionary
#read in mass table to string
f = open('/Users/almartin/Documents/workspace/rosalind/mass_table.txt', 'r')
mass = f.read()

#mass string to list
mass = mass.split()

#mass string to dict
mass = dict(zip(mass[0::2],mass[1::2]))


#modified print which add the mass of water H2O 
print("%.2f"%(sum(map(lambda x:mass[x],data))+18.01528))
