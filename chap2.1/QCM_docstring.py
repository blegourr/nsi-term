import os
"""
Structure de QCM:

QCM = [
  [question_1, question_2, question_3, question_4, ...],
  [question_1_response_1, question_2_response_1, question_3_response_1, question_4_response_1, ...],
  [question_1_response_2, question_2_response_2, question_3_response_2, question_4_response_2, ...],
  [question_1_response_3, question_2_response_3, question_3_response_3, question_4_response_3, ...]
]
"""
def creer_tableaurep(QCM:list)->list:
    '''
    permet de créer un tableau ou seront stockées les réponses données 
    par l'utilisateur (1, 2 ou 3 pour chaque question)
    le tableau renvoyé a pour longueur le nombre de questions du QCM soit len(QCM[0]) 	
    
    
    -----------------------
            EXEMPLE 
    -----------------------
    Params :
        QCM = [
            ["\"test\"+\"test\"", "\"test\"+\"test2\""],
            ["test", "test2"],
            ["test test", "test test2"],
            ["testtest*", "testtest2*"]
        ]

    ---------------------------------------------------------
    Return :
        tabRep = [0, 0] 
    '''
    return [0] * len(QCM[0])  # len(QCM[0]) permet de récupérer le nombre de question, [0] * nrbQuestion permet de crée un tableau de taille égale au nombre de question et d'élément uniquement de 0 


def affichageQCM(QCM:list, i:int):
    '''
    permet d'afficher la question n°i du QCM contenue dans le tableau QCM.
    les réponses sont ensuite proposées
    l'étoile indiquant la bonne réponse est supprimée lors de l'affichage

    -----------------------
            EXEMPLE 
    -----------------------
    Params :
        QCM = [
            ["\"test\"+\"test\"", "\"test\"+\"test2\""],
            ["test", "test2"],
            ["test test", "test test2"],
            ["testtest*", "testtest2*"]
        ]

        i = 1

    ---------------------------------------------------------
    Print :
        Question 2: "test"+"test2"
        1. test2
        2. test test2
        3. testtest2
    '''
    question = QCM[0][i]  # Récupère la question présentes sur la première ligne de QCM via son index.
    reponses = [QCM[j][i].replace('*', '') for j in range(1, 4)]  # Récupère les réponse sur les lignes 1 à 3 via l'index. Et supprime * permettant de marqué la bonne réponse
    print(f"Question {i+1}: {question}") # affiche la question.
    for j, rep in enumerate(reponses, start=1): # récupère l'index (variable : j), et la réponse ( variable rep) : la boucle commence avec l'index 1 via le enumerate(list, start = 1)
        print(f"{j}. {rep}") # affiche les réponses pour la question.


def score(QCM:list, rep:list)->list:
    '''
    calcule le score à chaque question (0 ou 1) en vérifiant si la réponse est 
    bonne dans les tableaux de réponse grâce au caractère *. Le tableau renvoyé 
    ne contient donc que des 0 ou des 1
    '''
    scores = [] # init d'un tableau vide pour y stock les valeurs
    for i in range(len(QCM[0])):  # Parcourt des questions
        bonnes_reponses = [j for j in range(1, 4) if '*' in QCM[j][i]]  # Repères la bonne réponse via * mis dans la réponse valide
        if (rep[i] - 1) in [br - 1 for br in bonnes_reponses]:  # On ajuste l'indice de la réponse de l'utilisateur
            scores.append(1)  # Réponse correcte set à 1
        else:
            scores.append(0)  # Réponse incorrecte set à 0
    return scores # renvoie le score


def total(tab_score:list)->tuple:
    '''
    renvoie un tuple contenant le score total et le nombre de questions du 
    type (7,10) quand le score est de 7/10
    '''
    score_total = sum(tab_score)
    nb_questions = len(tab_score)
    return (score_total, nb_questions)


def affiche_resultat(tab_total:tuple):
    '''
    affiche le résultat de l’utilisateur à partir d'un tableau à deux cases 
    contenant le score de l'utilisateur et le nombre de questions
    '''
    print("-----------------------------------------")
    print("                  SCORE                  ")
    print("-----------------------------------------")
    score, nb_questions = tab_total
    print(f"Votre score est de {score}/{nb_questions}.")


def affichage_bonne_rep(QCM:list, i:int):
    '''
    permet d'afficher la question n°i du QCM contenue dans le tableau QCM 
    puis uniquement la réponse correcte
    '''
    question = QCM[0][i]
    bonne_rep = [QCM[j][i].replace('*', '') for j in range(1, 4) if '*' in QCM[j][i]][0]  # Repérer la bonne réponse
    print(f"Question {i+1}: {question}")
    print(f"La bonne réponse est : {bonne_rep}")


