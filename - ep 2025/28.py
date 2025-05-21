def a_doublon(tab):
  """
  Vérifie si le tableau trié par ordre croissant contient au moins un doublon.
  param tab : tableau à vérifier
  return : True si le tableau contient au moins un doublon, False sinon
  """
  if len(tab) == 0:
    return False

  for i in range(len(tab) - 1):
    if tab[i] == tab[i + 1]:
      return True
  return False

print(a_doublon([]))
# False
print(a_doublon([1]))
# False
print(a_doublon([1, 2, 4, 6, 6]))
# True
print(a_doublon([2, 5, 7, 7, 7, 9]))
# True
print(a_doublon([0, 2, 3]))
# False

def voisinage(n, ligne, colonne):
  """ Renvoie la liste des coordonnées des voisins de la case
  (ligne, colonne) dans un grille de taille n x n,
  en tenant compte des cases sur les bords. """
  voisins = []
  for dl in range(-1, 2):
    for dc in range(-1, 2):
      l = ligne + dl
      c = colonne + dc
      if (l, c) != (ligne, colonne) and 0 <= l < n and 0 <= c < n:
        voisins.append((l,c))
  return voisins



def incremente_voisins(grille, ligne, colonne):
  """ Incrémente de 1 toutes les cases voisines d'une bombe."""
  voisins = voisinage(len(grille), ligne, colonne)
  for l, c in voisins:
    if grille[l][c] != -1: # si ce n'est pas une bombe
      grille[l][c] += 1 # on ajoute 1 à sa valeur


def genere_grille(bombes):
  """ Renvoie une grille de démineur de taille nxn où n est
  le nombre de bombes, en plaçant les bombes à l'aide de
  la liste bombes de coordonnées (tuples) passée en
  paramètre. """
  n = len(bombes)
  # Initialisation d'une grille nxn remplie de 0
  grille = [[0 for colonne in range(n)] for ligne in range(n)]
  # Place les bombes et calcule les valeurs des autres cases
  for ligne, colonne in bombes:
    grille[ligne][colonne] = -1 # place la bombe 
    incremente_voisins(grille, ligne, colonne)
  return grille

print(genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]))
