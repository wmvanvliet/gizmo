#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GIZMO Challenge

@author: jenni.saaristo@helsinki.fi
@version: 20210319
@notes: Funfunfun!
"""

import numpy as np
import pandas as pd


# -------------------- Exercise 1 --------------------

def hello(name, country='Finland'):
    print('Hello ' + name + ', how are things in ' + country + '?')

# -------------------- Exercise 2 --------------------

def spell(name):
    out = ''
    for i in range(len(name)):
        out = out + name[i] + '.'
    print(out[:-1])

# -------------------- Exercise 3 --------------------

def relative_path(ids):
    base = ['./subjects/mock_recording_','.rec']
    names = []
    
    if type(ids) == str:
        ids = [ids]
    for s in ids:
        names.append(base[0] + s + base[1])
    
    return names

# ------------------- Exercise 4–7 --------------------

class Gizmo:
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name)

# ------------------- Exercise 8-9 --------------------

def multiplication_table(zom=None):
    """Times table with optional dropping of multiples
    
    Returns the times table for integers up to 12, and optionally
    zeroes the multiples of the given int argument.
    
    Parameters
    ----------
    zom : int, optional
        The integer to drop the multiples of (zero_out_multiples)
    
    Returns
    -------
    tab : numpy array
        The times table as an array
        
    """

    v = np.arange(1,13)
    tab = np.outer(v,v)
    if type(zom) == int:
        tab[tab%zom == 0] = 0
    return tab

# ------------------- Exercise 11 --------------------

def generate_fibonacci_sequence(n):
    first=0
    yield first
    second=1
    yield second
    for i in range(n):
        this = first+second
        first = second
        second = this
        yield this

# ------------------- Exercise 12 --------------------

def get_fibonacci_sequence(n):
    fib = generate_fibonacci_sequence(n)
    arr = np.empty(0)
    for f in fib:
        arr = np.append(arr,f)
    return arr
        
# ------------------- Exercise 13 --------------------

def get_titanic():
    df = pd.read_csv('titanic.csv')
    return df

# ------------------- Exercise 14 --------------------

def get_titanic_children(age=12):
    df = get_titanic()
    return df.query('age <= @age')
