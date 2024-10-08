import time, math

"""----------------- ex 1 -----------------"""
""" function """
def perfFunction(function):
    # save time before funciton
    start = time.perf_counter()

    # exectute the function
    function

    # save time after function
    end = time.perf_counter()

    # print difference of time
    print(f"time : {(end-start)*1000}ms")

""" Algo 1 """
list = [2, 6, 3, 9, 7]
# trie par sélection 
def echange(t, i, j):
  tmp = t[i]
  t[i] = t[j]
  t[j] = tmp
  return t

def trie_par_selection(t):
  # trie par sélection dans l'ordre croissant
  for i in range(len(t)):
    # print(f"i1 : {i}")
    m=i
    for j in range(i+1, len(t)):
      # print(f"j1 : {j}")
      if t[j] < t[m]:
        m=j
    # print(f"m1 : {m}")
    t = echange(t, i, m)
  return t

# perfFunction(trie_par_selection(list))

""" Algo 2 """
def insert(t, i, v):
  j = i
  while j > 0 and t[j-1]> v:
    t[j] = t[j-1]
    j -= 1
  t[j] = v
  return t

def tri_par_insertion(t):
  # trie le tableau dans l'ordre croissant
  for i in range(1, len(t)):
    t = insert(t, i, t[i])
  return t

# perfFunction(tri_par_insertion(list))




"""----------------- ex 2.1 -----------------"""
list2 = ["&é", (20, 5), 5.0,]

def rechercheElement(list, element):
  step=0
  for val in list:
    step += 1
    if type(val) == type(element) and val == element:
      print(f"step : {step}")
      return True
  # if (element in list): return True
  print(f"step : {step}")
  return False

# print(rechercheElement(list2, ""))
# print(rechercheElement(list2, "&é"))
# print(rechercheElement(list2, (4, 6)))
# print(rechercheElement(list2, (20, 5)))
# print(rechercheElement(list2, 5.1))


"""----------------- ex 2.2 and 2.3 -----------------"""
list2_2 = [1, 5, 8, 9, 12, 15, 19, 20, 25, 36, 88, 120] # len == 12

def rechercheElementInDichotomique(list, element):
  step=0
  found = False
  i_pass = []
  i_pass.append(int(round((len(list) -1) / 2, 0)))
  while  found == False:
    step += 1
    i = int(i_pass[len(i_pass) - 1])

    if (i < 0 or i >= len(list)):
      print(f"step : {step}")
      return False;

    if (list[i] == element):
      print(f"step : {step}")
      return True
    
    elif element > list[i]:
      if ((len(list)-(i+1))/2 < 1 and (len(list)-(i+1))/2 > 0):
        iAddPass = i+1

      else:
        iAddPass = int(round((len(list)-(i+1))/2 + i , 0))

      if (iAddPass in i_pass): 
        print(f"step : {step}")
        return False

      i_pass.append(iAddPass)

    else:
      iAddPass = int(round(i / 2, 0))
      if (iAddPass in i_pass): 
        print(f"step : {step}")
        return False

      i_pass.append(iAddPass)

# print(rechercheElementInDichotomique(list2_2, 4))

"""----------------- ex 2.3 -----------------"""
list0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# rechercheElement(list0, 1)
# rechercheElementInDichotomique(list0, 1)



"""----------------- ex 3 -----------------"""
system=[0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]
somme = 549

def moneyRendue(system, somme):
  somme_restante = somme
  money = []

  while somme_restante > 0:
    # get the max value in money < somme_restant
    for i in range(len(system)):
      if (somme_restante >= system[len(system) - (i+1)]):
        somme_restante -= system[len(system) - (i+1)]
        money.append(system[len(system) - (i+1)])
        break

  return money

print(moneyRendue(system, somme))

"""----------------- ex 4 -----------------"""
c = [["c1", 1,1], ["c1", 1,2], ["c1", 1,4], ["c1", 2,1], ["c1", 3,1], ["c1", 3,3], ["c1", 3,4], ["c2", 4,1], ["c2", 4,2], ["c2", 4,4], ["c2", 5,1], ["c2", 6,2], ["c2", 7,2], ["c2", 7,3]]
m = [4,5]

def distanceM(c, m):
  xA_distance = m[0]
  yA_distance = m[1]

  for (i, val) in enumerate(c):
    xB_distance = val[1]
    yB_distance = val[2]
    distance = math.sqrt((xB_distance-xA_distance)**2 + (yB_distance-yA_distance)**2)
    c[i].append(distance)
  
  return c

c = distanceM(c, m)


# trie par sélection 
def echangeEx4(t, i, j):
  tmp = t[i]
  t[i] = t[j]
  t[j] = tmp
  return t

def trie_par_selectionEx4(t):
  # trie par sélection dans l'ordre croissant
  for i in range(len(c)):
    # print(f"i1 : {i}")
    m=i
    for j in range(i+1, len(t)):
      # print(f"j1 : {j}")
      if t[j][3] < t[m][3]:
        m=j
    # print(f"m1 : {m}")
    t = echangeEx4(t, i, m)
  return t

c = trie_par_selectionEx4(c)


def plusProche(k, c):
  kProche = []
  for i in range(k):
    kProche.append(c[i])
  return kProche

c = plusProche(5, c)

def nombreDoccurence(c):
  c1 = 0
  c2 = 0
  for i in range(len(c)):
    if c[i][0] == "c1":
      c1 += 1
    else:
      c2 += 1

  return [c1,c2]

occurence = nombreDoccurence(c)
if (occurence[0] > occurence [1]):
  m[3] = "c1"
else:
  m[3] = "c2"