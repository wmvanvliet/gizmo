import numpy as np
import numpydoc
import pandas as pd

def hello(name, country = 'Finland'):
    print('Hello ', name, ', how are things in ', country, '?', sep = '')
    
def spell(word):
    for letter in list(word)[:-1]:
        print(letter, ".", sep="", end="")
    print(list(word)[-1])
    
def relative_path(subject_identifier):
    l = []
    for i in range(len(subject_identifier)):
        l += ['./subjects/mock_recording_' + subject_identifier[i] + '.rec']
    return(l)

class Gizmo:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(self.name)

def multiplication_table(zero_out_multiples=None):
    """Replace all multiplies of given value with 0.
    
    Extended summary
    ----------------
    This function replaces in the multiplication table all multiplies 
    of the given numer `zero_out_multiples` with 0.
    
    Parameters
    ----------
    zero_out_multiples : int
                         Value and its multiplies to be zeroed out.
    
    Returns
    -------
    mt : array
         Array of multiplication table.
    """
    n = 12
    mt = np.outer(np.linspace(1,n,n), np.linspace(1,n,n))
    if zero_out_multiples != None:
        mt[(mt % zero_out_multiples) == 0] = 0
    return(mt)
    
def generate_fibonacci_sequence(n):
    n1 = 0
    n2 = 1
    count = 0
    while count < n:
        yield n1
        nn = n1 + n2
        n1 = n2
        n2 = nn
        count += 1

def get_fibonacci_sequence(n):
    n1 = 0
    n2 = 1
    fib_array = np.empty(n)
    for i in range(n):
        fib_array[i] = n1
        nn = n1 + n2
        n1 = n2
        n2 = nn
    return(fib_array)

def get_titanic():
    return pd.read_csv("titanic.csv")

def get_titanic_children():
    df = pd.read_csv("titanic.csv")
    return df[(df["who"] == "child") & (df["age"] <= 12)] 
