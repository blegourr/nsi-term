import sys
"""
Structure de QCM:

QCM = [
  [question_1, question_2, question_3, question_4, ...],
  [question_1_response_1, question_2_response_1, question_3_response_1, question_4_response_1, ...],
  [question_1_response_2, question_2_response_2, question_3_response_2, question_4_response_2, ...],
  [question_1_response_3, question_2_response_3, question_3_response_3, question_4_response_3, ...]
]
"""

"""
--------------------------------------------------------
                     GETS_DATA
--------------------------------------------------------  
"""
filePath = sys.argv[2] # "./chap2.1/qcm.txt"

# command to start exemple : 
# 
# to covert file.txt to ascii.txt : python importLibrary.py ascii qcm.txt
# to start programs by ascii : python importLibrary.py start qcm.txt
"""
--------------------------------------------------------
                        IMPORT
--------------------------------------------------------  
"""
import QCM_docstring;

def QCM():
  """
  --------------------------------------------------------
                SET QUESTION AND ANSWER 
  --------------------------------------------------------
  """
  # QCM = [
  #     ["\"test\"+\"test\"", "\"test\"+\"test2\""],
  #     ["test", "test2"],
  #     ["test test", "test test2"],
  #     ["testtest*", "testtest2*"]
  # ]

  QCM = QCM_docstring.getQcmFromFile(filePath)
  if type(QCM) != list:
    print(f"Error : {QCM}")
    return
  """
  --------------------------------------------------------
                        CODE 
  --------------------------------------------------------
  """
  # création du tableau de réponse et le définie dans la variable tabRep
  tabrep = QCM_docstring.creer_tableaurep(QCM)

  # poses toutes les questions et récupère les réponses de l'utilisateur pour chaque question.
  tabrep = QCM_docstring.passageQCM(QCM, tabrep)

  # Récupère le nombre de bonne réponse du player
  score = QCM_docstring.score(QCM, tabrep)
  # Récupère le nombre de nombre totale de réponse par rapport au nombre de question réussit
  total = QCM_docstring.total(score)
  # Affiche le nombre de bonne réponse / le nombre de question total
  QCM_docstring.affiche_resultat(total)
  # affiche la correction de toutes les questions
  QCM_docstring.correctionQCM(QCM)

def getAction():
  print(sys.argv[1])
  if (sys.argv[1] == "start"):
    QCM()
  elif (sys.argv[1] == "ascii"):
    QCM_docstring.convertFileToAscii(filePath)

getAction()