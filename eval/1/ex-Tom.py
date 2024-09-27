def moyenne(tab):
    # Calcul de la somme des éléments du tableau, puis division par le nombre d'éléments
    return sum(tab) / len(tab)

# Assertions fournies dans l'énoncé pour tester la fonction
assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5

print("Toutes les assertions sont correctes.")
