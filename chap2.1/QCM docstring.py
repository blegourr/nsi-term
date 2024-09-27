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
    

def affichageQCM(QCM:list,i:int):
    '''
    permet d'afficher la question n°i du QCM contenue dans le tableau QCM.
    les réponses sont ensuite proposées
    l'étoile indiquant la bonne réponse est supprimée lors de l'affichage
    '''

def score(QCM:list,rep:list)->list:
    '''
    calcule le score à chaque question (0 ou 1) en vérifiant si la réponse est 
    bonne dans les tableaux de réponse grâce au caractère *. Le tableau renvoyé 
    ne contient donc que des 0 ou des 1
    '''

def total(tab_score:list)->list:
    '''
    renvoie un tuple contenant le score total et le nombre de questions du 
    type (7,10) quand le score est de 7/10
    '''

def affiche_resultat(tab_total:list):
    '''
    affiche le résultat de l’utilisateur à partir d'un tableau à deux cases 
    contenant le score de l'utilisateur et le nombre de questions
    '''

def affichage_bonne_rep(QCM:list,i:int):
    '''
    permet d'afficher la question n°i du QCM contenue dans le tableau QCM 
    puis uniquement la réponse correcte
    '''

def passageQCM(QCM,tabrep):
	'''
	fonction de passage de QCM : pour chaque question, affiche la question 
    puis les trois propositions et enfin stocke le numéro de la réponse 
    du candidat dans un tableau qui sera ensuite renvoyé.
	'''

def correctionQCM(QCM):
	'''
	Affiche la correction de l'ensemble du QCM (uniquement les questions 
    et les bonnes réponses)
	'''
