"""----------------- ex 1 -----------------"""
def decTob(n, b):
  assert(b>1 and b<17)
  signes=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
  mot=""
  while n!=0:
    mot=signes[n%b] + mot
    n = n//b
  return mot

# print(decTob(77, 2))
# print(decTob(77, 8))
# print(decTob(77, 16))

def decToBr(n,b):
  signes=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
  mot=""
  if (n//b == 0):
    mot=signes[n%b] + mot
    n = n//b
    return mot
  else:
    n2 = n//b
    return decToBr(n2, b) + signes[n%b]
  
# print(decToBr(77, 2))
# print(decToBr(77, 8))
# print(decToBr(77, 16))

"""----------------- ex 2 -----------------"""
def bToDec(mot, b):
  assert (b>1 and b<17)
  assert (type(mot) == str)
  signes=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
  result=0
  p=len(mot)
  for i in range(p):
    result=result+signes.index(mot[i])*b**(p-i-1)
  return result

# print(bToDec('1001101', 2))
# print(bToDec('4D', 16))

def bToDecR(mot, b):
    assert (b > 1 and b < 17)
    assert (type(mot) == str)
    signes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    if len(mot) == 1:
        return signes.index(mot)

    return signes.index(mot[0]) * b**(len(mot) - 1) + bToDec(mot[1:], b)

# print(bToDecR('1001101', 2))
# print(bToDecR('4D', 16))

"""----------------- ex 3 -----------------"""
def est_palindrome(mot):
  mot=mot.lower()
  for i in range(len(mot)//2):
    if mot[i]!=mot[-i-1]:
      return False
  return True
  
# print(est_palindrome("test"))
# print(est_palindrome("testtset"))

def est_palindromeR(mot): 
  mot = mot.lower()
  mot = mot.replace(" ", "")
  if len(mot) <= 1:
    return True
  
  if mot[0] != mot[-1]:
    return False
  
  return est_palindrome(mot[1:-1])

# print(est_palindromeR("rad ar"))
# print(est_palindromeR("bonjour"))
# print(est_palindromeR("Level"))

"""----------------- ex 4 -----------------"""
def hanoi(n, depart, arrivee, auxiliaire):
  if n == 1:  # Cas de base : un seul disque à déplacer
    print(f"Déplacer le disque 1 de {depart} à {arrivee}")
  else:
    hanoi(n-1, depart, auxiliaire, arrivee)
    print(f"Déplacer le disque {n} de {depart} à {arrivee}")
    hanoi(n-1, auxiliaire, arrivee, depart)

# hanoi(3, "A", "C", "B")


"""----------------- Final -----------------"""
import turtle as tu

def koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_segment(t, length, level - 1)
        t.left(60)
        koch_segment(t, length, level - 1)
        t.right(120)
        koch_segment(t, length, level - 1)
        t.left(60)
        koch_segment(t, length, level - 1)

t = tu.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.goto(-150, 150)
t.pendown()
t.color("blue")
t.pensize(2)

for _ in range(3): 
    koch_segment(t, 300, 4)
    t.right(120)

tu.done()