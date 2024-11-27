"""----------------- ex 1 -----------------"""

class Tableau:
  def __init__(self, default=[]) -> None:
    self.tab = default

  def longueur(self):
    return len(self.tab)

  def est_vide(self):
    return self.tab == []

  def ajout(self, index, value):
    self.tab.insert(index, value)

  def data(self):
    return self.tab

  def suppr(self, index):
    self.tab.pop(index)


"""----------------- ex 3 -----------------"""
"""
  data:
    copainsName:
      serieName: [""]
      age: int
      taille: int
"""
# class Copains:
#   def __init__(self, defaultCopain={}) -> None:
#     self.copains = defaultCopain

#   def add(self, name, age, taille, serie=[]):
#     self.copains[name] = Copain(age, taille, serie)

#   def get(self, name):
#     return self.copains[name]

#   def delete(self, name):
#     self.copains[name] = None

# class Copain:
#   def __init__(self, age, taille, serie=[]) -> None:
#     self.age = age
#     self.taille = taille
#     self.serie=serie

# copains = Copains()
# copains.add("bertrant", 16, 1.80, ["pirates"])
# print(copains.copains)
# print(copains.get("bertrant").age)

copains_data = {}

def add_copain(name, age, taille, serie=[]):
    copains_data[name] = {
        "age": age,
        "taille": taille,
        "serieName": serie
    }

def get_copain(name):
    return copains_data.get(name)

def delete_copain(name):
    copains_data.pop(name, None)

add_copain("bertrant", 16, 1.80, ["pirates"])
print(copains_data)
print(get_copain("bertrant")["age"])