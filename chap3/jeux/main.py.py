from allClass.personnage_avec_outil import *

genre = input("""
              Saisir la lettre représentant le genre du personnage
                M: Masculin,
                F: Féminin
                A: Autre
              """)

genre = genre.upper()

if genre=='F':
    hero = PerssonageAvecOutil("féminin")
elif genre=='M':
    hero = PerssonageAvecOutil("masculin")
elif genre=='A':
    hero = PerssonageAvecOutil("autre")
else:
    print("erreur de saisie dans le choix du genre")
  
print(f"Votre personnage à comme niveau d'expériance {hero.get_experiance()}")
print(f"Vous commencer avec un bâton de marche de masse {hero.get_objet()[0]} que vous pouvez tenir à {hero.get_objet()[1]} main")

# hero.decouverte(10, 1.32, 2)
hero.decouverte(15, 1.32, 3)

