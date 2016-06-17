#!/usr/bin/env python

####################
#to use breadth-first search to compute single-source shortest distances in
# an unweighted directed graph
####################
#sample dataset
#6 6
#4 6
#6 5
#4 3
#3 5
#2 1
#1 4
#####################
#sample output
#0 -1 2 1 3 2
####################

with open("test.txt",'r') as file1:
    #read the first line:
    #the first line gives the information of the graph
    #the first number is number of vertices
    #the second number is number of edges
    first_line = file1.readline().split()
    vertices = int(first_line[1])
    edges = int(first_line[2])
    

