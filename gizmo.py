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
        
#Ex 8, 9 and 10
def multiplication_table(zero_out_multiples=None):    
    """
    Returns the multiplication tables from 1 to 12 in an array.

    This function returns a 12*12 array containing the numbers corresponding 
    to the multiplication tables from 1 to 12. It is possible to ask the 
    tables setting to 0 all multiples of any integer in the array.

    Parameters
    ----------
    zero_out_multiples : int or None, optional
        Non-zero value multiples will be set to 0, or None by default.
    
    Returns
    -------
    mat : array
        Contains the multiplication tables from 1 to 12 with the selected 
        values set to 0

    """
    
    import numpy as np
    mat=np.outer(np.arange(1,13,1),np.arange(1,13,1))
    if ( zero_out_multiples!= None):  
        mat[mat%zero_out_multiples==0]=0
    return mat

#Ex 11
def generate_fibonacci_sequence(n):
    num=1;fib=0
    for i in range(0,n,1):
        yield fib
        fib , num=num , fib+num
        
#Ex 12
def get_fibonacci_sequence(n):
    import numpy as np
    fib_list=np.empty(n,dtype=int)
    fibo=generate_fibonacci_sequence(n)
    for element in range(n):
        fib_list[element]=next(fibo)
    return fib_list

#Ex 13
def get_titanic():
    import pandas as pd
    titanic = pd.read_csv("titanic.csv")
    return titanic

#Ex 14
def get_titanic_children():
    import pandas as pd
    titanic = pd.read_csv("titanic.csv")
    titanic_children=titanic[titanic["age"] <= 12]
    return titanic_children
