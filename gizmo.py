def hello(name,country="Finland"):
    print("Hello {0}, how are things in {1}?".format(str(name),str(country)))

def spell(input_str):
    result=input_str[0]
    for i in input_str[1:]:
        result+="."+i
        
    return print(result)

def relative_path(subject_identifiers,relpath='./subjects/moc_recording'):
    names=[]
    relpath='./subjects/mock_recording'
    for i in subject_identifiers:
        res="{0}_{1}.rec".format(relpath,i) #new style
        #res=relpath+"_"+i+".rec" #old style, not good
        names.append(res)

    return names

class Gizmo:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print(self.name)

def multiplication_table():
    import numpy as np
    a=np.arange(1,13,1)
    b=np.arange(1,13,1)
    res=np.outer(a,b)
    return res


        

