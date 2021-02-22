"""Solutions to the Gizmo challenge by Joakim Loefgren. """
import numpy as np
import pandas as pd


def hello(name, country="Finland"):
    print(f"Hello {name}, how are things in {country}?")


def spell(word):
    spelled_word = ""
    for char in word[:-1]:
        spelled_word += char + "."

    spelled_word += word[-1]
    print(spelled_word)


def relative_path(subject_identifiers):
    paths = [f"./subjects/mock_recording_{sub}.rec" for sub in subject_identifiers]
    return paths


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


def multiplication_table(zero_out_multiples=None):
    """The products of integers 1 to 12.

    Calculates all possible products of integers 1 to 12 (inclusive),
    i.e. a multiplication table. Optionally, products that are multiples of a
    given number are zeroed out in the table.

    Parameters
    ----------
    zero_out_multiples : int
        If specified, products in the multiplication table that are
        multiples of this number will be set to 0.

    Returns
    -------
    table : np.ndarray
        A 12x12 array where element (i, j) is the product (i + 1) x (j + 1) unless
        zero_out_multiples was provided, in which case multiples of this value are
        set to 0.
    """
    arr = np.arange(1, 13)
    table = np.outer(arr, arr)
    if zero_out_multiples:
        table[table % zero_out_multiples == 0] = 0

    return table


def generate_fibonacci_sequence(n):
    count = 0
    a, b = 0, 1
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def get_fibonacci_sequence(n):
    # alternatively: np.fromiter(generate_fibonacci_sequence(n), dtype=np.int64)
    seq = np.array(list(generate_fibonacci_sequence(n)))
    return seq


def get_titanic():
    df = pd.read_csv("titanic.csv")
    return df


def get_titanic_children():
    df = get_titanic()
    return df[df["age"] <= 12]
