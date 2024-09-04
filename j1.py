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
    elif (moyenne >= 16):
        return "très bien"
    

def bissextile(annee):
    if (annee%4 == 0 and annee%100 != 0):
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
    

def entier():
    maxN = 0;
    etape = 0;
    n = int(input("donner un int > 0 : "))
    while (n > 1):
        if (n%2 == 0):
            n = n / 2;
        else:
            n = (n * 3) + 1
        etape += 1
        if (n > maxN):
            maxN=n;
        # print(f"number get : {n}")
    print(f"maxN : {maxN}, etape : {etape}")

    
entier()
