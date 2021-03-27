import numpy as np

def hello(name, country='Finland'):
    print(f"Hello {name}, how are things in {country}?")

def spell(word):
    wordlength = 0
    letters = []
    spelling = ""
    for letter in word:
        wordlength += 1
        letters.append(letter)
    for i in range (wordlength):
        if i == wordlength - 1:
            spelling += letters[i]
        else:
            spelling += letters[i] + '.'
    print(spelling) 

def relative_path(list):
    output_list = []
    for subject_identifier in list:
        output_list.append(
            f'./subjects/mock_recording_{subject_identifier}.rec')
    return output_list

class Gizmo:

    name = None

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name)

def multiplication_table(zero_out_multiples=None):
    """Creates a multiplication table.

    Returns a two-dimensional NumPy array that contains the multiplication 
    table from 1 to 12.  
    
    Paramateres
    -----------
    zero_out_multiples : int
        When this parameter is set to an integer number, then the 
        multiplication table that is returned by the function will have all
        multiples of the given number set to zero. The default value of this 
        parameter is None.

    Returns
    -------
    array : numpy ndarray
        A two-dimensional NumPy array that contains the multiplication table 
        from 1 to 12 with the multiples of zero_out_multiples paramaters 
        passed as argument set to zero. 
    """
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    array = np.outer(a, a)
    array[array % zero_out_multiples == 0] = 0
    return array
    


