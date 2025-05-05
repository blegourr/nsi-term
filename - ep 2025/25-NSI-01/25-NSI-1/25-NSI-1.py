def nombre_suivant(s):
  '''Renvoie le nombre suivant de celui representé par s
  en appliquant le procédé de lecture.'''
  resultat = '' #pouvoir retourner le résultat
  chiffre = s[0] #renvoi le premier caratère 
  compte = 1 # instancier a 1 compteur 
  for i in range(1, len(s)): # boucle qui parcour la longeur de s
    if s[i] == chiffre: #si l'indice est strictement égale a la chine de caractère
      compte += 1 
    else:
      resultat += str(compte) + chiffre 
      chiffre = s[i]
      compte = 1
  lecture_chiffre = str(compte) + chiffre 
  resultat += lecture_chiffre
  return resultat

print(nombre_suivant('1211'))


# def voisins_entrants(adj,x):
#   lst=[]
#   for i in range(len(adj)):
#     n=adj[i]
#     for j in range(len(n)):
#       if x ==n[j]:
#         lst.append(i)
#   return lst

# print (voisins_entrants([[1, 2], [2], [0], [0]], 0))