class Cellule:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

    def __str__(self):
        if self.suivant is None:
            return str(self.valeur) + " -> None"
        return str(self.valeur) + " -> " + str(self.suivant)


class ListeC:
    def __init__(self):
        self.tete = None

    def __str__(self):
        return str(self.tete)

    def est_vide(self):
        return self.tete is None

    def tailleListe(self):
        l = 0
        courant = self.tete
        while courant:
            l += 1
            courant = courant.suivant
        return l

    def get_maillon_indice(self, i):
        courant = self.tete
        j = 0
        while courant and j < i:
            courant = courant.suivant
            j += 1
        return courant if j == i else None

    def ajouter_debut(self, nM):
        nM.suivant = self.tete
        self.tete = nM

    def ajouter_fin(self, nM):
        if self.est_vide():
            self.tete = nM
        else:
            courant = self.tete
            while courant.suivant:
                courant = courant.suivant
            courant.suivant = nM

    def supprimer_fin(self):
        if self.est_vide():
            return None
        if self.tete.suivant is None:
            dernier = self.tete
            self.tete = None
            return dernier
        courant = self.tete
        while courant.suivant.suivant:
            courant = courant.suivant
        dernier = courant.suivant
        courant.suivant = None
        return dernier

    def inserer(self, M, nM):
        if M is None:
            return
        nM.suivant = M.suivant
        M.suivant = nM


# Example usage:
L = ListeC()
M1, M2 = Cellule(21), Cellule(15)
M1.suivant = M2
L.tete = M1
print(L)  # 21 -> 15 -> None

print(L.tailleListe())  # Output: 2
print(L.get_maillon_indice(1))  # Output: 15 -> None

M3 = Cellule(45)
L.ajouter_fin(M3)
print(L)  # 21 -> 15 -> 45 -> None

M4 = Cellule(37)
L.inserer(M1, M4)
print(L)  # 21 -> 37 -> 15 -> 45 -> None
