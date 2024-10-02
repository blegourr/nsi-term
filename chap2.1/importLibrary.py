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

  QCM = QCM_docstring.getQcmFromFile("./chap2.1/qcm.txt")
  if type(QCM) != list:
    print(f"Error : {QCM}")
    return
  print(QCM)
  """
  --------------------------------------------------------
                        CODE 
  --------------------------------------------------------
  """
  # création du tableau de réponse et le définie dans la variable tabRep
  tabrep = QCM_docstring.creer_tableaurep(QCM)

  print("-----------------------------------------")
  print("                QUESTION                 ")
  print("-----------------------------------------")

  # poses toutes les questions et récupère les réponses de l'utilisateur pour chaque question.
  tabrep = QCM_docstring.passageQCM(QCM, tabrep)

  print("-----------------------------------------")
  print("                  SCORE                  ")
  print("-----------------------------------------")
  # Récupère le nombre de bonne réponse du player
  score = QCM_docstring.score(QCM, tabrep)
  # Récupère le nombre de nombre totale de réponse par rapport au nombre de question réussit
  total = QCM_docstring.total(score)
  # Affiche le nombre de bonne réponse / le nombre de question total
  print(f"Vous avez {total[0]}/{total[1]}")

  print("-----------------------------------------")
  print("                 REPONSE                 ")
  print("-----------------------------------------")
  # affiche la correction de toutes les questions
  QCM_docstring.correctionQCM(QCM)

QCM()