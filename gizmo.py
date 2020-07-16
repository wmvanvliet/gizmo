# file for python testing test


class Gizmo:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

    @property
    def friendship_name(self):
        """ The friendship name, i.e. the name, reversed and capitalized as a proper noun """
        inv_name = self.name[::-1]
        return inv_name.casefold().capitalize()

    def spell(self):
        outstring = self.name[0]
        for elem in self.name[1:len(self.name) + 1]:
            outstring = outstring + '.' + elem
        print(outstring)


def relative_path(subject_identifiers):
    output_path = []
    for ident in subject_identifiers:
        output_path.append(f'./subjects/mock_recording_{ident}.rec')
    return output_path
