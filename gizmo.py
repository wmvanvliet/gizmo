'''
Created on Mar 31, 2022
Gizmo Challenge File

@author: thomas
'''

def hello(name,country='Finland'):
    print("Hello {name}, how are things in {country}?".format(name=name,country=country))
    

def spell(word):
    spelled = ''
    for letter in word[:-1]:
        spelled += letter+'.'
    print(spelled + word[-1])

def relative_path(subjects, basename='./subjects/mock_recording_', extension='.rec' ):
    return [(basename + '{subj}' + extension).format(subj=subj) for subj in subjects]


def generate_fibonacci_sequence(maxcount):
    """ This function returns a fibonacci number generator.
    
    generate_fibonacci_sequence(maxcount)
        
    The returned generator yields fibonacci numbers up to the maximum number indicated.    
        
    Parameters
    ----------
    maxcount: int
        The number of fibonacci numbers to be yielded by the generator.
        
    Yields
    -------        
    fibonacci: int
        The n-th number yielded is the n-th fibonacci number  
     
    """
    start = (0,1)    
    for i in range(maxcount):
        current = start[0]
        start = (start[0]+start[1],current)        
        yield current


class Gizmo:
    
    def __init__(self, name):
        self.name = name        
    
    def speak(self):
        print(self.name)
    
    
