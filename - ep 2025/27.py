def verifie(tab):
  """
  Vérifie si le tableau est trié dans l'ordre croissant.
  param tab : tableau à vérifier
  return : True si le tableau est trié, False sinon
  """
  if len(tab) == 0:
    return True

  for i in range(len(tab) - 1):
    if tab[i] > tab[i + 1]:
      return False
  return True

print(verifie([0, 5, 8, 8, 9]))
# True
print(verifie([8, 12, 4]))
# False
print(verifie([-1, 4]))
# True
print(verifie([]))
# True
print(verifie([5]))
# True



def depouille(urne):
  '''prend en paramètre une liste de suffrages et renvoie un dictionnaire avec le nombre de voix pour chaque candidat'''
  resultat = {}
  for bulletin in urne:
    if bulletin in resultat:
      resultat[bulletin] = resultat[bulletin] + 1
    else:
      resultat[bulletin] = 1
  return resultat

def vainqueurs(election):
  '''prend en paramètre un dictionnaire non vide avec le nombre de voix pour chaque candidat et renvoie la liste des vainqueurs'''
  nmax = 0
  for candidat in election:
    if election[candidat] > nmax:
      nmax = election[candidat]
  liste_finale = [ nom for nom in election if election[nom] >= nmax ]
  return liste_finale

print(depouille([ 'A', 'B', 'A' ]))
# {'A': 2, 'B': 1}
print(depouille([]))
# {}
election = depouille(['A', 'A', 'A', 'B', 'C','B', 'C', 'B', 'C', 'B'])
print(election)
# {'A': 3, 'B': 4, 'C': 3}
print(vainqueurs(election))
# ['B']
print(vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}))
# ['A', 'B']