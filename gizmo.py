#Ex 2
def hello(name,country='Finland'):
    print('Hello ',name,', how are things in ',country,'?',sep='')
        
#Ex 3
def spell(word):
    for letter in range(0,len(word)-1):
        print(word[letter],end='.')
    print(word[len(word)-1])

#Ex 4
def relative_path(identifiers):
    names=[ ]
    for element in identifiers:
        names.append(f"./subjects/mock_recording_{element}.rec")
    return names

#Ex 5, 6 and 7
class Gizmo:
    def __init__(self, name):
        self.name = name 
        
    def speak(self):
        print(self.name)
        
#Ex 9 and 10
def multiplication_table(zero_out_multiples=None):
    import numpy as np
    mat=np.outer(np.arange(1,13,1),np.arange(1,13,1))
    if ( zero_out_multiples!= None):  
        mat[mat%zero_out_multiples==0]=0
    return mat