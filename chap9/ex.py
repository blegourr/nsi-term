from AB import ArbreBinaire;


"""----------------- ex 2 -----------------"""
ng = ArbreBinaire(9)
nd = ArbreBinaire(4)
ng = ArbreBinaire(1, ng, nd)
nd = ArbreBinaire(12)
nd = ArbreBinaire(6, ng, nd)
ngd = ArbreBinaire(3)
ng = ArbreBinaire(10, droit=ngd)
arbre = ArbreBinaire(5, ng, nd)