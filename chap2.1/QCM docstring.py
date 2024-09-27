# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:40:40 2021

@author: resptechno
"""
def creer_tableaurep(QCM:list)->list:
  '''
  permet de créer un tableau ou seront stockées les réponses données 
  par l'utilisateur (1, 2 ou 3 pour chaque question)
  le tableau renvoyé a pour longueur le nombre de questions du QCM soit len(QCM[0]) 	
  '''
  return [0] * len(QCM) 


def affichageQCM(QCM:list,i:int):
  '''
  permet d'afficher la question n°i du QCM contenue dans le tableau QCM.
  les réponses sont ensuite proposées
  l'étoile indiquant la bonne réponse est supprimée lors de l'affichage
  '''
  question = QCM[i][0]
  reponses = [rep.replace('*', '') for rep in QCM[i][1]]
  print(f"Question {i+1}: {question}")
  for j, rep in enumerate(reponses, start=1):
      print(f"{j}. {rep}")

def score(QCM:list,rep:list)->list:
  '''
  calcule le score à chaque question (0 ou 1) en vérifiant si la réponse est 
  bonne dans les tableaux de réponse grâce au caractère *. Le tableau renvoyé 
  ne contient donc que des 0 ou des 1
  '''
  scores = []
  for i in range(len(QCM)):
      bonnes_reponses = [j for j, r in enumerate(QCM[i][1]) if '*' in r]
      if (rep[i] - 1) in bonnes_reponses:
          scores.append(1)  # Réponse correcte
      else:
          scores.append(0)  # Réponse incorrecte
  return scores

def total(tab_score:list)->list:
  '''
  renvoie un tuple contenant le score total et le nombre de questions du 
  type (7,10) quand le score est de 7/10
  '''
  score_total = sum(tab_score)
  nb_questions = len(tab_score)
  return (score_total, nb_questions)

def affiche_resultat(tab_total:list):
  '''
  affiche le résultat de l’utilisateur à partir d'un tableau à deux cases 
  contenant le score de l'utilisateur et le nombre de questions
  '''
  score, nb_questions = tab_total
  print(f"Votre score est de {score}/{nb_questions}.")

def affichage_bonne_rep(QCM:list,i:int):
  '''
  permet d'afficher la question n°i du QCM contenue dans le tableau QCM 
  puis uniquement la réponse correcte
  '''
  question = QCM[i][0]
  bonne_rep = [rep.replace('*', '') for rep in QCM[i][1] if '*' in rep][0]
  print(f"Question {i+1}: {question}")
  print(f"La bonne réponse est : {bonne_rep}")

def passageQCM(QCM:list,tabrep):
  '''
  fonction de passage de QCM : pour chaque question, affiche la question 
  puis les trois propositions et enfin stocke le numéro de la réponse 
  du candidat dans un tableau qui sera ensuite renvoyé.
  '''
  for i in range(len(QCM)):
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


def correctionQCM(QCM):
  '''
  Affiche la correction de l'ensemble du QCM (uniquement les questions 
  et les bonnes réponses)
  '''
  for i in range(len(QCM)):
    affichage_bonne_rep(QCM, i)
