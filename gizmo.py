import gizmo

  
def hello(a,country='Finland'):
  print('Hello %s, how are things in %s?'%(a, country) )

def spell(word):
  spell_word=''
  for i in word:
    spell_word=spell_word+i+'.'
    spell_word = spell_word[:-1]
  print(spell_word)
