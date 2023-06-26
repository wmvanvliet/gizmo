def hello(name, country = "Finland"):
    print("Hello ", name, " How's life in ", country, "?")

def spell(woord):
    teller = 1
    for i in woord:
        print(i, end='')
        if teller < len(woord):
            print(".", end='')
        teller += 1
    print()
