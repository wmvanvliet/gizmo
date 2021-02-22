import numpy as np


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
    table_ij = np.outer(range(1, 13), range(1, 13))
    if zero_out_multiples is not None:
        flt_ij = table_ij % zero_out_multiples == 0
        table_ij[flt_ij] = 0
    return table_ij
