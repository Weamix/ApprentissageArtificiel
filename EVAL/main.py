import pandas as pd


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


if __name__ == '__main__':
    dataCCfinal_1 = pd.read_csv('csv/dataCCfinal_1.csv')
    dataCCfinal_2 = pd.read_csv('csv/dataCCfinal_2.csv')
    analyze(dataCCfinal_1, 'Z')
    analyze(dataCCfinal_2, 'Z')


