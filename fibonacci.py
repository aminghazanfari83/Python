#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:18:58 2020

@author: aminghazanfari
This file consist of fucntions and implementaions related to fibonacci number 
"""
def fibo_rec(n):
    #This function provides n's fibonacci number  
    #recursive approach for implementation of fibonacci
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo_rec(n-1)+fibo_rec(n-2)


def fibo_iter(n):
    #This function provides n's fibonacci number 
    #iterative approach for implementaion of fibonacci 
    f0, f1 = 0, 1
    for i in range(0, n):
        f0,f1 = f1, f0 + f1
    return f0


#Provide list of n fibonacci numbers 
def fibo_list(n):
   return [fibo_iter(i) for i in range(n+1)]

#print list of first 10 fibonacci numbers
#print(fibo_list(10))


def fibo_last_digit(n):
    #This function returns the last digit of n's fibonacci number
    return int('{}'.format(fibo_iter(n))[-1])


#Product of consecutive Fib numbers
def productFib(prod):
    # ythis function checks if a given number can be written as a product of
    #two consequitive Fibonacci numbers if possible
    f0,f1 = 0,1
    while f0*f1 <prod:    
        f0,f1 = f1,f0+f1
        
        
    return [f0,f1, prod==f0*f1] 

fibo_cache = {}

#fibonacci implementation with memory
def fibo_rec_memo(n):
    if n in fibo_cache:
        return fibo_cache[n]
    if n ==1:  
        return 1
    elif n==2:
        return 1
    elif n > 2:
        res = fibo_rec_memo(n-1)+fibo_rec_memo(n-2)
        
    #cache the value first and then return it
    fibo_cache[n] = res
    return res

#test run
#for n in range(1,10):
#    print(n,';',fibo_rec_memo(n))
    
    
#fibonacci implementation with memory by 
#using the bulit-in function lru_cache
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibo_rec_memo_lr(n):
    #This function provides n's fibonacci number  
    #recursive approach for implementation of fibonacci
    #check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n<1:
        raise ValueError("n must be a positive int")
    
    #compute the Nth term
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo_rec_memo_lr(n-1)+fibo_rec_memo_lr(n-2)
    
    #test run
for n in range(1,10):
    print(n,';',fibo_rec_memo_lr(n))