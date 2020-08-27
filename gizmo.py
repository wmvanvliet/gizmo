import numpy as np
import pandas as pd

# exercise 2
def hello(name, country="Finland"):
    print(f"Hello {name}, how are things in {country}?")

# exercise 3
def spell(word):
    spelled = ""
    for i in word:
        spelled += i + "."
    print(spelled[:-1])

# exercise 4
def relative_path(subject_identifiers):
    files = []
    for subject_identifier in subject_identifiers:
        files.append(f'./subjects/mock_recording_{subject_identifier}.rec')
    return files

# exercise 5,6,7
class Gizmo():
    def __init__(self,name):
        self.name = name
    def speak(self): 
            print(self.name)

# exercise 8,9,10
def multiplication_table(zero_out_multiples=None):
    """ A function returning a multiplication table for 1-12.

    This function returns a multiplication table for 1-12. 
    Multiples of the specified value will be replaced with zeros.

    Parameters
    ----------
    zero_out_multiples : int
        Multiples of which to replace with zeros. Defaults to None.

    Returns
    -------
    
    table : ndarray 
        Multiplication table with multiples set to zero if specified.

    """
    table = np.outer(np.array(range(1,13)),np.array(range(1,13)))
    if zero_out_multiples != None:
        table[table % zero_out_multiples == 0] = 0
    return table

# exercise 11
def generate_fibonacci_sequence(n):
    prev_num = 0
    next_num = 1
    for i in range(n):
        yield prev_num
        prev_num, next_num = next_num, prev_num + next_num
        

# exercise 12
def get_fibonacci_sequence(n):
    return np.array(list(generate_fibonacci_sequence(n)))

# exercise 13
def get_titanic():
    return pd.read_csv("titanic.csv")

# exercise 14
def get_titanic_children():
    df = get_titanic()
    return df[df.age <= 12]

        
    
    
        
        
