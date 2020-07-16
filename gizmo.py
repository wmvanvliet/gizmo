import numpy as np

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
