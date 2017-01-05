#!/usr/bin/perl

def fibonacci(n,k):
    if (n==1 or n==2):
        return 1;
    if (n==2):
        return 1;
    
    
    return fibonacci(n-1,k)+3*fibonacci(n-2,k)

print fibonacci(28,3)

        
