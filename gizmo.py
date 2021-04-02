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
    vector = list(range(1,13))
    table = numpy.outer(vector,vector)
    if zero_out_multiples != None:
        inds = table % zero_out_multiples == 0
        table[inds] = 0
    return table
        

