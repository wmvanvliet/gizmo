def hello(name, country='Finland'):
    print("Hello {name}, how are things in {country}?".format(name=name, country=country))

def spell(word):
    
    for i in range(len(word)):
        if(i!=len(word)-1):
            print(word[i], end=".") #JASSOO
        else:
            print(word[i], end="")

def relative_path(subject_ids):
    
    for s in range(len(subject_ids)):
        path = './subjects/mock_recording_{subject_identifier}.rec'.format(subject_identifier=subject_ids[s])
        subject_ids[s] = path
        
    return subject_ids

class Gizmo:
    """Gizmo class"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name)

def generate_fibonacci_sequence(n):
    """ Generates first n numbers of the fibonacci sequence.
    
    Initialized with integer values a=0 and b=1, this function increments
    the sequence by the sum of two its previous values.
    
    Parameters
    ---------- 
    n : int
        The length of the generated sequence
        
    
    Yields
    ------
    fib : generator
         Generator that contains the first n fibonacci numbers
        """
    
    a=0 
    b=1
    for i in range(n):
        yield a
        a,b = b, a+b
