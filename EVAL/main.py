import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import confusion_matrix, mean_absolute_error, mean_squared_error, r2_score
from sklearn import tree
from sklearn.neural_network import MLPClassifier,MLPRegressor


def analyze(data, type):
    # Pour chaque champs : data1 / data2
    # Apercu de la base
    print(data.head())
    # Nombre d'exemples : 101 / 17 379
    print(data.shape)
    # Nombre de caractéristiques descriptives : 25 / 14
    print(data.info())
    # Nombre d'exemples de chaque classe : 101 et 17 379
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
    sns.heatmap(data.corr(), vmax=0.5, cmap="PiYG", annot=False)
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


def split_data(data, y):
    train, test = train_test_split(data, test_size=0.3)
    x_train = train
    y_train = train[y]
    del x_train[y]

    x_test = test
    y_test = test[y]
    del x_test[y]

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


def k_neighbors(model_string, model, x_train, y_train, x_test, y_test):
    classifier = create_model(model, x_train, y_train)
    if model_string == "classifier":
        display_score_classifier(classifier, x_train, y_train, x_test, y_test)
    elif model_string == "regressor":
        display_score_regressor(classifier, x_train, y_train, x_test, y_test)


def decision_tree(classifier, x_train, y_train, x_test, y_test):
    classifier.fit(x_train, y_train)
    tree.export_graphviz(classifier, out_file='tree.dot',
                         feature_names=['F', 'G', 'I', 'L', 'N', 'Q'])
    display_score_classifier(classifier, x_train, y_train, x_test, y_test)


def neural_network(model, x_train, y_train, x_test, y_test):
    classifier = create_model(model, x_train, y_train)
    display_score(classifier, x_train, y_train, x_test, y_test)


def create_model(classifier, x, y):
    classifier.fit(x, y)
    return classifier


def display_score(classifier, x_train, y_train, x_test, y_test):
    print("Train score: {}, Test score {}".format(classifier.score(x_train, y_train), classifier.score(x_test, y_test)))
    y_pred = classifier.predict(x_test)
    print(confusion_matrix(y_test, y_pred))


if __name__ == '__main__':
    dataCCfinal_1 = pd.read_csv('csv/dataCCfinal_1.csv')
    dataCCfinal_2 = pd.read_csv('csv/dataCCfinal_2.csv')

    # label_encode(dataCCfinal_1, 'C')

    # F, G, I, L, N, Q et Z
    dataCCfinal_1 = dataCCfinal_1.drop(
        columns=['A', 'B', 'C', 'D', 'E', 'H', 'J', 'K', 'M', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'], axis=1)
    # dataCCfinal_2 = dataCCfinal_2.drop(['C'], axis=1)

    # analyze(dataCCfinal_1, 'Z')
    # analyze(dataCCfinal_2, 'Z')

    x_train1, y_train1, x_test1, y_test1 = split_data(dataCCfinal_1, 'Z')
    print("KNeighborsClassifier")
    k_neighbors("classifier", KNeighborsClassifier(), x_train1, y_train1, x_test1, y_test1)
    print("TreeClassifier")
    decision_tree(tree.DecisionTreeClassifier(criterion='entropy', max_depth=8), x_train1, y_train1, x_test1, y_test1)
    print("NeuralNetwork")
    neural_network(MLPClassifier(), x_train1, y_train1, x_test1, y_test1)

    # x_train2, y_train2, x_test2, y_test2 = split_data(dataCCfinal_2, 'Z')
    # print("KNeighborsRegressor")
    # k_neighbors("regressor", KNeighborsRegressor(), x_train2, y_train2, x_test2, y_test2)
    # print("TreeRegressor")
    #decision_tree( tree.DecisionTreeRegressor(min_impurity_decrease=0.02, max_depth=5), x_train1, y_train1, x_test1, y_test1)
    # print("NeuralNetworkRegressor")
    #neural_network(MLPRegressor(), x_train1, y_train1, x_test1, y_test1)
