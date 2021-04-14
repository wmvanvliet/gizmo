#!/usr/bin/python3
import numpy as np
import pandas as pd

def hello(name, country='Finland'):
    
    print('Hello {}, how are things in {}?'.format(name,country))
    
    return


def spell(str_in):
    
    str_out = str_in[0]
    for el in str_in[1:]:
        str_out += '.' + el
    print(str_out)
    
    return


def relative_path(subject_identifiers):
    
    rel_path = './subjects/mock_recording_'
    ext = '.rec'
    
    file_list = [rel_path + elem + ext for elem in subject_identifiers]
    
    return file_list


class Gizmo(object):
  
    def __init__(self, name):
      
        self.name = name
      
        return
    
    def speak(self):
        
        print(self.name)
        
        return


def multiplication_table(zero_out_multiples=None):
      """Multiplication table from 1 to 12
      
      This function returns a dim(2) matrix contasining the multiplication
      table from 1 to 12. If parameter zero_out_multiples is set to an
      integer value all matrix elements multiple of this value are set
      to zero.
      
      Parameters
      ----------
      zero_out_multiples : int, optional
          If default (None) returns 2x2 matrix as is, 
          if integer sets to 0 the multiples of zero_out_multiples
      
      Returns
      -------
      mat : numpy.ndarray
          Matrix with dimension 2 containing multiplication table
          up to 12 with values set to zero according to zero_out_multiples
      """
      mat = np.outer(np.arange(1,13,1),np.arange(1,13,1))
      
      if zero_out_multiples is None:
          return mat
      else:
          mat[mat % zero_out_multiples == 0] = 0
          return mat
      
      
def generate_fibonacci_sequence(n):
    n1 = 0
    n2 = 1
    
    it = 1
    
    while it <= n:
        yield n1
        it += 1
        n1, n2 = n2, n1 + n2

def get_fibonacci_sequence(n):
    
    lst_fib = []
    fib = generate_fibonacci_sequence(n)
    for ii in range(0, n):
        lst_fib.append(next(fib))
    res = np.array(lst_fib)
    
    return res
      
    
def get_titanic():
    
    titanic = pd.read_csv('titanic.csv')
    
    return titanic
    
    
 def get_titanic_children():
    
    titanic_df = get_titanic()
    ages_le12 = titanic[titanic["Age"] >= 12]
    
    return age_le12
