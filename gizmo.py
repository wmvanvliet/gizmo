
import glob
import os
import warnings
import numpy as np
import pandas as pd

def hello(name=None,country='Finland'):
    if name is not None:
        out_text = 'Hello {name}, how are things in {country}?'\
            .format(name=name,country=country)
        print(out_text)
    else:
        print('you need to enter a valid name')
        
def spell(string=''):
    output = ''
    for char in string:
        output=output + '.'+ char
    output = output[1:]
    print(output)

def relative_path(identifier_list):
    output = []
    if isinstance(identifier_list, str) or \
    isinstance(identifier_list, int) or \
    isinstance(identifier_list, float):
        return('./subjects/mock_recording_{subject_identifier}.rec')\
                        .format(subject_identifier = str(identifier_list))
    
    if hasattr(identifier_list,'__iter__'):
        if len(identifier_list) != 0:
            for file in identifier_list:
                if isinstance(file,str):
                    output.append('./subjects/mock_recording_{subject_identifier}.rec'\
                        .format(subject_identifier = str(file)))
                else:
                    print('object in the list is not a string!')
                    
        else:
            warnings.warn('The supplied itterator is empty')
            
    else:
        warnings.warn('Supplied object is not an itterator')
    return(output)

class Gizmo:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(self.name)
    
def multiplication_table(zero_out_multiples: int =0, table_size: int=12) -> np.ndarray:
    """Returns the multiplitation table of a number
    
    This function returns the multiplitation table of a number
    with ommited values for specific integer that values in table 
    are its multiplier.
    
    Parameters
    ----------
        zero_out_multiples: int (optional)
            This vale replaces its mulipliers with 0.
            if multiplier is not specified, nothing will change.
            multiplier with value of zero is discarded.
            
        table_size: int 
            maximum size of the table.
            
    Returns
    -------
        np.ndarray
            multiplication table with removed values of 
            `zero_out_multiples` if specified
    """
    number = table_size
    array_ = np.array([list(range(number))])+1
    if zero_out_multiples != 0:
        array_ = np.where(array_%zero_out_multiples == 0, 0, array_) 
    array_T = array_.T
    output = np.matmul(array_T,array_)
    return(output)

    
def generate_fibonacci_sequence(n=5):
    fib_list = []
    for i in range(n):
        if i<=1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[-1]+fib_list[-2])
    return(fib_list)

def get_titanic():
    return(pd.read_csv('titanic.csv'))


def get_titanic_children():
    df = pd.read_csv('titanic.csv')
    df = df[df['age']<= 12]
    return(df)
    

