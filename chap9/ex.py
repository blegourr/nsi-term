from AB import ArbreBinaire,affiche,afficher_parcours_suffixe;


"""----------------- ex 2 -----------------"""
ng = ArbreBinaire(9)
nd = ArbreBinaire(4)
ng = ArbreBinaire(1, ng, nd)
nd = ArbreBinaire(12)
nd = ArbreBinaire(6, ng, nd)
ngd = ArbreBinaire(3)
ng = ArbreBinaire(10, droit=ngd)
arbre = ArbreBinaire(5, ng, nd)

# print(arbre.taille())
print(affiche(arbre))
print(arbre.parcours_infixe())
print(arbre.parcours_prefix())
print(arbre.parcours_suffixe())
print(afficher_parcours_suffixe(arbre))