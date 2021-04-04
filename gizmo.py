#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 16:17:18 2021

@author: tavastm1
"""

import numpy as np
import pandas as pd

def hello(name, country='Finland'):
    """ - """
    return print(f'Hello {name}, how are things in {country}?')

def spell(word):
    dots = ''
    for i in range(len(word)):
        if i == len(word) -1:
            dots += (word[i])
        else:
           dots += word[i]
           dots += '.'
    return print(dots)
    
def relative_path(subject_identifier):
    names = []
    for i in range(len(subject_identifier)):
        temp = subject_identifier[i]
        names.append(f'./subjects/mock_recording_{temp}.rec')
    return names


class Gizmo:
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return print(self.name)
    
def multiplication_table(a=1,b=12, zero_out_multiplies=None):
    """
    Creates a multiplication table from a to b. 
    
    Parameters: 
        a : int
            Default 1.
        b : int
            Default 12,
        Zero_out_multiplies : int
            All the multiplies of the int will be set to 0. Defaults None.
    
    Returns:
        A multiplication table from a to b. 
    """ 
    temp = np.outer(list(range(a,b+1)),list(range(a,b+1)))
    if zero_out_multiplies is not None:
        temp[temp % zero_out_multiplies == 0] = 0   
        
    return temp

def get_titanic():
    titanic = pd.read_csv('titanic.csv')
    return titanic

def get_titanic_children():
    titanic_c = pd.read_csv('titanic.csv')
    titanic_index = titanic_c["age"] <= 12
    titanic_c = titanic_c.loc[titanic_index, :]
    return titanic_c