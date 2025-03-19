from PIL import Image

def echangePixel(image, x1, y1, x2, y2):
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
  pixel1 = image.getpixel((x1, y1))
  pixel2 = image.getpixel((x2, y2))
  image.putpixel((x1, y1), pixel2)
  image.putpixel((x2, y2), pixel1)

  return None

def echangecarre(image, x1, y1, x2, y2, n):
  """
  Échange les pixels entre les deux quadrants de taille n
  définis par leur coin haut gauche.
  x1 y1 : coordonnées du coin supérieur gauche du quadrant a
  x2 y2 : coordonnées du coin supérieur gauche du quadrant b
  n : taille des deux quadrants
  """
  for i in range(n):
    for j in range(n):
      echangePixel(image, x1 + i, y1 + j, x2 + i, y2 + j)

def tourneCarre(image, x, y, n):
  """
  Applique une rotation du quadrant de l'image défini par
  son coin supérieur gauche et sa taille.
  x : coordonnées du coin supérieur gauche du quadrant
  y : coordonnées du coin supérieur gauche du quadrant
  n : taille du quadrant à faire tourner
  tourne l'image de 90° dans le sens des aiguilles d'une montre
  """
  if n >= 2:
    m = n // 2
    tourneCarre(image,x,y,m)
    tourneCarre(image,x,y+m,m)
    tourneCarre(image,x+m,y ,m)
    tourneCarre(image,x+m,y+m, m)

    echangecarre(image,x,y,x+m,y,m)       
    echangecarre(image,x,y+m,x+m,y+m,m)
    echangecarre(image,x+m,y,x,y+m,m)
    echangecarre(image,x+m,y+m,x,y,m)

def rotation(image):
  """
  Lance la fonction récursive sur l'image originale.
  """
  assert image.size[0] == image.size[1]
  # fonction    
  tourneCarre(image, 0, 0, image.size[0])
  image.save("C:/Users/legou/Documents/dev/nsi-term/chap12/Apres_rotation.png")

img=Image.open("C:/Users/legou/Documents/dev/nsi-term/chap12/hokusai_512x512.png")
# img = Image.open("C:/Users/legou/Documents/dev/nsi-term/chap12/A-80x80.png")
# img.show()   
# Lance le programme
rotation(img)
# Affiche l'image
# img.show()
