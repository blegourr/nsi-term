# Problématique
**Comment la cryptographie a-t-elle évolué pour rester efficace face aux progrès des techniques de déchiffrement ?**

---

# Introduction
La question de la **sécurité des données** est devenue centrale. Chaque jour, des milliards d’informations circulent sur Internet : messages personnels, transactions bancaires, dossiers médicaux, communications gouvernementales... Mais ces données sont-elles vraiment à l’abri ?

Pour sécuriser ces communications, il faut garantir :
- **la confidentialité**
- **l'intégrité**
- **l'authenticité**

Grâce aux **mathématiques** et à l’**informatique**, on a développé des méthodes de chiffrement pour protéger les informations.

---

# Le chiffre de César

**Signification** : Nommé d'après Jules César, qui l'utilisait pour ses communications militaires.  
**Date de création** : Vers -50 av. J.-C.  
**Date d'utilisation** : Antiquité, mais aussi parfois plus tard à des fins pédagogiques.
**Représentation** : Machine à écrire

**Principe** : Le chiffre de César est l'un des plus anciens systèmes de chiffrement. Il s'agit d'un chiffrement par substitution mono-alphabétique : chaque lettre du message va subir une translation vers une autre lettre, située un certain nombre de positions plus loin dans l'alphabet. C'est un chiffrement **symétrique** : la même clé (le décalage) sert à chiffrer et à déchiffrer.

**Exemple** : Avec un décalage de 3 :

- A devient D
- B devient E
- C devient F
- …
- jusqu'à Z qui devient C

Pour chiffrer un message, on applique ce décalage à chaque lettre. Par exemple, « B O N J O U R » devient « E R Q M R X U » avec un décalage de 3. Pour déchiffrer, il suffit de soustraire le décalage.

**Modulo** : On peut représenter chaque lettre par un nombre de 0 à 25 (A=0, B=1, ..., Z=25). Le chiffrement s'écrit alors :

```python
LettreChiffrée = (LettreOriginale + Décalage) % 26
```

Exemple avec Z :
```python
(25+3) % 26 = 28 % 26 = 2  # donc C
```

**Sécurité** : Le nombre de clés possibles est de 25 (puisqu’un décalage de 0 ne change rien). C'est donc un système très simple à casser :

- Il suffit d'essayer toutes les possibilités (**attaque par force brute**).
- Ou d'utiliser l'**analyse fréquentielle** (étudier la fréquence des lettres dans le texte chiffré).

---

## Notion mathématique : Factoriel
Le **factoriel** d'un nombre n (noté n!) est le produit de tous les entiers de 1 à n. Par exemple :

```python
4! = 4 x 3 x 2 x 1 = 24
```

Il sert à compter le nombre de façons d'ordonner n objets.

---

# La machine Enigma

**Signification** : « Enigma » signifie « énigme » en grec.  
**Date de création** : 1918 (brevetée par Arthur Scherbius).  
**Date d'utilisation** : Principalement de 1920 à 1945, surtout pendant la Seconde Guerre mondiale par l'Allemagne.

**Principe** : La machine Enigma, utilisée par l'Allemagne pendant la Seconde Guerre mondiale, était un dispositif électromécanique de chiffrement. Son fonctionnement se décompose en plusieurs étapes :

1. **Clavier** : Lorsqu'on appuie sur une lettre, un courant électrique est envoyé dans la machine.
2. **Plugboard (tableau de connexions)** : Permet de permuter certaines lettres entre elles.

> On souhaite choisir 10 paires parmi 26 lettres, sans tenir compte de l'ordre des paires ni de l'ordre dans chaque paire.

$$
\text{Choix de 20 lettres parmi 26 (pour 10 paires)} : \quad \binom{26}{20} = \frac{26!}{20!\,6!} = \binom{26}{6}
$$


$$
\text{Pour les 20 lettres, on dispose de 10 câbles pour les relier 2 à 2 :}
$$

$$
\text{1er câble :} \quad \frac{20!}{2!\,18!} \\
$$

$$
\quad
$$

$$
\text{2e câble :} \quad \frac{18!}{2!\,16!} \\
$$

$$
\quad
$$

$$
\ldots \\
$$

$$
\quad
$$

$$
\text{10e câble :} \quad \frac{2!}{2!\,0!} = 1
$$

$$
\quad
$$

$$
\text{Simplification :} \quad \frac{20!}{2!\,\color{red}\cancel{18!}} \times \frac{\color{red}\cancel{18!}}{2!\,\color{red}\cancel{16!}} \times \frac{\color{red}\cancel{16!}}{2!\,\cancel{14!}} \times \cdots \times \frac{\color{red}\cancel{2!}}{2!\,\cancel{0!}} = \frac{20!}{{(2!)^{10}}} = \frac{20!}{{2^{10}}}
$$


- À chaque étape, le numérateur du terme précédent s'annule avec le dénominateur du terme suivant.
- Il reste donc seulement le $20!$ au numérateur, et $2!$ multiplié 10 fois au dénominateur, soit $(2!)^{10}$.


