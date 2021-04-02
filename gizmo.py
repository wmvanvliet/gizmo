import numpy

def hello(name, country="Finland"):
    
    print("Hello %s, how are things in %s?" % (name, country))
    
def spell(word):
    
    for i in range(0, len(word)):
        print(word[i], end = '')
        if i != len(word)-1:
            print(".", end = '')

def relative_path(subject_identifier):
    names = []
    for i in subject_identifier:
        path= './subjects/mock_recording_%s.rec' % (i)
        names.append(path)
    return names

class Gizmo:
    def __init__(self, name):
         self.name = name
         
    def speak(self):
        print(self.name)
        
def multiplication_table(zero_out_multiples = None):
    """ Creates multiplication table from 1 to 12.
    Creates multiplication table from 1 to 12. Optional input parameters zeros elements of the table,
    which are integer multiples of given input integer.
    
    Parameters
    ----------
    zero_out_multiples : int, optional (default is None)
    This integer parameter zeros all elements of the multiplication table which are exact multiples of it.
    
    Returns
    ----------
    table: array
    Table is the resultant multiplication table, modified based on the input parameter zero_out_multiples
    


    """
    vector = list(range(1,13))
    table = numpy.outer(vector,vector)
    if zero_out_multiples != None:
        inds = table % zero_out_multiples == 0
        table[inds] = 0
    return table

def generate_fibonacci_sequence(n):
    sequence = [0,1]
    counter = 2
    if n == 1:
        return 0 
    elif n == 2:
        return sequence
    else:
        while len(sequence) < n:
            sequence.append((sequence[counter-2]+sequence[counter-1]))
            counter = counter + 1
        return sequence
    
        

