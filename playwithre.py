#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:27:35 2020

@author: aminghazanfari
"""
import re

def filter_string(string):
    #this function  return a number from a string.
    return int(re.sub('[^0-9]','',string)) 

print(filter_string('aafdfdg3ffh5hj6k6'))