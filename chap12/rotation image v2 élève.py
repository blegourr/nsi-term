# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:58:17 2022

@author: mperenno
"""
from PIL import Image


def echangePixel(image,x1,y1,x2,y2):
    """
    Echange les pixels d'une image entre une 
    position de départ et une position d'arrivée

    Parameters
    ----------
    image : instance de la classe Image 
    x1 y1 : coordonnées du pixel de départ
	x2 y2 : coordonnées du pixel d'arrivée
    Returns : None
    """
    pixel1=image.getpixel((x1,y1))
    pixel2=image.getpixel((x2,y2))
    #A compléter

    
def echangecarre(image,x1,y1,x2,y2,n):
    """
	Échange les pixels entre les deux quadrants de taille n
	définis par leur coin haut gauche.
	x1 y1 : coordonnées du coin supérieur gauche du quadrant a
	x2 y2 : coordonnées du coin supérieur gauche du quadrant b
	n : taille des deux quadrants
	"""
    for i in range(n):
        for j in range(n):
            echangePixel(image,#A compléter

def tourneCarre(image,x,y,n):
    """
	Applique une rotation du quadrant de l'image défini par
	son coin supérieur gauche et sa taille.
	x,y: coordonnées du coin supérieur gauche du quadrant
	n : taille du quadrant à faire tourner
    """
    if n>=2:
        m=n//2
        tourneCarre(image,x,y,m)
        tourneCarre(image,x,y+m,m)
        tourneCarre(image,x+m,y ,m)
        tourneCarre(image,x+m,y+m, m)
             
        echangecarre(image,x,y,x+m,y,m)       
        #A compléter
        


def rotation(image):
    """
	Lance la fonction récursive sur l'image originale.
    """
    assert image.size[0] == image.size[1]
    #fonction    
    tourneCarre(image,0,0,image.size[0])
    image.save("Apres_rotation.png")
    
img=Image.open("hokusai_512x512.png")
img.show()   
# Lance le programme
rotation(img)
# Affiche l'image
img.show()