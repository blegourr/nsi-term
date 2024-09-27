import doctest
import os

"""----------------- ex 1 -----------------"""
def inverse(n):
  assert  n!=0
  assert n > 0
  assert isinstance(n, int)

  return 1/n

# inverse(0)
# inverse(-2)
# inverse(1.2)
# inverse(10)

"""----------------- ex 2 -----------------"""
def minimumList(lst):
  assert isinstance(lst, list)
  assert len(lst) >= 2
  longeur = len(lst)
  mini=lst[0]
  i = 1
  while (i<longeur):
    if (lst[i]<mini):
      mini = lst[i]
    i+=1
  return mini

"""----------------- ex 3 -----------------"""
def afficherInverse(lst):
  # assert len ([ element for element in lst if isinstance(element) != int ]) > 0:
  # print("all element in list are not an number")
  for x in lst:
    try :
      if x == 0:
        raise ZeroDivisionError
      if not (isinstance(x, int) or isinstance(x, float)):
        raise TypeError
      print(x, end=" , ")
      print(1.0/x)
    except ZeroDivisionError:
      print("division by 0")
    except TypeError:
      print(f"x: {x} is not an int or float")
    
# list=[5, 5.5, "fds"]
# afficherInverse(list)

"""----------------- ex 4 -----------------"""
# f = open("test.tkt", "r")

def ouvertureFichierLecture(nameFile):
  f=None;error=""
  if os.path.exists(nameFile): f = open(nameFile)
  else: error = "file not found"
  return (f, error)

# print(ouvertureFichierLecture("test.tkt"))

"""----------------- ex 5 -----------------"""
def division(n1, n2):
  quotient = n1/n2 # retirer la divisions // et observer le résultat
  rest= n1%n2
  return quotient, rest

# print(division(4, 5))


"""----------------- ex 6 -----------------"""

def insert(t, i, v):
  j = i
  while j > 0 and t[j-1]> v:
    t[j] = t[j-1]
    j -= 1
  t[j] = v
  return t

def tri_par_insertion(t):
  """
    fonction pour trier par insertions

  test unitaires
  # >>> tri_par_insertion([12, 8, 2.4, 56])

  # >>> tri_par_insertion([12, 8, 2.4, "aa"])

  >>> tri_par_insertion([12, 8, 24, 56])
  [8, 12, 24, 56]
  """
  # trie le tableau dans l'ordre croissant
  for i in range(1, len(t)):
    t = insert(t, i, t[i])
  return t

doctest.testmod()