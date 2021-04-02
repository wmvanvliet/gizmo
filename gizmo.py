import numpy

def hello(name, country = "Finland"):
    print("Hello %s, how are things in %s?" % (name, country))
    
def spell(word):
    for i in range(len(word)):
        print(word[i],end='')
        if i != len(word)-1:
            print(".",end='')

def relative_path(identifiers):
    path_list = []
    
    for i in identifiers:
        path_list.append('./subjects/mock_recording_{}.rec'.format(i))
    
    return path_list

def multiplication_table(zero_out_multiples = None):
    
    """Multiplication table from 1 to 12.
    
    If input is an integer, the multiples of that integer are
    zero in the returned multiplication table.
    
    Parameters
    ----------
    zero_out_multiples : int
        Sets multiples of this value to zero in the 
        returned array.
    
    Returns
    -------
    table : array
        Multiplication table from 1 to 12.
    """
    
    
    v = list(range(1,13))
    
    table = numpy.outer(v,v)
    
    table[table % zero_out_multiples == 0] = 0
    
    return table


def generate_fibonacci_sequence(n):   
    x = 0
    y = 1
    for i in range(n):
        if i == 0:
            yield x
        else:
            x, y = y, x+y
            yield x


class Gizmo:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(self.name)
             