def moyenne(tab):
    """
    Calcule la moyenne des éléments d'une liste.
    
    param tab : Liste de nombres
    return : La moyenne des éléments de la liste
    """
    if not tab:
        return 0
    
    sum = 0
    for i in range(len(tab)):
        sum += tab[i]

    return  sum / len(tab)
 
print(moyenne([1.0]))
# 1.0
print(moyenne([1.0, 2.0, 4.0]))
# 2.3333333333333335

def binaire(a):
  '''convertit un nombre entier a en sa representation
  binaire sous forme de chaine de caractères.'''
  if a == 0:
    return '0'
  bin_a = ''
  while a > 0:
      bin_a = str(a % 2) + bin_a
      a = a // 2
  return bin_a

print(binaire(83))
# '1010011'
print(binaire(6))
# '110'
print(binaire(127))
# '1111111'
print(binaire(0))
# '0'