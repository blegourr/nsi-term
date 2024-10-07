"""----------------- ex 1 -----------------"""
class Carte:
    def __init__(self, number, signe):
        self.number = number
        self.signe = signe

"""----------------- ex 2 -----------------"""
class Voiture:
    def __init__(self, couleur, vitesse) -> None:
        self.couleur = couleur
        self.vitesse = vitesse
        self.volume = 0

    def rouler(self):
        print(f"je roule à {self.vitesse}")

    def faire_le_plein(self, volume):
        self.volume = volume

voit_jonathan = Voiture("rouge", 150)
voit_denis = Voiture("bleu", 150)
# print(voit_jonathan.couleur)
# print(voit_denis.couleur)

"""----------------- ex 3 -----------------"""
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def deplace(self, dx, dy):
        self.x += dx
        self.y += dy

    def abscisse(self) -> int:
        return self.x

    
    def ordonnee(self) -> int:
        return self.y

a = Point(2, 4)
print(a)
print(a.abscisse())


"""----------------- ex 4 -----------------"""
class Stock:
    def __init__(self) -> None:
        self.qt_farine = 0
        self.nb_oeufs = 0
        self.qt_beurre = 0
    
    def ajouter_beurre(self, beurre):
        self.qt_beurre += beurre

    def ajouter_farine(self, farine):
        self.qt_farine += farine
    
    def ajouter_oeufs(self, oeufs):
        self.nb_oeufs += oeufs

    def afficher(self):
        print("---------------- Stock ----------------")
        print(f" farine -> {self.ajouter_farine}g")
        print(f" beurre -> {self.ajouter_beurre}g")
        print(f" oeufs -> {self.ajouter_oeufs}")
        print("---------------------------------------")
    
    def stock_suffisant_brioche(self):
        if (self.nb_oeufs >= 4 and self.ajouter_farine >= 350 and self.ajouter_beurre >= 175):
            return True
        else:
            return False
        
mon_stock = Stock()
mon_stock.afficher()
mon_stock.ajouter_beurre(650)
mon_stock.afficher()