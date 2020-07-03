class Gizmo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

    @property
    def friendship_name(self):
        return self.name[::-1].title()
