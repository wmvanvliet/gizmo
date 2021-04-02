import numpy

def hello(name, country):
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

def multiplication_table():
    v = list(range(1,13))
    
    table = numpy.outer(v,v)
    return table


class Gizmo:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(self.name)
        
        