$$
\text{Simplification finale :} \quad \frac{20!}{2^{10}}
$$


$$
\text{L’ordre des câbles n’importe pas :} \quad 10! \text{ permutations}
$$


$$
\text{Total plugboard :} \quad \frac{26!}{20!\,6!} \times \frac{20!}{2^{10}} \div 10! \approx 15 \times 10^{13}
$$


3. **Passage à travers les rotors** : Les rotors mélangent les lettres selon un certain ordre (permutation de l'alphabet). À chaque frappe, le rotor de droite avance d'un cran, ce qui change la substitution à chaque lettre. Cela crée un chiffrement **polyalphabétique**.


> Le choix et l'ordre des rotors correspond à un triplet d'éléments distincts pris dans un ensemble à 5 éléments :

$$
5 \times 4 \times 3 = 60 \text{ possibilités}
$$


> Chaque rotor peut être placé sur une des 26 positions (lettres de l'alphabet). Pour 3 rotors c'est comme choisir un 3-uplet avec remise parmi 26 :

$$
26 \times 26 \times 26 = 17\,576 \text{ positions possibles}
$$


4. **Passage par le réflecteur** : Relie les lettres deux à deux et renvoie le courant dans l'autre sens, rendant le chiffrement réversible.


> Le réflecteur forme 13 paires de lettres parmi les 26, sans tenir compte de l'ordre, ni de l'ordre dans la paire.

$$
\frac{26!}{13!\,2^{13}} \approx 79 \times 10^{11}
$$


5. **Retour** : Le courant repasse à travers les rotors et le plugboard.

6. **Affichage de la lettre chiffrée** : Une lampe s'allume pour indiquer la lettre obtenue.


**Nombre total de configurations** :
On multiplie les quatre résultats précédents (rotors, positions des rotors, plugboard, réflecteur) :

$$
60 \times 17\,576 \times 79 \times 10^{11} \times 15 \times 10^{13} \approx 125 \times 10^{31}
$$

Ce nombre astronomique explique pourquoi Enigma était considérée comme inviolable à l'époque. La probabilité de décrypter un message par hasard est quasi nulle. La complexité d'Enigma réside dans le nombre de configurations possibles, bien plus que dans la difficulté des opérations mathématiques utilisées.

**Comment Enigma a été craquée** :
La machine Enigma a été cassée grâce aux efforts conjoints de mathématiciens polonais (notamment Marian Rejewski, Jerzy Różycki et Henryk Zygalski) qui ont réussi à reconstituer le fonctionnement interne de la machine dès les années 1930. Plus tard, les Britanniques à Bletchley Park, dirigés par Alan Turing, ont automatisé le décryptage avec des machines appelées "bombes". Ils ont exploité des faiblesses dans les procédures allemandes (messages répétitifs, erreurs humaines, absence de chiffrement d'une lettre par elle-même) et des indices dans les messages pour réduire le nombre de configurations à tester. Cela a permis de lire de nombreux messages allemands et a eu un impact majeur sur l'issue de la guerre.

*Source : bibmath.net - Enigma*

---

# Le chiffrement RSA

**Signification** : RSA vient des initiales de ses inventeurs : Ron Rivest, Adi Shamir et Leonard Adleman.  
**Date de création** : 1977.  
**Utilisation** : Pour de nombreux usages (transactions bancaires, signatures numériques, etc.).

**Principe** : RSA est un algorithme de **cryptographie asymétrique**, utilisant une paire de clés : une publique pour chiffrer et une privée pour déchiffrer. Il repose sur la difficulté de décomposer un grand nombre en facteurs de nombres premiers.

**Différences entre symétrique et asymétrique** :

- **Symétrique** : même clé pour chiffrer et déchiffrer (ex : chiffre de César, Enigma).
- **Asymétrique** : deux clés différentes, l'une publique et l'autre privée (ex : RSA).

**Exemple concret** : Lors d'une connexion à une page web sécurisée (HTTPS), le chiffrement asymétrique (comme RSA) sert à échanger une clé secrète, puis le chiffrement symétrique (comme AES) est utilisé pour la suite de la communication, car il est plus rapide.

---

# Conclusion
Assurer la **sécurité des données** est un enjeu majeur dans notre société connectée. Les méthodes de chiffrement (qu’elles soient simples comme le chiffre de César ou complexes comme Enigma et RSA) montrent que la robustesse d’un système dépend de sa conception et de sa complexité.

Cependant, la sécurité absolue n’existe pas :

- les progrès technologiques (**quantique**, puissance de calcul, nouveaux algorithmes),
- les failles humaines ou organisationnelles peuvent remettre en cause un système.

**Ouverture** : L'arrivée des ordinateurs quantiques pourrait bouleverser la cryptographie actuelle, car ils pourraient casser certains algorithmes (comme RSA) très rapidement. De nouveaux protocoles, comme ceux basés sur la cryptographie quantique (QKD, QBER, NISQ), sont en cours de développement pour anticiper cette révolution.

En définitive, on ne peut jamais garantir une sécurité totale, mais on peut la rendre suffisamment forte pour protéger efficacement nos données.
