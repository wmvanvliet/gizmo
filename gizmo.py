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

class Gizmo:
    def __init__(self,na):
        self.name=na
    
    def speak(self):
        print(self.name)

    def multiplication_table(zero_out_multiples=None):

        a=np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
        b=np.transpose(a)
        c=a*b
        
        if zero_out_multiples==None:
            return c
        else:
            d=12%zero_out_multiples
            e=(12-d)/zero_out_multiples
            e=int(e)
            
            for i in range(e):
                c[(i+1)*5-1,:]=0
                c[:,(i+1)*5-1]=0
            
            return c
          
