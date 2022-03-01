### Vitse Maxime M1 I2L

Objectif : apprendre la colonne Z

## How to run code?

Using python

Click right on the file and select `Run` on Pycharm ;-)

## Explications/choix

### Analyze data : 

Champ : dataCCfinal_1 / dataCCfinal_2

    Nombre d'exemples : 101 / 17 379

    Nombre de caractéristiques descriptives : 25 / 14

    Nombre d'exemples de chaque classe : 101 / 17 379


### Matrice de corélation - dataCCfinal_1 - Cas de classification

    Suppresion des colonnes A, B et C pour générer la matrice de corrélation
    A et B ont des valeurs fixes
    C sont des strings

![imgs/correlation_matrix_data_1.png](imgs/correlation_matrix_data_1.png)

Les champs qui ont une corrélation faibles ou fortes sont : 
F, G, I, L, N, Q

Avec les annotations à true , on peut confirmer plus facilement
Donc >0.2 et > -0.6

![imgs/correlation_matrix_data_1.png](imgs/correlation_matrix_data_1_with_annot.png)

### Algorithmes - dataCCfinal_1
- K voisins avec  F, G, I, L, N, Q et Z
    
```
KNeighborsClassifier
Train score :  0.7428571428571429
Test score :  0.5806451612903226
[[14  0  0  1  0  0  0]
 [ 0  0  6  3  0  0  0]
 [ 0  1  0  0  0  0  0]
  0  0  0  2  0  0  0]
 [ 0  0  0  2  0  0  0]
 [ 0  0  0  0  0  1  0]
 [ 0  0  0  0  0  0  1]]
 ```

- Arbre de décisions avec  F, G, I, L, N, Q

```
TreeClassifier
Train score :  0.7857142857142857
Test score :  0.8387096774193549
[[10  0  0  0  0  0]
 [ 0  4  0  0  0  0]
 [ 0  0  6  0  0  0]
 [ 0  0  0  1  0  0]
 [ 0  0  0  0  0  5]
 [ 0  0  0  0  0  5]]
```

![imgs/TreeClassifier_data1.png](imgs/TreeClassifier_data1.png)

- Réseaux de neuronnes avec  F, G, I, L, N, Q et Z

```
NeuralNetwork
Train score: 0.8571428571428571
Test score 0.7741935483870968
[[12  0  0  0  0  0  0]
 [ 0  5  0  2  0  0  0]
 [ 0  2  0  1  0  0  0]
 [ 0  0  0  5  0  0  0]
 [ 0  0  0  1  0  0  1]
 [ 0  0  0  0  0  2  0]
 [ 0  0  0  0  0  0  0]]
```

### Si on chosiit de prendre les valeurs les plus corélés à Z : ['F', 'I', 'N', 'O', 'P']
Nous aurons des meilleurs scores :

```
KNeighborsClassifier
Train score :  0.8285714285714286
Test score :  0.8709677419354839
[[13  0  0  1  0  0  0]
 [ 0  5  0  0  0  0  0]
 [ 0  0  1  0  0  0  0]
 [ 0  0  0  3  0  0  0]
 [ 0  0  0  0  1  0  0]
 [ 0  0  0  0  0  3  0]
 [ 0  0  0  2  1  0  1]]
 
TreeClassifier
Train score :  0.9714285714285714
Test score :  0.9354838709677419
[[14  0  0  0  0  0  0]
 [ 0  5  0  0  0  0  0]
 [ 0  0  0  0  0  0  1]
 [ 0  0  0  3  0  0  0]
 [ 0  0  0  0  1  0  0]
 [ 0  0  0  0  0  3  0]
 [ 0  0  0  0  1  0  3]]
 
NeuralNetwork
Train score: 0.8571428571428571
Test score 0.8709677419354839
[[14  0  0  0  0  0  0]
 [ 0  5  0  0  0  0  0]
 [ 0  0  1  0  0  0  0]
 [ 0  0  0  3  0  0  0]
 [ 0  0  0  0  0  0  1]
 [ 0  0  0  0  0  3  0]
 [ 0  2  1  0  0  0  1]]
```

    Quand le Train score > Test score => il y a surapprentissage
    Donc garder les colonnes ['F', 'I', 'N', 'O', 'P'] est mieux pour le NeuralNetwork et pour KNeighborsClassifier
    mais pour TreeClassifier, il y a un surapprentissage
    Avec ['F', 'G', 'I', 'L', 'N', 'Q'], ce n'est pas le cas

    Le plus performant est TreeClassifier -> NeuralNetwork -> KNeighborsClassifier

### Matrice de corélation - dataCCfinal_2 - Cas de régression

![imgs/correlation_matrix_data_1.png](imgs/correlation_matrix_data_2.png)

Les colonnes le plus en coorélation avec Z sont : D,I,J,M,N