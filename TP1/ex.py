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

print(bToDec('1001101', 2))
print(bToDec('4D', 16))

def bToDecR(mot, b):
    assert (b > 1 and b < 17)
    assert (type(mot) == str)
    signes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    if len(mot) == 1:
        return signes.index(mot)

    return signes.index(mot[0]) * b**(len(mot) - 1) + bToDec(mot[1:], b)

print(bToDecR('1001101', 2))
print(bToDecR('4D', 16))

"""----------------- ex 3 -----------------"""

