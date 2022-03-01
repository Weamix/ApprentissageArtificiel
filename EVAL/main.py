import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


def analyze(data, type):
    # Pour chaque champs : data1 / data2

    # Apercu de la base
    print(data.head())
    # Nombre d'exemples : 101 / 17 379
    print(data.shape)
    # Nombre de caractéristiques descriptives : 25 / 14
    print(data.info())
    # Nombre d'exemples de chaque classe : 101 et 17 379 mais 0 classes car on est en régression
    print(data.describe())
    # Stats autour de la colonne "Z" :
    print(data[type].value_counts())
    # Matrice corrélation :
    matrix_correlation(data)


def matrix_correlation(data):
    averages = data.mean()
    print(averages)

    sns.set()
    plt.figure(figsize=(15, 8))
    plt.hist(data)
    print(data.shape)
    sns.heatmap(data.corr(), vmax=0.5, cmap="PiYG")
    plt.title('Correlation matrix')
    plt.show()

def label_encode(data, col):
    # Transforme un type catégorie en entier
    le = LabelEncoder()
    # On récupère tous les noms de catégories possibles
    unique_values = list(data[col].unique())
    le_fitted = le.fit(unique_values)
    # On liste l'ensemble des valeurs
    values = list(data[col].values)
    # On transforme les catégories en entier
    values_transformed = le.transform(values)
    # On fait le remplacement de la colonne dans le dataframe d'origine
    data[col] = values_transformed

if __name__ == '__main__':
    dataCCfinal_1 = pd.read_csv('csv/dataCCfinal_1.csv')
    dataCCfinal_2 = pd.read_csv('csv/dataCCfinal_2.csv')

    #label_encode(dataCCfinal_1, 'C')

    dataCCfinal_1 = dataCCfinal_1.drop(columns=['A','B','C'], axis=1)
    #dataCCfinal_2 = dataCCfinal_2.drop(['C'], axis=1)

    analyze(dataCCfinal_1, 'Z')
    #analyze(dataCCfinal_2, 'Z')


