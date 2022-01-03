import matplotlib.pyplot as plt
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import confusion_matrix, mean_absolute_error, mean_squared_error, r2_score
import seaborn as sns
from sklearn.preprocessing import StandardScaler


def load_data(file, c_value_counts, c_to_delete):
    dataframe = p.read_csv(file)

    print("shape : ", dataframe.shape)
    print("info : ", dataframe.info())
    print("describe : ", dataframe.describe())
    print("head : ", dataframe.head())
    print("value_counts : ", dataframe[c_value_counts].value_counts())

    del dataframe[c_to_delete]
    return dataframe


def split_data(data, y):
    train, test = train_test_split(data, test_size=0.3)
    x_train = train
    y_train = train[y]
    del x_train[y]

    x_test = test
    y_test = test[y]
    del x_test[y]

    print(x_test.shape)
    print(y_test.shape)

    return x_train, y_train, x_test, y_test


def create_model(model, x, y):
    model.fit(x, y)
    return model


def display_score_classifier(classifier, x_train, y_train, x_test, y_test):
    print("Train score : ", classifier.score(x_train, y_train))
    print("Test score : ", classifier.score(x_test, y_test))
    y_pred = classifier.predict(x_test)
    print(confusion_matrix(y_test, y_pred))


def display_score_regressor(regressor, x_train, y_train, x_test, y_test):
    y_pred = regressor.predict(x_test)
    print('Coefficient of determination: %s' % r2_score(y_test, y_pred))
    print('MAE: %s' % mean_absolute_error(y_test, y_pred))
    print('MSE: %s' % mean_squared_error(y_test, y_pred))
    y_pred2 = regressor.predict(x_train)
    print('MAE (training): %s' % mean_absolute_error(y_train, y_pred2))
    print('MSE (training): %s' % mean_squared_error(y_train, y_pred2))


def plot_data(data, c):
    sns.set_style("whitegrid")
    sns.pairplot(data, hue=c)
    plt.show()


def iris():
    data_iris = load_data("iris.csv", "Species", "Id")
    plot_data(data_iris, "Species")
    x_train, y_train, x_test, y_test = split_data(data_iris, "Species")
    classifier = create_model(KNeighborsClassifier(), x_train, y_train)
    #display_score_classifier(classifier, x_train, y_train, x_test, y_test)

def auto():
    data_auto = load_data("csv/auto-mpg.data.csv", "mpg", "name")
    #plot_data(data_auto, "mpg")
    x_train, y_train, x_test, y_test = split_data(data_auto, "mpg")
    regressor = create_model(KNeighborsRegressor(), x_train, y_train)
    display_score_regressor(regressor, x_train, y_train, x_test, y_test)

    #normaliser les données pour ne pas avoir des biais sur les poids du type 3000 vs 1.5
    print("After rescaling")
    ss = StandardScaler()
    x_train = ss.fit_transform(x_train)
    x_test = ss.transform(x_test)
    classifier = create_model(KNeighborsRegressor(), x_train, y_train)
    display_score_regressor(classifier, x_train, y_train, x_test, y_test)


if __name__ == '__main__':
    '''Commented part 1 TP2 : Iris
    
    Combien d'exemples : 150
    Combien de classes (species) : 3 classes
    Combien de caractéristiques descriptives ? De quels types ? 4 : SepalLengthCm , SepalWidthCm , PetalLengthCm, PetalWidthCm
    Combien d’exemples de chaque classe ? 50 chacune
    Comment sont organisés les exemples ? Ordonnées d'où l'importance du random split
      '''
    #iris()

    '''part 2 TP2 : Auto
        392 exemples
        0 classes car on est en régression
        7 caractéristiques avec y=mp
    '''

    auto()

