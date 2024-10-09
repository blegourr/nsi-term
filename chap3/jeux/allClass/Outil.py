  
"""
  Créationn d'outil
"""
class Outil:
  """
    class pour gérer les outils        
  """

  def __init__(self, experianceMin:int, masse:int, main:int=1):
    """
      initialistations d'un personnage lors de la création
    """
    self.__masse = masse
    self.experianceMin = experianceMin
    self.__main = main
    
  def get_masse(self):
    """
      renvoie l'éxpériance actuelle du personnage
    """
    return self.__masse

  def get_main(self):
    """
      renvoie l'éxpériance actuelle du personnage
    """
    return self.__main

  def __dim1_main(self, experriance:int):
    """
      diminue de 1 le nombre de main néssésaire pour l'outil
    """
    self.__main -= 1


