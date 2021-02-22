import numpy as np
import pandas as pd


def hello(name, country='Finland'):
    print(f'Hello {name}, how are things in {country}?')


def spell(word):
    if len(word) == 0:
        return
    s = word[0]
    for letter in word[1:]:
        s += '.' + letter
    print(s)


def relative_path(subject_identifiers):
    paths = []
    for subject in subject_identifiers:
        path = f'./subjects/mock_recording_{subject}.rec'
        paths.append(path)
    return paths


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


def multiplication_table(zero_out_multiples=None):
    """Build a multiplication table.

    This function builds a multiplication table from 1 to 12.

    Parameters
    ----------
    zero_out_multiples : int
        The multiples of this value are set to zero.

    Returns
    -------
    table : np.ndarray
        Multiplication table as a two-dimensional array.
    """
    table_ij = np.outer(range(1, 13), range(1, 13))
    if zero_out_multiples is not None:
        flt_ij = table_ij % zero_out_multiples == 0
        table_ij[flt_ij] = 0
    return table_ij


def generate_fibonacci_sequence(n):
    if n < 0:
        return

    vals = [0, 1]
    for i in range(min(2, n)):
        yield vals[i]

    for i in range(2, n):
        val = sum(vals)
        vals = [vals[-1], val]
        yield val


def get_fibonacci_sequence(n):
    return np.array(list(generate_fibonacci_sequence(n)))


def get_titanic():
    return pd.read_csv('titanic.csv')


def get_titanic_children():
    df = get_titanic()
    return df[df['age'] <= 12]
