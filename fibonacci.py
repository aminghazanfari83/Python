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
print(fibo_list(10))


def fibo_last_digit(n):
    #This function returns the last digit of n's fibonacci number
    return int('{}'.format(fibo_iter(n))[-1])