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


