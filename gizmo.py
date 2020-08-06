def hello(name, country='Finland'):
  print(f'Hello {name} , how are things in {country}?')

def spell(word):
    ans = ""
    for i in range(len(word)):
        ans += word[i]
        ans += '.'
    print(ans)
    
def relative_path(identifiers):
    paths = []
    for id in identifiers:
        name = f'./subjects/mock_recording_{id}.rec'
        paths.append(name)
    return paths
  
  
    
