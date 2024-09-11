# init
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


# print(trie_par_selection(list))

# trie par insertion

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

# print(tri_par_insertion(list))


"""with python function"""
# print(sorted(list))
# list.sort()
# print(list)

