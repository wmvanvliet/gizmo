#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from dataclasses import dataclass
from numpy import arange, array
from numpy.ma import outerproduct
from pandas import read_csv


def hello(name: str, country: str = "Finland"):    
    """Prints a friendly greeting.

    """
    print(f"Hello {name}, how are things in {country}?")


def spell(word: str):
    """Spells out the given `word`.

    """
    for i,letter in enumerate(word):
        if i > 0: 
            print('.', end='')
        print(letter, end='')
    print()

    #print(".".join(word))   # <-- this is the correct pythonic solution

def relative_path(ids: List[str], path_fmt: str = "./subjects/mock_recording_{id}.rec"):
    """Returns the given `ids` as a list with the given `path_fmt`.

    Example
    -------
    >>> relative_path(['foo', 'bar'])
    ['./subjects/mock_recording_foo.rec', ./subjects/mock_recording_bar.rec']

    """
    return [path_fmt.format(id=_id) for _id in ids]


def multiplication_table(n: int=12, zero_out_multiples: int=None):
    """Returns a 2-dimensional multiplication table for size `n`.

    A multiplication table will contain all the multiples 1x1, 1x2, ..., 1xn 
    on the first row; 2x1, 2x2, ..., 2xn on the seconds row; until nx1, nx2,
    ..., nxn on the last row.

    Certain multiples can be 'zeroed out' by giving the parameter `zero_out_multiples`.
    For example, giving the value '2' will make all even numbers zero on the 
    output array.


    Parameters
    ----------
    n : int
        Size of returned array 1...n

    zero_out_multiples : int or None
        Multiples of this number are 'zeroed out' in the array.

    Returns
    -------
    numpy.ndarray
        nxn sized array of type int.

    """
    ns = arange(n, dtype=int)+1   # Counting starts from 1
    arr = outerproduct(ns, ns)
    if zero_out_multiples is not None:
        arr[arr % zero_out_multiples == 0] = 0
    return arr


def generate_fibonacci_sequence(n: int):
    """Generator for the first `n` Fibonacci numbers.

    Yields
    ------
    int
        The next fibonacci number

    """
    f1, f2 = 0, 1   # Fibonacci sequence starts with 0, 1, 1, 2, ...
    for i in range(n):
        if i == 0:
            yield f1
        elif i == 1:
            yield f2
        else:
            f1, f2 = f2, f1 + f2
            yield f2


def get_fibonacci_sequence(n: int):
    """Returns an array of first `n` Fibonacci numbers.

    Returns
    -------
    numpy.ndarray
        First `n` Fibonacci numbers in a numpy array.

    """
    return array(list(generate_fibonacci_sequence(n)))


def get_titanic(titanic_csv: str="titanic.csv"):
    """Reads the data from `titanic_csv` and returns it as a Pandas data frame.

    Returns
    -------
    pandas.DataFrame
        Titanic passanged data.

    """
    return read_csv(titanic_csv)


def get_titanic_children(titanic_csv: str="titanic.csv"):
    """Reads and returns all the children from the `titanic_csv` file.

    Returns
    -------
    pandas.DataFrame
        Filtered out data of children on the Titanic.

    """
    return get_titanic(titanic_csv).query('age <= 12.0')


@dataclass
class Gizmo():
    name: str

    def speak(self):
        """Prints the name of this gizmo.

        """
        print(self.name)

    @property
    def friendship_name(self):
        """Returns the friendship name for this gizmo.

        """
        return self.name[-1].upper() + self.name[::-1].lower()[1:]



    