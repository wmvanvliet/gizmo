import numpy as np

# exercise 2
def hello(name, country="Finland"):
    print(f"Hello {name}, how are things in {country}?")

# exercise 3
def spell(word):
    spelled = ""
    for i in word:
        spelled += i + "."
    print(spelled[:-1])

# exercise 4
def relative_path(subject_identifiers):
    files = []
    for subject_identifier in subject_identifiers:
        files.append(f'./subjects/mock_recording_{subject_identifier}.rec')
    return files

# exercise 5,6,7
class Gizmo():
    def __init__(self,name):
        self.name = name
    def speak(self): 
            print(self.name)

# exercise 8
def multiplication_table():
    return np.outer(np.array(range(1,13)),np.array(range(1,13)))



        
    
    
        
        
