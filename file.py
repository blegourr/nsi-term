def calcul(n):
    suite=[]
    suite.append(n)
    while n!=1:
        if n%2==0:
            n=n/2
            suite.append(n)
        else:
            n=(n*3)+1
            suite.append(n)
    return suite

print(calcul(7))


def rebours(n):
    if n < 0:
        return print("Partez !")
    print(n)
    rebours(n - 1)

# Exemple d'utilisation
rebours(3)