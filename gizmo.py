def hello(name, country=None):
    
    assert isinstance(name, str),"You forgot your name! unless you are Elon's baby, then sorry write your nickname"
    if (country!=None):
        assert isinstance(country,str),"hmmm... that is not a country, please write a valid country"
    else:
        country="Finland"
    "Hello %s, how are things in %s" % (name, country)

def spell(word):
    assert isinstance(name, str),"please enter a valid word, you know... with letters"
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