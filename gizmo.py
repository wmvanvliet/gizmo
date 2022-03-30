"""
My Gizmo module!
"""


def hello(name, country='Finland'):
    print(f'Hello {name}, how are things in {country}?')


def spell(word):
    word_spelled = ''
    for letter in word[:-1]:
        word_spelled += letter + '.'
    word_spelled += word[-1]
    print(word_spelled)


def relative_path(subjects):
    return [f'./subjects/mock_recording_{s}.rec' for s in subjects]


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

    def generate_fibonacci_sequence(n):
        """Generate the first n Fibonacci numbers.

        The Fibonacci sequence starts with [0, 1]. Then, each next number is
        the sum of the previous two numbers.

        Parameters
        ----------
        n : int
            The number of Fibonacci numbers to generate.

        Yields
        ------
        x : int
            The next Fibonacci number.
        """
        a, b = 0, 1
        for i in n:
            if i == 0:
                yield a
            elif i == 1:
                yield b
            else:
                a, b = b, a + b
                yield b
