# Exercise 2
def hello(name, country='Finland'):
  print(f'Hello {name} , how are things in {country}?')

# Exercise 3
def spell(word):
    ans = ""
    for i in range(len(word)):
        ans += word[i]
        ans += '.'
    print(ans)
    
# Exercise 4    
def relative_path(identifiers):
    paths = []
    for id in identifiers:
        name = f'./subjects/mock_recording_{id}.rec'
        paths.append(name)
    return paths
  
# Exercise 5  
class Gizmo:
    
    # Exercise 6
    def __init__(self, name):
        self.name = name

    # Exercise 7    
    def speak(self):
        print(self.name)

# Exercise 8 and 9

import numpy as np

def multiplication_table(zero_out_multiples=None):
    a = np.arange(1, 13)
    b = a
    out = np.outer(a, b)
    if zero_out_multiples:
        out[out % zero_out_multiples == 0] = 0
    return out
       
  
    
