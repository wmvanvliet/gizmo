import numpy as np


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


def hello(name, country="Finland"):
    print(f"Hello {name}, how are things in {country}?")


def spell(word):
    print(".".join(word))


def relative_path(subject_identifiers):
    return [
        f"./subjects/mock_recording_{subject_identifier}.rec"
        for subject_identifier in subject_identifiers
    ]


def multiplication_table():
    return np.outer(np.arange(1, 13), np.arange(1, 13))
