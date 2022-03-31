'''
Created on Mar 31, 2022
Gizmo Challenge File

@author: thomas
'''

def hello(name,country='Finland'):
    print("Hello {name}, how are things in {country}".format(name=name,country=country))
    

def spell(word):
    spelled = ''
    for i in range(len(word)-1):
        spelled += word[i]+'.'
    print(spelled + word[-1])

def relative_path(subjects, basepath='./subjects/mock_recording_', extension='.rec' ):
    return [basepath + subj + extension for subj in subjects]

class Gizmo:
    
    def __init__(self, name):
        self.name = name        
    
    def speak(self):
        print(self.name)
    
    def generate_fibonacci_sequence(self,maxcount):
        """ This function returns a fibonacci number generator.
        
        generate_fibonacci_sequence(maxcount)
        
        The returned generator yields fibonacci numbers up to the maximum number indicated.
        Note, that at least 2 numbers are always yielded!
        
        Parameters
        ----------
        maxcount: int
                  The number of fibonacci numbers to be yielded by the generator.
        
        Yields
        -------        
        fibonacci: int
                   The n-th number yielded is the n-th fibonacci number  
         
        """
        last = 0
        yield last
        start = 1
        yield start
        for i in range(maxcount-2):
            current = start+last
            last = start
            start = current
            yield current    
    