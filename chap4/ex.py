from interface import Pile


"""----------------- ex 3 -----------------"""
parenthese=Pile()

char = "fdui(fndjks)fdnjkéfndso(fndsndoef (fdsjif (buif (bidfsfnois efef)))) fdsdfsdf)fdf nf(fnd isfodjo)"

for i in range (len(char)):
    if char[i]=="(":
        parenthese.empiler(i)
    if char[i]==")" and not parenthese.vide():
        parenthese.depiler()

if not parenthese.vide():
    raise ValueError("Nombre de parenthèse incorecte")

print("nombre de parenthèse correcte")