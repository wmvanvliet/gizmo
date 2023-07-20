# hello function
def hello(name, country = "Finland"):
    print("Hello", name + ", how are things in", country + "?")
# spelling function
def spell(word):
    for letter in word:
        print (letter + '.', end = '')
        
# editing strings
def relative_path(arr):
    for i in arr:
        i = './subjects/mock_recording_'+i+'.rec'
        print(i)

# creating a class     
class Gizmo:
    def __init__(self,name = "default"):
        self.name = name
        
    def speak(self):
        print(self.name)
    
# function for fibonacci
def generate_fibonacci_sequence(n):
    seq = []
    iterator = iter(seq)
    a, b = 0,1
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return iterator
