def hello(name,country="Finland"):
    print("Hello {0}, how are things in {1}?".format(str(name),str(country)))

def spell(input_str):
    result=input_str[0]
    for i in input_str[1:]:
        result+="."+i
        
    return print(result)

def relative_path(subject_identifiers,relpath='./subjects/moc_recording'):
    names=[]
    relpath='./subjects/mock_recording_'
    for i in subject_identifiers:
        res=relpath+"_"+i+".rec"
        names.append(res)

    return names

class Gizmo:
    pass
