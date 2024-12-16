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
    mot= decToBr(n2, b) + signes[n%b]
    return mot
  
# print(decToBr(77, 2))
# print(decToBr(77, 8))
# print(decToBr(77, 16))

"""----------------- ex 2 -----------------"""
