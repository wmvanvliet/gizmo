#!/usr/bin/python3
import numpy as np

def hello(name, country='Finland'):
    
    print('Helllo {}, how are things in {}?'.format(name,country))
    
    return


def spell(str_in):
    
    str_out = str_in[0]
    for el in str_in[1:]:
        str_out += '.' + el
    print(str_out)
    
    return

def relative_path(subject_identifiers):
    
    rel_path = './subjects/mock_recording_'
    ext = '.rec'
    
    file_list = [rel_path + elem + ext for elem in subject_identifiers]
    
    return file_list
  
class Gizmo(object):
  
    def __init__(self, name):
      
        self.name = name
      
        return
    
    def speak(self):
        
        print(self.name)
        
        return
      
def multiplication_table(zero_out_multiples=None):
      
      mat = np.outer(np.arange(1,13,1),np.arange(1,13,1))
      
      if zero_out_multiples is None:
          print(mat)
      else:
          mat[mat % zero_out_multiples == 0] = 0
          print(mat)
      
      return
      
      
    
    
