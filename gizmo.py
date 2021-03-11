from pandas.core.frame import DataFrame


def hello(name,country="Finland"):
    print("Hello {0}, how are things in {1}?".format(str(name),str(country)))

def spell(input_str):
    result=input_str[0]
    for i in input_str[1:]:
        result+="."+i
        
    return print(result)

def relative_path(subject_identifiers,relpath='./subjects/moc_recording'):
    names=[]
    relpath='./subjects/mock_recording'
    for i in subject_identifiers:
        res="{0}_{1}.rec".format(relpath,i) #new style
        #res=relpath+"_"+i+".rec" #old style, not good
        names.append(res)

    return names

class Gizmo:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print(self.name)


def multiplication_table(zero_out_multiples=None):
    """ 
    Calculates a multiplication table based on two vectors ranging from 1 to 12 each.

    The function multiplication_table caclulates a multiplication table for all numbers between 1 to 12. If the input argument zero_out_multiples is not None, multiplies of this input argument in the table will be all set to zero.

    Parameters
    ----------
    zero_out_multiples: int, default = None
        The arg is used for the multiplication table. If it is not None, the table returned by the function will have all multiples of the given number set to zero.

    Returns
    -------
    res: numpy.ndarray
        The arg contains the calculated multiplication table. Calculation is based on the outer product.
    """
    import numpy as np

    a=np.arange(1,13,1)
    b=np.arange(1,13,1)

    if zero_out_multiples is not None and isinstance(zero_out_multiples, int):
        #Version with modulo
        a[a%zero_out_multiples==0]=0  #okay, I learned something :-)
        b[b%zero_out_multiples==0]=0    

        #I found a version without modulo operator
        #index=zero_out_multiples-1
        #a[index::zero_out_multiples]=0
        #b[index::zero_out_multiples]=0
        res=np.outer(a,b)
    else:
        res=np.outer(a,b)
    
    return res

def generate_fibonacci_sequence(n):
    a, b = 1, 0
    for i in range(0, n):
        a, b = b, a + b
        yield a


def get_fibonacci_sequence(n):
    import numpy as np
    res=generate_fibonacci_sequence(n)
    #Comment: I found this example, but I am still not sure, how list works on res. It is still mysterious here.
    return np.array(list(res))
        
def get_titanic():
    import pandas as pd
    titanic=pd.read_csv("./titanic.csv")
    return titanic

def get_titanic_children():
    titanic=get_titanic()
    children=titanic.loc[titanic["age"]<=12,:]
    #children=titanic[titanic["age"]<=12] #this works, too
    return children