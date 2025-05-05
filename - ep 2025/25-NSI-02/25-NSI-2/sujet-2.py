def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab) #longeur de la liste
    # les entiers vus lors du parcours
    vus = []

    for x in tab:
        if x < 1 or x > n or x in vus: #si la valeur est superieur ou inférieur a la liste ou ceux ayants été déjà vu
            return False # retourner faux
        vus.append(x) # ajouter la valeur x a la tab
    return True # retourner vrai

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre)
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n-1:
        if ordre[i]-ordre[i+1] not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[i] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb

print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))
# 4
print(nombre_points_rupture([1, 2, 3, 4, 5]))
# 0
print(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]))
# 7

# def max_et_indice(tab): # fonction 
#   max = tab[0] # premier élément de la liste
#   p_max = 0 # compteur à 0
#   for i in range(1,len(tab)): # pour elt dans longeur de tab 
#     if tab[i] > max: # si i est supérueur a max 
#       max = tab[i] # je remplace le nouveux max par i
#       p_max = i
#   return (max,p_max)
 