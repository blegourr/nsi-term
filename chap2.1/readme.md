## init
### crée un fichier.txt
- nom libre pour le fichier
- structure de donnée obligatoire
- ``*`` en début de ligne pour la bonne réponse
```
Question_1
Question_1_Reponse_1
Question_1_Reponse_2
Question_1_Reponse_3
```
### exemple
```
"test" + "test"
test
test test
*testtest
"test" + "test2"
test2
test test2
*testtest2
```

--------------------
## convert to ascii
### Commande à éxécuter pour remplacer "cacher" les réponses en remplacant chaque caractère par son code ascii
``python importLibrary.py ascii <NameFile>.txt``

### exemple du fichier ascci
```
[34, 116, 101, 115, 116, 34, 32, 43, 32, 34, 116, 101, 115, 116, 34, 10]
[116, 101, 115, 116, 10]
[116, 101, 115, 116, 32, 116, 101, 115, 116, 10]
[42, 116, 101, 115, 116, 116, 101, 115, 116, 10]
[34, 116, 101, 115, 116, 34, 32, 43, 32, 34, 116, 101, 115, 116, 50, 34, 10]
[116, 101, 115, 116, 50, 10]
[116, 101, 115, 116, 32, 116, 101, 115, 116, 50, 10]
[42, 116, 101, 115, 116, 116, 101, 115, 116, 50]
```

--------------------
## start with ascci

### Démarer le code via le fichier ascci
``python importLibrary.py start <NameFile_ascii>.txt``

#### (vous pouvez supprimer le fichier qui n'est pas en ascii)
