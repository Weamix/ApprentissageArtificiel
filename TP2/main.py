import matplotlib.pyplot as plt
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import confusion_matrix
import seaborn as sns


def load_data_iris():
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


def load_data_auto():
    dataframe = p.read_csv("auto-mpg.data.csv")

    print("shape : ", dataframe.shape)
    print("info : ", dataframe.info())
    print("describe : ", dataframe.describe())
    print("head : ", dataframe.head())
    print("value_counts : ", dataframe['cylinders'].value_counts())

    del dataframe['name']
    return dataframe


def split_data_iris(data):
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


def split_data_auto(data):
    train, test = train_test_split(data, test_size=0.3)
    x_train = train
    y_train = train['mpg']
    del x_train['mpg']

    x_test = test
    y_test = test['mpg']
    del x_test['mpg']

    print(x_test.shape)
    print(y_test.shape)

    return x_train, y_train, x_test, y_test


def create_model(model, x, y):
    model.fit(x, y)
    return model


def display_score(classifier, x_train, y_train, x_test, y_test):
    print("Train score : ", classifier.score(x_train, y_train))
    print("Test score : ", classifier.score(x_test, y_test))
    y_pred = classifier.predict(x_test)
    print(confusion_matrix(y_test, y_pred))


def plot_data(data, c):
    sns.set_style("whitegrid")
    sns.pairplot(data, hue=c)
    plt.show()


if __name__ == '__main__':
    '''Commented part 1 TP2 : Iris
    
    data_iris = load_data_iris()
    plot_data(data_iris, "Species")
    x_train, y_train, x_test, y_test = split_data_iris(data_iris)
    classifier = create_model(KNeighborsClassifier(), x_train, y_train)
    display_score(classifier, x_train, y_train, x_test, y_test)
    
    '''

    # 392 exemples
    # 0 classes car on est en régression
    # 7 caractéristiques avec y=mpg

    data_auto = load_data_auto()
    plot_data(data_auto, "mpg")
    x_train, y_train, x_test, y_test = split_data_auto(data_auto)
    regressor = create_model(KNeighborsRegressor(), x_train, y_train)

