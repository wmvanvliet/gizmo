# file for python testing test
class Gizmo:

  def __init__(self, name):
    self.name = name
  
  def speak(self):
    print(self.name)
  
  @property
  def friendship_name(self):
    """ The friendship name, i.e. the name, reversed and capitalized as a proper noun """
    inv_name=self.name[::-1]
    return inv_name.casefold().capitalize()
  
