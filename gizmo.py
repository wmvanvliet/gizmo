# Function for saying hello, with the default country set to Finland
def hello(name, country = "Finland"):
    print("Hello", name + ", how are things in", country + "?")

# Spelling function
def spell(word):
    for letter in word:
        print (letter + '.', end = '')

# creating a relative path finder
# takes an array as an argument and parses it into strings
def relative_path(arr):
    for i in arr:
        i = './subjects/mock_recording_'+i+'.rec'
        print(i)
