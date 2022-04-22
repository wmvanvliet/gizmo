# Test gizmo file
def hello(name, country='Finland'):
  print('Hello {name}, how are things in {country}?')
  
def spell(name):
  total_chars = len(name)
  for idx,char in enumerate(name):
    print(char, end="")
    if idx != total_chars-1:
      print(".", end="")
