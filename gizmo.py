import numpy as np
import pandas as pd


def hello(name, country="Finland"):
    print(f"Hello {name}, how are things in {country}?")


def spell(s):
    res = ""
    for l in s:
        res += l + '.'
    return res[:-1]


def relative_path(ids):
    return [f'./subjects/mock_recording_{i}.rec' for i in ids]


def multiplication_table(zero_out_multiples=None):
    """
    Generate a multiplication table.

    Function for generating a multiplication table from 1 to 12,
    with an option to zero out certain multiples

    Parameters
    ----------
    zero_out_multiples : int, optional
        Multiples of which numbers to zero out

    Returns
    -------
    out : (12, 12) ndarray
        ``out[i, j] = (i+1) * (j+1)``
    """
    v = np.arange(1, 13)
    out = np.outer(v, v)
    if zero_out_multiples is not None:
        out[out % zero_out_multiples == 0] = 0
    return out


def generate_fibonacci_sequence(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def get_fibonacci_sequence(n):
    return np.array(list(generate_fibonacci_sequence(n)))


def get_titanic():
    return pd.read_csv('titanic.csv')


def get_titanic_children():
    df = get_titanic()
    return df[df.age <= 12]


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)
