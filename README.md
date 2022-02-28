# ApprentissageArtificiel

## Vitse Maxime (I2L)

#### notation : 1tp noté (voir 2) + controle mi parcours (connaissances cours) + examen machine


Cours : https://www-lisic.univ-littoral.fr/~teytaud/apprentissage.html

TP0 - regression linéaire : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp0.pdf

TP1 - regression polynomiale : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp1.pdf

TP2 - k plus proches voisins (classification et régression): https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp2.pdf

TP3 - arbres de décision (classification et régression) : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp3.pdf

TP4 - perceptron : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/perceptronTP.pdf

TP5 - réseaux de neuronnes : https://www-lisic.univ-littoral.fr/~teytaud/files/Cours/Apprentissage/tp5.pdf

TP6 - apprentissage par renforcement : espilon greedy / q-learning [TP6-qlearning/qlearning.pdf](TP6-qlearning/qlearning.pdf)

Apprentissage automatique :

    Des données de chiens et de chats
    je veux apprendre à reconnaitre les 2

Régression : 

    Quand j'essaye d'apprendre des données dans R
    Exemple la T°
    Opposé de la classification

Linéaire : 

    un programme qui peut apprendre qu'une droite ou un hyper plan (droite en plein de dimensions)

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