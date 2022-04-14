def hello(name, country="Finland"):
    return f"Hello {name}, how are things in {country}"

def spell(word):
    spelling = ''
    for l in word:
        spelling += l
        spelling += '.'
    return spelling[:-1]


