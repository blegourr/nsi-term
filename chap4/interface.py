class Pile:
  def __init__(self) -> None:
    self.pile=[]

  def vide(self):
    return self.pile==[]

  def empiler(self,x):
    self.pile.append(x)
    
  def depiler(self):
    assert not self.vide()
    return self.pile.pop()
  
  def taille(self):
    return len(self.pile)

  def sommet(self):
    return self.p[len(self.pile) - 1]