import gizmo

  
def hello(a,country='Finland'):
  print('Hello %s, how are things in %s?'%(a, country) )

def spell(word):
  spell_word=''
  for i in word:
    spell_word=spell_word+i+'.'
  spell_word = spell_word[:-1]
  print(spell_word)

def relative_path(subj):
  names=[]
  for i in subj:
      subject_identifier=i
      a=f"./subjects/mock_recording_{subject_identifier}.rec"
      names.append(a)
  return names
