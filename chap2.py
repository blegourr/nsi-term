"""----------------- ex 1 -----------------"""
# import math; help(math);
# import turtle; help(turtle);
# import tkinter; help(tkinter);
# import timeit; help(timeit);


"""----------------- ex 2 -----------------"""
# import math
# help(math.pi())
# help(math.remainder)
# help(math.factorial)
# help(math.gcd)


"""----------------- ex 3 -----------------"""
# import turtle
# print(turtle.__file__)
# print(turtle.__doc__)

"""----------------- ex 4 -----------------"""
# import numpy
# print(numpy.__file__)
# print(numpy.__doc__)

"""----------------- ex 5 -----------------"""


# def est_impair(a):
#     """
#     la fonction prends un int en paramètre et renvoie 
#     - True si impaire
#     - False si paire 
#     """
#     assert type(a) == int;
#     if a%2 != 0: return True;
#     return False;

# est_impair(4)


"""----------------- ex 6 -----------------"""
"""
>>> help(aires)
Help on module aires :

NAME
    aires

DESCRIPTION
    Fourniture de fonctions calculant les surfaces de diverse figures géométrique

FUNCTIONS
    disque(rayon: float) -> float
        Renvoie l'air d'un disque de rayon r

    rectangle(largeur: float, longueur: float) -> float
        Renvoie l'air d'un retangle de côtés largeur et longueur.

    triangle(base: float, hauteur: float) -> float
        renvoie l'air d'un triangle de base base et de hauteur hauteur.

DATA
    pi = 3.14159

FILE
    /aires.py
"""
import math
import doctest

def disque(rayon):
    """
    disque(rayon: float) -> float
        Renvoie l'air d'un disque de rayon r
    >>> disque(123.0)
    772.8317927830891
    """
    assert type(rayon) == float;
    return 2*math.pi*rayon

def rectangle(largeur, longueur):
    """
     rectangle(largeur: float, longueur: float) -> float
        Renvoie l'air d'un retangle de côtés largeur et longueur.
    >>> rectangle(5.0, 2.0)
    10.0

    """
    assert type(largeur) == float;
    assert type(longueur) == float;
    return largeur*longueur

def triangle(base, hauteur):
    """
    triangle(base: float, hauteur: float) -> float
        renvoie l'air d'un triangle de base base et de hauteur hauteur.
    triangle(4.0, 2.0)
    4.0

    """
    assert type(base) == float;
    assert type(hauteur) == float;
    return (base*hauteur)/2


doctest.testmod()