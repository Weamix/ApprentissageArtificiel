import matplotlib.pyplot as plt
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
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

    return dataframe


def split_data(data):
    train, test = train_test_split(data, test_size=0.3)
    x_train = train
    y_train = train['Species']
    del x_train['Id']
    del x_train['Species']

    x_test = test
    y_test = test['Species']
    del x_test['Id']
    del x_test['Species']

    print(x_test.shape)
    print(y_test.shape)

    # x_train ,y_train, x_test, y_test = train_test_split(data_x,data_y,test_size=0.3)
    return x_train, y_train, x_test, y_test


def create_model(classifier, x, y):
    classifier.fit(x, y)
    return classifier


def display_score(classifier, x_train, y_train, x_test, y_test):
    print("Train score : ", classifier.score(x_train, y_train))
    print("Test score : ", classifier.score(x_test, y_test))
    y_pred = classifier.predict(x_test)
    print(confusion_matrix(y_test, y_pred))


def plot_data(data):
    sns.set_style("whitegrid")
    sns.pairplot(data, hue="Species")
    plt.show()


if __name__ == '__main__':
    data = load_data()
    # plot_data(data)

    x_train, y_train, x_test, y_test = split_data(data)
    classifier = create_model(KNeighborsClassifier(), x_train, y_train)
    display_score(classifier, x_train, y_train, x_test, y_test)
