import numpy as np
import pandas as pd

def hello(name, country='Finland'):
    print(f'Hello {name}, how are things in {country}?')

def spell(word):
    for w in word[:-1]:
        print(w, end='')
        print('.', end='')
    print(word[-1], end='')

def relative_path(subjects):
    return [f'./subjects/mock_recording_{subj}.rec' for subj in subjects]

class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

    @property
    def friendship_name(self):
        return self.name[::-1].title()

def multiplication_table(zero_out_multiples=None):
    """Construct a multiplication table.

    This function constructs a multiplication table with the numbers 1 to 12,
    like the one you had to learn in elementary school. Optionally, if you
    don't like certain numbers, you can zero out multiples of them.

    Parameters
    ----------
    zero_out_multiples : int, optional
        When specified, all numbers that are multiples of the given value are
        set to zero in the table.

    Returns
    -------
    table : array (12, 12)
        The multiplication table. Possibly with values zero-ed out.
    """
    table = np.outer(np.arange(1, 13), np.arange(1, 13))
    if zero_out_multiples is not None:
        table[table % zero_out_multiples == 0] = 0
    return table

def generate_fibonacci_sequence(n):
    a = 0
    b = 1
    yield a
    yield b
    for _ in range(n - 2):
        a, b = b, a + b
        yield b

def get_fibonacci_sequence(n):
    return np.array(list(generate_fibonacci_sequence(n)))

def get_titanic():
    return pd.read_csv('titanic.csv')

def get_titanic_children():
    return get_titanic().query('age <= 12')
