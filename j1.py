import random

def expo(n):
    value = 2
    for i in range(n):
        value = value*2      
    return value;

# print(expo(5))

def passage(moyenne):
    if (moyenne < 8):
        return "RECALE"
    elif (8 <= moyenne and moyenne < 10):
        return "Oral rattrappage"
    elif (10 <= moyenne and moyenne < 12):
        return "admis"
    elif (12 <= moyenne and moyenne < 14):
        return "ASSEZ BIEN"
    elif (14 <= moyenne and moyenne < 16):
        return "bien"
    else:
        return "très bien"
    
def bissextile(annee):
    if (annee%4 == 0 and (annee%100 != 0 or annee%400 == 0)):
        return True;
    return False;

# print(bissextile(2096));
# print(bissextile(2092));
# print(bissextile(2088));
# print(bissextile(2089));

def nbJoursAnnee(annee):
    if (bissextile(annee)):
        return 365;        
    else :
        return 364;

def nbJourMois(annee, mois):
    if (mois == 1): 
        return 31;
    elif (mois == 2): 
        if (bissextile(annee)):
            return 29;
        else:
            return 28;
    elif (mois == 3): 
        return 31;
    elif (mois == 4): 
        return 30;
    elif (mois == 5): 
        return 31;
    elif (mois == 6): 
        return 30;
    elif (mois == 7): 
        return 31;
    elif (mois == 8): 
        return 31;
    elif (mois == 9): 
        return 30;
    elif (mois == 10): 
        return 31;
    elif (mois == 11): 
        return 30;
    else: 
        return 31; 
    

def entier(n):
    startN = n
    maxN = 0;
    etape = 0;
    while (n > 1):
        if (n%2 == 0):
            n = n / 2;
        else:
            n = (n * 3) + 1
        etape += 1
        if (n > maxN):
            maxN=n;
        # print(f"number get : {n}")
    # print(f"Pour n = {startN} => maxN : {maxN}, etape : {etape}")

for i in range(1, 21):
    entier(i)

# ex 6

list = [1**3, 2**3, 3**3, 4**3]
listRandom = []
for i in range(100):
    listRandom.append(random.randrange(1, 1000))

listRandomImpaire = [val for val in listRandom if val%2 != 0]
# print(listRandomImpaire)

# ex 7
def somme(list):
    sommeTotal = 0
    for element in list:
        sommeTotal += element
        # print(element)
    return sommeTotal

somme(listRandomImpaire)

# ex 8
def max(list):
    max = 0;
    for element in list:
        if (element > max):
            max = element
    return max


# ex 9 

def mini(list):
    min = 1000;
    for element in list:
        if (element< min):
            min = element
    return min

def min2(list):
    min = 1000;
    index = 0;
    for i in range(len(list)):
        if (list[i] < min):
            min = list[i]
            index = i
    return index;

def min3(list):
    min = 1000;
    for element in list:
        if (element< min):
            min = element

    listOfIndex = []
    for i in range(len(list)):
        if (list[i] == min):
            listOfIndex.append(i);    
            
    return listOfIndex;

print(min3(listRandom));

# ex 10 
