def hello(name, country=None):
    
    assert isinstance(name, str),"You forgot your name! unless you are Elon's baby, then sorry write your nickname"
    if (country!=None):
        assert isinstance(country,str),"hmmm... that is not a country, please write a valid country"
    else:
        country="Finland"
    print("Hello %s, how are things in %s?" % (name, country))

def spell(word):
    assert isinstance(word, str),"please enter a valid word, you know... with letters"
    for letter in word:
        if letter == word[-1]:
            print(letter)
        else:
            print(letter+".", end="")

def relative_path(subject_identifiers):
    rp = "./subjects/mock_recording_"
    names = []
    for identifier in subject_identifiers:
        name = rp+identifier+".rec"
        names.append(name)
    return names

class Gizmo(object):
    def __init__(self, name):  
        self.name = name  
    
    def speak(self):  
        print(self.name)  

def multiplication_table():
    i = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    array = np.outer(i,i)
    return array