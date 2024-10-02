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
    '''
    return [0] * len(QCM[0])  # On base la taille du tableau sur le nombre de questions


def affichageQCM(QCM:list, i:int):
    '''
    permet d'afficher la question n°i du QCM contenue dans le tableau QCM.
    les réponses sont ensuite proposées
    l'étoile indiquant la bonne réponse est supprimée lors de l'affichage
    '''
    question = QCM[0][i]  # Les questions sont sur la première ligne de QCM
    reponses = [QCM[j][i].replace('*', '') for j in range(1, 4)]  # Les réponses sont sur les lignes 1 à 3
    print(f"Question {i+1}: {question}")
    for j, rep in enumerate(reponses, start=1):
        print(f"{j}. {rep}")


def score(QCM:list, rep:list)->list:
    '''
    calcule le score à chaque question (0 ou 1) en vérifiant si la réponse est 
    bonne dans les tableaux de réponse grâce au caractère *. Le tableau renvoyé 
    ne contient donc que des 0 ou des 1
    '''
    scores = []
    for i in range(len(QCM[0])):  # Parcourt des questions
        bonnes_reponses = [j for j in range(1, 4) if '*' in QCM[j][i]]  # Repères la bonne réponse
        if (rep[i] - 1) in [br - 1 for br in bonnes_reponses]:  # On ajuste l'indice de la réponse de l'utilisateur
            scores.append(1)  # Réponse correcte
        else:
            scores.append(0)  # Réponse incorrecte
    return scores


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
    for i in range(len(QCM[0])):  # On parcourt les questions
        affichage_bonne_rep(QCM, i)
        print("---------------------------")
