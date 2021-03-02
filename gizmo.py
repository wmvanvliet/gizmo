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

    

