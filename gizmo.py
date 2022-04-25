from functools import lru_cache

# Test gizmo file
def hello(name, country='Finland'):
  print(f'Hello {name}, how are things in {country}?')

def spell(name):
  total_chars = len(name)
  for idx,char in enumerate(name):
    print(char, end="")
    if idx != total_chars-1:
        print(".", end="")
    else:
        print("\n")

def relative_path(subject_identifiers):
    names = []
    pattern = './subjects/mock_recording_{subject_identifier}.rec'
    for item in subject_identifiers:
        names.append(pattern.format(subject_identifier=item))
    return names

class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

@lru_cache(maxsize=128)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def generate_fibonacci_sequence(n):
    """ Yields first `n` fibonacci numbers 

    Given an integer `n`, returns an iterator which yields first `n` Fibonacci numbers.

    Parameters
    ----------
    n : int
        First `n` Fibonacci numbers.

    Yields
    ------
    nth_fib : int
              The n_th Fibonacci number. n = 0 nth_fib = 0; n = 1 nth_fib = 1, n = 2 nth_fib = 1

    Example
    -------
    >>> [_ for _ in gizmo.generate_fibonacci_sequence(5)]
    [0, 1, 1, 2, 3]
    """
    for i in range(n):
        nth_fib = fib(i)
        yield nth_fib

        
