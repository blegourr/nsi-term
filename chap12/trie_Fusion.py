def fusion(T1, T2):
  i1 = 0
  i2 = 0
  T = []

  while i1 < len(T1) and i2 < len(T2):
    if T1[i1] <= T2[i2]:
      T.append(T1[i1])
      i1 += 1
    else:
      T.append(T2[i2])
      i2 += 1

  while i1 < len(T1):
    T.append(T1[i1])
    i1 += 1
  while i2 < len(T2):
    T.append(T2[i2])
    i2 += 1

  return T

print(fusion([3,6,8], [2,5,7,12]))

def triFusion(T):
  if len(T) <= 1:
    return T
  else:
    m = len(T) // 2
    T1 = triFusion(T[:m])
    T2 = triFusion(T[m:])
    return fusion(T1, T2)
  
print(triFusion([3,6,8,2,5,7,12]))
print(triFusion([0,25,36,41,1,465,2,3,987]))