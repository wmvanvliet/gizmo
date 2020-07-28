import numpy as np
import os.path


def hello(name, country='Finland'):
    print(f'Hello {name}, how are things in {country}?')


def spell(word):
    print('.'.join(list(word)))


def relative_path(ids):
    return [os.path.join('.', 'subjects', f'mock_recording_{i}.rec')
            for i in ids]


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


def multiplication_table(zero_out_multiples=None):
    """
    A multiplication table such as you might learn in school.

    Creates an array with the times tables of the numbers from 1 to 12.
    The optional `zero_out_multiples` argument can be used to change certain
    times tables to zero.

    Parameters:
    -----------
    zero_out_multiples : int or None, optional
        If not None, causes the times table of `zero_out_multiples` and its
        multiples to be changed to zero.
        The default is None.

    Returns:
    --------
    table : numpy.ndarray
        A 12x12 array with the times tables from 1 to 12, with some times
        times tables optionally changed to zero.
        The array is diagonally symmetric.

    """
    count = np.arange(1, 13)
    if zero_out_multiples is not None:
        count[count % zero_out_multiples == 0] = 0
    return np.outer(count, count)
