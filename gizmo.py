## open python in terminal, import gizmo, call function
## https://github.com/MertenNefs/gizmo/tree/testbranch

## exercise 1
import gizmo

## exercise 2
def hello(name,country='Finland'): 
    print('Hello '+ name + ', how are things in ' + country + '?')
    
## exercise 3
def spell(name):
    spelled = ''
    for l in name:
        spelled += l + '.' # spelled + l + '.'
    print(spelled[:-1])
    
## exercise 4 
### https://realpython.com/python-f-strings/
def relative_path(subject_identifiers):
    paths = []
    for i in subject_identifiers:
        paths.append(f"./subjects/mock_recording_{i}.rec")
    return paths

## exercise 5/6/7 add attribute and method to class
class Gizmo:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name)
        
## exercise 8/9/10 numpy
import numpy as np
def multiplication_table(zero_out_multiples = None):
    """
    Summary: Generates a table of multiples

    Extended Summary: As an outer product of the array x,
    eliminating multiples of the argument.
    
    Parameters
    ----------
    zero_out_multiples : int
        argument of integer value to zero out.
   
    Returns
    -------
    y : array
        outer product array of integers resulting from (x,x).
 
    """
    x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    y = np.outer(x,x)
    if zero_out_multiples != None:
        y[y % zero_out_multiples == 0] = 0 ## modulo operator yields remainder of division
    return y

## https://numpy.org/doc/stable/user/quickstart.html#the-basics
## https://numpy.org/doc/stable/reference/generated/numpy.outer.html
## https://docs.python.org/3.6/reference/expressions.html#binary-arithmetic-operations
## https://numpy.org/doc/stable/reference/arrays.indexing.html#boolean-array-indexing
## documentation printable through: print(multiplication_table.__doc__)

## exercise 11
def generate_fibonacci_sequence(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x+y
      
        
        

## exercise 12
def get_fibonacci_sequence(n):
    y = generate_fibonacci_sequence(n)
    return np.array(list(y))

#13 exercise 13
import pandas as pd
def get_titanic():
    titanicdata = pd.read_csv('titanic.csv')
    return(titanicdata)
    
#14 exercise 14
def get_titanic_children():
    total = get_titanic()
    children = total[total['age'] <= 12]
    return(children)