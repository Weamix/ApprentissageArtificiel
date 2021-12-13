# ApprentissageArtificiel

## Vitse Maxime (I2L)

#### notation : 1tp noté (voir 2) + controle mi parcours (connaissances cours) + examen machine


Cours : https://www-lisic.univ-littoral.fr/~teytaud/apprentissage.html

TP0 : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp0.pdf

TP1 : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp1.pdf

TP2 : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp2.pdf

TP3 : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp3.pdf

Apprentissage automatique :

    Des données de chiens et de chats
    je veux apprendre à reconnaitre les 2

Régression : 

    Quand j'essaye d'apprendre des données dans R
    Exemple la T°
    Opposé de la classification

Linéaire : 

    un programme qui peut apprendre qu'une droite

TP1 : limité à des droites (modèle linéaire)

TP2 : on ne se limite plus à droits linéaires mais à des polynômes

Surapprentissage : 

    très bon avec nos points à nous mais nul en apprentissage
    On est bon avec nos images mais pas avec un nouveau jeu de donnée
    On ne connait pas le "concept"

    Pas bon en généralisation

Pattern pour l'année :

    x,y 
    x_train, y_train => fit
    x_test, y_test => score (mesure de perf)
    Surtout pas fit le test

Apprentissage supervisé :

    Trouver un modèle qui apprend à partir des données
    y=f(x)
    x des données de chien et chat
    y des étiquettes (tags) de chiens ou chats
    f notre modèle (algo) qui doit faire matcher x et y