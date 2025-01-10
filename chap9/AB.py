class ArbreBinaire:
  """Structure de donnée d'arbre binaire

  Attributs
  ---------
  data: type simple int, float, str
      étiquette du nœud
  gauche: objet de type ArbreBinaire ou None si vide
      sous-arbre gauche
  droit: objet de type ArbreBinaire ou None si vide
      sous-arbre droit
  """

  def __init__(self, data, gauche=None, droit=None):
    self.data = data
    self.gauche =  gauche
    self.droit = droit
 
  def __str__(self):
    if self.data == None:
        return ""
    else:
        return str(self.data)
  
  def est_vide(self):
    if self.data:
        return False
    return True

  def est_feuille(self):
    return not (self.droit or self.gauche)

  def branche(self, noeud):
    if self.est_vide():
      self.data = noeud.data
      self.gauche = noeud.gauche
      self.droit = noeud.droit
      return self
    else:
      if not self.gauche:
        self.gauche = noeud
        return self.gauche
      elif not self.droit:
        self.droit = noeud
        return self.droit

  def hauteur(self):
    if self.est_vide():
      return -1
    else:
      hauteur_gauche = self.gauche.hauteur() if self.gauche else -1
      hauteur_droit = self.droit.hauteur() if self.droit else -1
      return 1 + max(hauteur_gauche, hauteur_droit)

  def profondeur(self, noeud):
    if self.est_vide():
      return -1
    if self == noeud:
      return 0
    else:
      if self.gauche:
        profondeur_gauche = self.gauche.profondeur(noeud)
        if profondeur_gauche != -1:
          return 1 + profondeur_gauche
      if self.droit:
        profondeur_droit = self.droit.profondeur(noeud)
        if profondeur_droit != -1:
          return 1 + profondeur_droit
    return -1
  
  def taille(self):
    compteur = 1
    if self.est_vide():
        return -1
    if self.est_feuille():
      return 1
    else:
      if self.gauche:
        compteur += self.gauche.taille()
      if self.droit:
        compteur += self.droit.taille()
      return compteur
  
  
        
def affiche(arbre):
  if arbre != None:
    return (arbre.data, affiche(arbre.gauche), affiche(arbre.droit))