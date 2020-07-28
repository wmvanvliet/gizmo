import os.path


def hello(name, country='Finland'):
    print(f'Hello {name}, how are things in {country}?')


def spell(word):
    print('.'.join(list(word)))


def relative_path(ids):
    return [os.path.join('.', 'subjects', f'mock_recording_{i}.rec')
            for i in ids]


class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)
