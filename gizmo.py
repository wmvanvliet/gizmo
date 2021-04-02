def hello(name, country):
    
    print("Hello %s, how are things in %s?" % (name, country))
    
def spell(word):
    
    for i in range(0, len(word)):
        print(word[i], end = '')
        if i != len(word)-1:
            print(".", end = '')

def relative_path(subject_identifier):
    names = []
    for i in subject_identifier:
        path= './subjects/mock_recording_%s.rec' % (i)
        names.append(path)
    return names

class Gizmo:
     def __init__(name):
         self.name = name

