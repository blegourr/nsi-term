import time

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

perfFunction(trie_par_selection(list))




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

perfFunction(tri_par_insertion(list))




"""----------------- ex 2.1 -----------------"""
list2 = ["&é", (20, 5), 5.0,]

def rechercheElement(list, element):
  for val in list:
    if type(val) == type(element) and val == element:
      return True
  return False

# print(rechercheElement(list2, ""))
# print(rechercheElement(list2, "&é"))
# print(rechercheElement(list2, (4, 6)))
# print(rechercheElement(list2, (20, 5)))
# print(rechercheElement(list2, 5.1))


"""----------------- ex 2.2 -----------------"""
list2_2 = [1, 5, 8, 9, 12, 15]

def rechercheElementInDichotomique(list, element):
  found = False
  i_pass = []
  i_pass.append(round((len(list) -1) / 2, 0))
  while  found == False:
    i = i_pass[len(i_pass) - 1]
  
    if (len[i] == element):
      return True
    elif element > len[i]:
      i_pass.append(round(i + (len(list) -1) - (i / 2)))
    else:
      i_pass.append(round(i / 2))



rechercheElementInDichotomique(list2_2, 5)