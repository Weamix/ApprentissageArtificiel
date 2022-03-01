import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import confusion_matrix, mean_absolute_error, mean_squared_error, r2_score
from sklearn import tree
from sklearn.neural_network import MLPClassifier, MLPRegressor


def analyze(data, type):
    # Pour chaque "champ : data1 / data2"
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


def split_data(data, y):
    train, test = train_test_split(data, test_size=0.3)
    x_train = train
    y_train = train[y]
    del x_train[y]

    x_test = test
    y_test = test[y]
    del x_test[y]

    return x_train, y_train, x_test, y_test


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


def decision_tree(model_string, classifier, x_train, y_train, x_test, y_test, letters):
    classifier.fit(x_train, y_train)
    tree.export_graphviz(classifier, out_file='tree.dot',
                         feature_names=letters)
    if model_string == "classifier":
        display_score_classifier(classifier, x_train, y_train, x_test, y_test)
    elif model_string == "regressor":
        display_score_regressor(classifier, x_train, y_train, x_test, y_test)


def neural_network(model_string, model, x_train, y_train, x_test, y_test):
    classifier = create_model(model, x_train, y_train)
    if model_string == "classifier":
        display_score_classifier(classifier, x_train, y_train, x_test, y_test)
    elif model_string == "regressor":
        display_score_regressor(classifier, x_train, y_train, x_test, y_test)


def create_model(classifier, x, y):
    classifier.fit(x, y)
    return classifier


def data_replace_string_by_float():
    # Strings to float without , but .
    dataCCfinal_2['B'] = dataCCfinal_2['B'].str.replace(',', '.').astype(float)
    dataCCfinal_2['K'] = dataCCfinal_2['K'].str.replace(',', '.').astype(float)
    dataCCfinal_2['I'] = dataCCfinal_2['I'].str.replace(',', '.').astype(float)
    dataCCfinal_2['J'] = dataCCfinal_2['J'].str.replace(',', '.').astype(float)
    dataCCfinal_2['L'] = dataCCfinal_2['L'].str.replace(',', '.').astype(float)


if __name__ == '__main__':
    dataCCfinal_1 = pd.read_csv('csv/dataCCfinal_1.csv')
    dataCCfinal_2 = pd.read_csv('csv/dataCCfinal_2.csv')

    data_replace_string_by_float()

    # label_encode(dataCCfinal_1, 'C')

    # Colonnes les plus et moins corrélés à Z : F, G, I, L, N, Q -data1
    dataCCfinal_1_FGILNQ = dataCCfinal_1.drop(
        columns=['A', 'B', 'C', 'D', 'E', 'H', 'J', 'K', 'M', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'], axis=1)
    # Colonnes les plus corrélés à Z : F,I,N,O,P - data1
    dataCCfinal_1_FINOP = dataCCfinal_1.drop(
        columns=['A', 'B', 'C', 'D', 'E', 'G', 'H', 'J', 'K', 'L', 'M', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'],
        axis=1)
    # Colonnes les plus corrélés à Z : ['D', 'I', 'J', 'M', 'N'] - data2
    dataCCfinal_2_DIJMN = dataCCfinal_2.drop(['A', 'B', 'C', 'E', 'F', 'G', 'H', 'K', 'L'], axis=1)

    """
    print("ANALYZE DATA"
    analyze(dataCCfinal_1, 'Z')
    analyze(dataCCfinal_2, 'Z')
    """

    print("SPLIT, TRAIN, TEST - ALGOS ON DATASET 1")
    x_train1, y_train1, x_test1, y_test1 = split_data(dataCCfinal_1_FINOP, 'Z')
    print("\nKNeighborsClassifier")
    k_neighbors("classifier", KNeighborsClassifier(), x_train1, y_train1, x_test1, y_test1)
    print("\nTreeClassifier")
    letters_FINOP = ['F', 'I', 'N', 'O', 'P']
    #letters_FGILNQ= ['F', 'G', 'I', 'L', 'N', 'Q']
    decision_tree("classifier",tree.DecisionTreeClassifier(criterion='entropy', max_depth=8), x_train1, y_train1, x_test1, y_test1, letters_FINOP)
    print("\nNeuralNetwork")
    neural_network("classifier",MLPClassifier(), x_train1, y_train1, x_test1, y_test1)

    print("SPLIT, TRAIN, TEST - ALGOS ON DATASET 2")
    x_train2, y_train2, x_test2, y_test2 = split_data(dataCCfinal_2_DIJMN, 'Z')
    print("\nKNeighborsRegressor")
    k_neighbors("regressor", KNeighborsRegressor(), x_train2, y_train2, x_test2, y_test2)
    print("\nTreeRegressor")
    letters_DIJMN = ['D', 'I', 'J', 'M', 'N']
    decision_tree("regressor", tree.DecisionTreeRegressor(min_impurity_decrease=0.02, max_depth=5), x_train2, y_train2,
                  x_test2, y_test2, letters_DIJMN)
    print("\nNeuralNetworkRegressor")
    neural_network("regressor", MLPRegressor(), x_train2, y_train2, x_test2, y_test2)