def passageQCM(QCM:list, tabrep:list)->list:
    '''
    fonction de passage de QCM : pour chaque question, affiche la question 
    puis les trois propositions et enfin stocke le numéro de la réponse 
    du candidat dans un tableau qui sera ensuite renvoyé.
    '''
    print("-----------------------------------------")
    print("                QUESTION                 ")
    print("-----------------------------------------")
    for i in range(len(QCM[0])):  # On parcourt les questions
        affichageQCM(QCM, i)
        while True:
            try:
                reponse = int(input(f"Votre réponse pour la question {i+1} (1, 2 ou 3) : "))
                if reponse in [1, 2, 3]:
                    tabrep[i] = reponse
                    break
                else:
                    print("Veuillez entrer un nombre entre 1 et 3.")
            except ValueError:
                print("Entrée non valide, veuillez entrer un nombre.")
    return tabrep


def correctionQCM(QCM:list):
    '''
    Affiche la correction de l'ensemble du QCM (uniquement les questions 
    et les bonnes réponses)
    '''
    print("-----------------------------------------")
    print("                 REPONSE                 ")
    print("-----------------------------------------")
    for i in range(len(QCM[0])):  # On parcourt les questions
        affichage_bonne_rep(QCM, i)
        print("---------------------------")

def getQcmFromFile(nameFile:str) -> list: # pathFile:str
    '''
    Récupère QCM depuis un fichier tkt et renvoie la variable à la main.

    Params:
    - pathFile : Chemin d'accès vers le fichier.txt

    Returns:
    - QCM: Renvoie la variable QCM qui est utilisé dans la library
    '''
    QCM=[[], [], [], []]

    if os.path.exists(nameFile):
        with open(nameFile, 'r') as file:
            # vérifie qu'il y a un nombre de line qui est un modulo de 4 car sinon il trop/pas assez d'éléments dans le fichier
            fileline = file.readlines()
            if ((len(fileline)) %4 != 0):
                return f"Number of line in {nameFile} is not a % of 4"
            
            for i, valueLine in enumerate(fileline):
                line = ''.join(chr(int(i)) for i in valueLine.replace("[", "").replace("]", "").replace("'", "").replace("\n", "").split(", "))
                if (i%4 == 0):
                    QCM[0].append(line)
                elif (i%4 == 1):
                    QCM[1].append(line)
                elif (i%4 == 2):
                    QCM[2].append(line)
                elif (i%4 == 3):
                    QCM[3].append(line)
            
            # vérifie si il y a une seule bonne réponse par question, sinon renvoie la question qui pose pb
            for i in range(len(QCM[0])):
                if (not ("*" in QCM[1][i] or "*" in QCM[2][i] or "*" in QCM[3][i])):
                    return f"\n---------------\nQCM Question {i} :\n - {QCM[0][i]}Do not have a good response.\n---------------"

            return QCM
    else: 
        return "file not found"

def convertFileToAscii(nameFile:str) -> list:
    '''
    Récupère QCM depuis un fichier tkt et renvoie la variable à la main.

    Params:
    - pathFile : Chemin d'accès vers le fichier.txt

    Returns:
    - QCM: Renvoie la variable QCM qui est utilisé dans la library
    '''
    QCM=[[], [], [], []]

    if os.path.exists(nameFile):
        with open(nameFile, 'r') as file:
            # vérifie qu'il y a un nombre de line qui est un modulo de 4 car sinon il trop/pas assez d'éléments dans le fichier
            fileline = file.readlines()
            if ((len(fileline)) %4 != 0):
                return f"Number of line in {nameFile} is not a % of 4"
            
            for i, valueLine in enumerate(fileline):
                if (i%4 == 0):
                    QCM[0].append(valueLine)
                elif (i%4 == 1):
                    QCM[1].append(valueLine)
                elif (i%4 == 2):
                    QCM[2].append(valueLine)
                elif (i%4 == 3):
                    QCM[3].append(valueLine)
            
            # vérifie si il y a une seule bonne réponse par question, sinon renvoie la question qui pose pb
            for i in range(len(QCM[0])):
                if (not ("*" in QCM[1][i] or "*" in QCM[2][i] or "*" in QCM[3][i])):
                    return f"\n---------------\nQCM Question {i} :\n - {QCM[0][i]}Do not have a good response.\n---------------"
        
        newFileAscii = open(nameFile.replace(".", "_ascii."), "w")
        writeAscii = ""
        for i in range(len(QCM[0])):
            for j in range(4): 
                writeAscii = writeAscii + f"{[ord(c) for c in QCM[j][i]]}" + "\n"

        newFileAscii.write(writeAscii)


    else: 
        return "file not found"