def hello(name, country):
    print("Hello %s, how are things in %s?" % (name, country))
    
def spell(word):
    for i in word:
        print(i,end='')
        if i != word[-1]:
            print(".",end='')
