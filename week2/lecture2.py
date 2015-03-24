# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 20:11:42 2014

@author: jonatan
"""

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    
    import random
    # Your code here
    x = random.randint(0,99)
    if x%2 == 0:
        return x
    else:
        return x+1



def stochasticNumber():
    import random
    
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    x = random.choice([10,12,14,16,18,20])
    return x