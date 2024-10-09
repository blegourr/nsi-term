from allClass.Outil import *
from random import *

class PerssonageAvecOutil:
  """
    class pour gérer les personnages        
  """
  def __init__(self, genre:str, experiance:int=0):
    """
      initialistations d'un personnage lors de la création
    """
    if (not (genre == "féminin" or genre == "masculin" or genre == "autre")): return {
      "Error": True,
      "Message": "genre need = to \"féminin\" ou \"masculin\" ou \"autre\""
    }
    self.genre = genre
    self.__experiance = experiance
    self.object = Outil(0,0.5)
    
  def get_experiance(self):
    """
      renvoie l'éxpériance actuelle du personnage
    """
    return self.__experiance

  def __set_experiance(self, experriance:int):
    """
      update l'expériance du personnage
    """
    self.__experiance = experriance
  
  def rencontre(self):
    """
      crée une rencontre se qui rajoute un nombre entre 10 et 20 à l'éxpériance du personnage
    """
    n = randint(10,20)
    self.__set_experiance(self.get_experiance()+n)

  def decouverte(self, experiance:int, masse:int, main:int):
    if (self.get_experiance() >= experiance):
      self.object = Outil(experiance, masse, main)
      print("Nouvel object")
    else:
      print("Dommage il faut encore progresser")
    
      

    

  def get_objet(self):
    """
      renvoie la masse et le nombre de main de l'objet -> (masse, main)
    """
    masse = self.object.get_masse()
    main = self.object.get_main()
    return masse,main