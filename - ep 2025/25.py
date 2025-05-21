t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]


def annee_temperature_minimale(temps, year):
    temp_min = temps[0]
    index = 0
    for i in range(1, len(temps)):
        if temps[i] < temp_min:
            temp_min = temps[i]
            index = i
            
    return (temp_min, year[index])

# print(annee_temperature_minimale(t_moy, annees))


def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre
    est un palindrome'''
    chaine = str(nbre)
    return est_palindrome(chaine)


print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))
