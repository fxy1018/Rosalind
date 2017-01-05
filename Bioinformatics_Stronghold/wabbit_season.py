#!/usr/bin/perl

f1 = open ('rosalind_fibd.txt','r')
(n,m) = f1.read().split()
n= int(n)
m= int(m)

def calculate_rabbits(t):
    total = sum(num for num in t)
    return total 

def make_list(m):
    t_new = []
    for i in range(m):
        t_new.append(0)
    return t_new

def mortal_fibonacci(n,m):
    if n==1:
        t=[1]
        for i in range(1,m):
            t.append(int(0))
        return t
    else:
        t = mortal_fibonacci((n-1),m)
        t_new = make_list(m)
        total = sum(num for num in t)
        t_new[0]=total - t[0]
        for i in range(0,m-1):
            t_new[i+1] = t[i]
        return t_new


print calculate_rabbits(mortal_fibonacci(n,m))
