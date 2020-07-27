import numpy as np

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
    table = np.outer(np.arange(1, 13), np.arange(1, 13))
    if zero_out_multiples is not None:
        table[table % zero_out_multiples == 0] = 0
    return table
