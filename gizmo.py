def hello(name, country=None):
    
    assert isinstance(name, str),"You forgot your name! unless you are Elon's baby, then sorry write your nickname"
    if (country!=None):
        assert isinstance(country,str),"hmmm... that is not a country, please write a valid country"
    else:
        country="Finland"
    print("Hello %s, how are things in %s?" % (name, country))

def spell(word):
    assert isinstance(word, str),"please enter a valid word, you know... with letters"
    for i, letter in enumerate(word):
        if i == len(word) - 1:
            print(letter)
        else:
            print(letter+".", end="")

def relative_path(subject_identifiers):
    names = []
    for identifier in subject_identifiers:
        name = f"./subjects/mock_recording_{identifier}.rec"
        names.append(name)
    return names

class Gizmo(object):
    def __init__(self, name):  
        self.name = name  
    
    def speak(self):  
        print(self.name)  

def multiplication_table(zero_out_multiples=None):
    """ Returns a multiplication table form 1 to 12
    
    Parameters
    ----------
    zero_out_multiples : int, optional
                        multiples of this parameter will be deleted
    
    Returns
    -------
    array : array
            array type with the multiplication table from 1 to 12. If specified
            the multiples of zero_out_multiples are set to 0.
    """
    if (zero_out_multiples!=None):
        assert isinstance(zero_out_multiples,int),"please enter an integer"
    else:
        zero_out_multiples=0
    
    i = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    array = np.outer(i,i)
    
    if zero_out_multiples!=0:
        array[(array % zero_out_multiples == 0)] = 0
        
    return array

def generate_fibonacci_sequence(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def get_fibonacci_sequence(n):
    array=[]
    fib = generate_fibonacci_sequence(n)
    while(True):
        array.append(next(fib))
    return np.array(array)

def get_titanic():
    import pandas as pd
    return pd.read_csv("./titanic.csv")

def get_titanic_children():
    import pandas as pd
    df = pd.read_csv("./titanic.csv")
    df = df[df['age'] < 13]
    return df
    