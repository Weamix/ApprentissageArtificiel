import numpy as np
import matplotlib.pyplot as plt
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns


def load_data():
    dataframe = p.read_csv("iris.csv")

    # Combien d'exemples : 150
    # Combien de classes (species) : 3 classes
    # Combien de caractéristiques descriptives ? De quels types ? 4 : SepalLengthCm , SepalWidthCm , PetalLengthCm, PetalWidthCm

    print("shape : ", dataframe.shape)
    print("info : ", dataframe.info())
    print("describe : ", dataframe.describe())
    print("head : ", dataframe.head())

    # Combien d’exemples de chaque classe ? 50 chacune
    print("value_counts : ", dataframe['Species'].value_counts())

    # Comment sont organisés les exemples ? Ordonnées d'où l'importance du random split

    train, test = train_test_split(dataframe,test_size=0.3)
    x_train = train
    y_train = train['Species']
    del x_train['Id']
    del x_train['Species']

    x_test = test
    y_test = test['Species']
    del x_test['Id']
    del x_test['Species']

    #x_train ,y_train, x_test, y_test = train_test_split(data_x,data_y,test_size=0.3)
    return dataframe


def KNeighborsClassifier(n_neighbors=3):
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    return knn, y_pred


def plotData(data):
    sns.set_style("whitegrid")
    sns.pairplot(data,hue="Species")
    plt.show()


if __name__ == '__main__':
    dataframe = load_data()
    plotData(dataframe)
