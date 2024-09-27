# ------------------------------
#            FUNCTION
# ------------------------------
def indice_du_min(tab:list) -> int: # initialisation de la function
  min = None
  for value in tab: 
    if min == None or (value < min): # si valeur min non définie ou value < min définie le nouveau min
      min = value
  
  for i in range(len(tab)): # récupère la première value du tab avec la valeur min (ou inférieur)
    if (tab[i] <= min): return i # renvoie l'index min
# ------------------------------
#               TEST
# ------------------------------
print(indice_du_min([5])) # -> 0
print(indice_du_min([2,4,1])) # -> 2
print(indice_du_min([5, 3, 2, 2, 4])) # -> 2