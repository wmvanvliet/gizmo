def hello(name, country='Finland'):
    print(f"Hello {name}, how are things in {country}?")

def spell(word):
    wordlength = 0
    letters = []
    spelling = ""
    for letter in word:
        wordlength += 1
        letters.append(letter)
    for i in range (wordlength):
        if i == wordlength - 1:
            spelling += letters[i]
        else:
            spelling += letters[i] + '.'
    print(spelling) 

def relative_path(list):
    output_list = []
    for subject_identifier in list:
        output_list.append(f'./subjects/mock_recording_{subject_identifier}.rec')
    return output_list

class Gizmo:

    name = None

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name)



