# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:20:00 2021

@author: arsii
"""
import numpy as np
import pandas as pd

#%% EX 2 

def hello(name, country='Finland'):
	print(f'Hello {name}, how are things in {country}?')

#%% EX 3
    
def spell(word):
    for i in range(len(word)):
        if i < len(word) - 1:
            print(word[i], end='.')
        else:
            print(word[i])
        
#%% EX 4
    
def relative_path(subjects):
    return [f'./subjects/mock_recording_{i}.rec' for i in subjects]   

#%% EX 5 - 7

class Gizmo:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        print(f'{self.name}')
        
#%% EX 8 - 10

def multiplication_table(zero_out_multiples = None):
    """Return a 12 x 12 multiplication table.
    Function returns a multiplication table in numpy format.
    Numbers from 1 to 12 are multiplied in the table.
    Selected multiples on numbers are converted to zero.
    
    Parameters
    ----------
    zero_out_multiples : int, optional
        Multiples to zero out. The default is None.

    Returns
    -------
    mm : numpy.ndarray
        12 x 12 multiplication table.

    """
    a = np.arange(1,13)
    mm = np.outer(a,a)
    if isinstance(zero_out_multiples, int):
        bool_filt = mm % zero_out_multiples == 0
        mm[bool_filt] = 0
    return mm
#%% EX 11
def generate_fibonacci_sequence(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x + y
        
        
#%% EX 12
def get_fibonacci_sequence(n):
    ret = []
    f = generate_fibonacci_sequence(n)
    for i in range(n):    
        ret.append(next(f))
    return np.array(ret)


#%% EX 13
def get_titanic():
    return pd.read_csv('titanic.csv')

df = get_titanic()

#%% EX 14
def get_titanic_children():
    df = get_titanic()
    children = df[df.age <= 12]
    return children