#!/usr/bin/python



def fibonacci(x):
    if x==0:
        return 0
    if x==1:
        return 1
    value = fibonacci(x-1)+fibonacci(x-2)
    return value

def fibonacci2(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        fib_list = [0,1]
        for i in range(2,x+1):
            fib_list.append(fib_list[i-1]+fib_list[i-2])
        return fib_list[x]
        

def fibonacci3(x):
    a,b=0,1
    for i in xrange(0,n):
        a,b = b,a+b
    return a



print fibonacci2(20)
