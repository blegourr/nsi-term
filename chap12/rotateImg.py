from PIL import Image

def echangePixel(image, x1, y1, x2, y2):
  """
  Échange les pixels entre (x1, y1) et (x2, y2) dans l'image.python -m pip install --upgrade SomePackage

  """
  pixel1 = image.getpixel((x1, y1))
  pixel2 = image.getpixel((x2, y2))
  image.putpixel((x1, y1), pixel2)
  image.putpixel((x2, y2), pixel1)

def echangecarre(image, x1, y1, x2, y2, n):
  """
  Échange deux quadrants de taille n dans l'image,
  définis par leurs coins supérieurs gauches (x1,y1) et (x2,y2).
  """
  for i in range(n):
    for j in range(n):
      echangePixel(image, x1 + i, y1 + j, x2 + i, y2 + j)

def tourneCarre(image, x, y, n):
  """
  Effectue une rotation de 90° dans le sens des aiguilles d'une montre
  sur le quadrant de taille n défini par son coin supérieur gauche (x,y).
  La rotation est appliquée récursivement sur chaque sous-quadrant.
  """
  if n >= 2:
    m = n // 2
    # Appliquer la rotation récursive sur chaque quadrant
    tourneCarre(image, x, y, m)
    tourneCarre(image, x, y + m, m)
    tourneCarre(image, x + m, y, m)
    tourneCarre(image, x + m, y + m, m)
    
    # 1. Échange quadrant A (x,y) avec quadrant B
    echangecarre(image, x, y, x+m, y, m)
    # 2. Échange quadrant B avec quadrant D
    echangecarre(image, x, y, x + m, y + m, m)
    # 3. Échange quadrant D avec quadrant C
    echangecarre(image, x, y, x, y + m, m)

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
