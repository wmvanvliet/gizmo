import numpy as np
import pandas as pd

def hello(name, country='Finland'):
    # These are two examples of how it can be done
    # print("Hello {}, how are things in {}?".format(name, country))
    print("Hello %s, how are things in %s?" % (name, country))


def spell(word):
    result = ''
    for i, char in enumerate(word):
        if(i == len(word)-1):
            result = result + char
        else:
            result = result + char + '.'
    print(result)


def relative_path(identifiers):
    for i, item in enumerate(identifiers):
        identifiers[i] = './subjects/mock_recording_{}.rec'.format(item)

    return identifiers


class Gizmo(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

# Algorithms made with lists
def multiplication_table_1():
    ref = 1
    table = [] 
    while ref <= 12:
        sub_table = []
        sub_arr  = np.array([])

        for n in range(1,13):
            sub_table.append(n*ref)
            
        table.append(sub_table)
        ref += 1

    print(table)
    return table


# done without using outer product
def multiplication_table_2():
    table = np.zeros(12*12).reshape(12,12)
    row_count = 0
    for row in table:
        row_count += 1
        for i,n in enumerate(row):
            row[i] = (i+1) * row_count
    
    return table

# done using numpi outer product
def multiplication_table_3():
    n_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    table = np.outer(n_list,n_list, out=None)
    return table

def multiplication_table(zero_out_multiples=None):
    """Creates a multiplication table from 1 to 12, 
    It also turns into zeros the multiples of the passed number.
    multiplcation_table(5) turns into zero all multiples of 5 int he table.

    Parameters
    ----------
    zero_out_multiples : int, optional
        number that we want to use to turn multiples into zero
   
    Returns
    ----------
    table : numpy.array
        array([ [  1,   2,   3,   4,   0,   6,   7,   8,   9,   0,  11,  12],
                [  2,   4,   6,   8,   0,  12,  14,  16,  18,   0,  22,  24],
                [  3,   6,   9,  12,   0,  18,  21,  24,  27,   0,  33,  36],
                [  4,   8,  12,  16,   0,  24,  28,  32,  36,   0,  44,  48],
                .....

    """
    array = np.arange(1,13)

    # Compute the outer product of two vectors.
    table = np.outer(array,array, out=None)
    
    if zero_out_multiples:
        # numpy does dynamic indexing iterating on each element of the table
        # and finds out those items which modulo is 0 and replace the values with 0
        table[table % zero_out_multiples == 0] = 0
    
    return table


def generate_fibonacci_sequence(n):  
    if n > 0:
        number = 1 
        prev_number = 0 
        for i in range(n):
            if i < 1: 
                yield prev_number
            else:
                yield number
                number = number + prev_number
                prev_number = number - prev_number 

def get_fibonacci_sequence(n):
    array = np.arange(n)
    for i, el in enumerate(generate_fibonacci_sequence(n)):
        array[i] = el
        
    return array

def get_titanic():
    return pd.read_csv('titanic.csv')
    

def get_titanic_children():
    titanic = get_titanic()
    # Create a list of boolean values based on the condition <= 12
    is_child = titanic['age'] <= 12    
    # filter rows for children using the boolean variables
    return titanic[is_child]         
