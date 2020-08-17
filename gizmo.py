import numpy as np
import pandas as pd


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


def hello(name, country="Finland"):
    print(f"Hello {name}, how are things in {country}?")


def spell(word):
    result = ""
    for c in word:
        result = result + c + "."
    print(result[:-1])


def relative_path(subject_identifiers):
    return [
        f"./subjects/mock_recording_{subject_identifier}.rec"
        for subject_identifier in subject_identifiers
    ]


def multiplication_table(zero_out_multiples=None):
    """Returns a multiplication table from 1 to 12

    The table shows you the results of multiplying two numbers. One number is along a row, the other down a column, and the results are shown where a row and column meet.

    Parameters
    ----------
    zero_out_multiples : int, optional
        When this parameter is set to an integer number, then the multiplication table that is returned by the function will have all multiples of the given number set to zero.

    Returns
    -------
    multiplication_table : ndarray
        Multiplication table
    """
    array = np.arange(1, 13)
    result = np.outer(array, array)
    if zero_out_multiples is not None:
        result[result % zero_out_multiples == 0] = 0
    return result


def generate_fibonacci_sequence(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def get_fibonacci_sequence(n):
    return np.array(list(generate_fibonacci_sequence(n)))


def get_titanic():
    return pd.read_csv("titanic.csv")


def get_titanic_children():
    titanic = get_titanic()
    return titanic[titanic["age"] <= 12]
