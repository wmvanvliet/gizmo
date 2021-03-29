# First draft for gizmo.py
import numpy as np
import pandas as pd

def hello(name, country='Finland'):
    print('Hello ' + name + ', how are things in ' + country + '?')

def spell(word):

    output = ""
    for i,l in enumerate(word):
        if i == len(word)-1:
            output = output + l
        else:
            output = output + l + "."

    print(output)

def relative_path(ids):

    list = []
    path_base = './subjects/mock_recording_'
    suffix = '.rec'
    for id in ids:
        list.append(path_base + id + suffix)
        #print(path_base + id + suffix)

    return list

def multiplication_table(zero_out_multiples: int = None):
    """Multiplication table for integers from 1 to 12.

    This function returns the multiplication table from integers from 1 to 12 so that
    a table element on row i and in column j corresponds to i*j.

    Parameters
    ----------
    zero_out_multiples : int
        Sets all numbers that are multipliers of this parameter to 0.

    Returns
    -------
    m_table : numpy array
        A numpy array with the multiplication values i*j.
    """
    nums = np.array(range(1,13))
    if zero_out_multiples is None:
        return np.outer(nums, nums)
    else:
        print("tetst: ", zero_out_multiples, '-->', [nums % zero_out_multiples == 0])

        print("nums: ", nums)
        m_table = np.outer(nums, nums)
        m_table[m_table % zero_out_multiples == 0] = 0
        return m_table

def generate_fibonacci_sequence(n):


    if n == 1:
        seq = [0]
        yield seq[-1]

    if n == 2:
        yield 0
        yield 1

    if n > 2:
        seq = [0, 1]
        yield 0
        yield 1
        for i in range(1, n-1):
            seq.append(seq[i-1] + seq[i])
            yield seq[-1]

def get_fibonacci_sequence(n):
    res_array = np.empty(n)
    for i, el in enumerate(generate_fibonacci_sequence(n)): res_array[i] = int(el)

    return res_array

def get_titanic():
    df = pd.read_csv('titanic.csv')
    return df

def get_titanic_children():
    df = get_titanic()
    children = df[df.age <= 12]
    return children


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)
