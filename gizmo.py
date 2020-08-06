import numpy as np

# Exercise 2
def hello(name, country='Finland'):
  print(f'Hello {name}, how are things in {country}?')

# Exercise 3
def spell(word):
    ans = ""
    for i in range(len(word)-1):
        ans += word[i]
        ans += '.'
    ans += word[len(word)-1]
    print(ans)
    
# Exercise 4    
def relative_path(identifiers):
    paths = []
    for id in identifiers:
        name = f'./subjects/mock_recording_{id}.rec'
        paths.append(name)
    return paths
  
# Exercise 5  
class Gizmo:
    
    # Exercise 6
    def __init__(self, name):
        self.name = name

    # Exercise 7    
    def speak(self):
        print(self.name)

# Exercises 8, 9 and 10

def multiplication_table(zero_out_multiples = None):
    """Multiplication table from 1 to 12.

    Extended summary
    =================
    This function returns the multiplication table from 1 to 12 as a 2-dimensional array.
    If given a number as an input, the function will display all multiples of this number as zero.

    Parameters
    ===========

    :zero_out_multiples: int, optional
    
    If 'zero_out_multiples' is defined, the function will display all multiples of 'zero_out_multiples' as zero.
    The default value of 'zero_out_multiples' is None.

    Returns
    =========
    :out: ndarray
    The function returns a 2-dimensonal NumPy array (i.e. a matrix) that contains the multiplication table from 1 to 12.
    """
    a = np.arange(1, 13)
    b = a
    out = np.outer(a, b)
    if zero_out_multiples:
        out[out % zero_out_multiples == 0] = 0
    return out

# Exercise 11
def generate_fibonacci_sequence(n):
    n1, n2 = 0, 1
    cnt = 2
    if n==0:
        yield()  
    elif n==1:
        yield(n1)
    elif n>1:
        yield(n1)
        yield(n2)
        while cnt < n:
            nth = n1 + n2
            yield(nth)
            # update values
            n1 = n2
            n2 = nth
            cnt += 1

# Exercise 12
def get_fibonacci_sequence(n):
    seq = []
    cnt = 0
    fb = generate_fibonacci_sequence(n)
    while cnt < n:
        seq.append(next(fb))
        cnt += 1
    return seq


    
