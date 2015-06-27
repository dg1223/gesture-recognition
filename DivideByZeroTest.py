# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:15:29 2015

@author: Shamir
"""

def divide(a,b):
    try:
        result = a/float(b)
        return result
    except ZeroDivisionError as detail:
        print 'Handling run-time error:', detail
        pass