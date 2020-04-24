#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:18:58 2020

@author: aminghazanfari
This file consist of fucntions and implementaions related to fibonacci number 
"""

def fibo(n):
    #This function provides n's fibonacci number 
    if n==0:
        return 1
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)