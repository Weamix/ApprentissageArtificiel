import pandas as pd
from sklearn import tree
import graphviz
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


def tree_barbecue():
    data = pd.read_csv("barbecue.csv")
    print(data)
    # analyze(data, 'barbecue')

    x_train = data
    y_train = data['barbecue']
    del x_train['barbecue']

    # x_train, y_train, x_test, y_test = split_data(data, 'Type')

    classifier = tree.DecisionTreeClassifier(criterion='entropy')
    classifier.fit(x_train, y_train)
    tree.export_graphviz(classifier, out_file='tree.dot', feature_names=['Meteo', 'Amis', 'Vent', 'Jour'])


def tree_glass():
    data = pd.read_csv("glass-data.csv")
    del data['Id']
    print(data)
    analyze(data, 'Type')

    x_train, y_train, x_test, y_test = split_data(data, 'Type')

    # classifier = tree.DecisionTreeClassifier(min_impurity_decrease=0.02, max_depth=10)
    # classifier = tree.DecisionTreeClassifier(criterion='entropy', min_impurity_decrease=0.00, max_depth=8)
    # classifier = tree.DecisionTreeClassifier(criterion='entropy', max_depth=8)
    # classifier = tree.DecisionTreeClassifier(min_impurity_decrease=0.02, max_depth=8)

    classifier = tree.DecisionTreeClassifier(criterion='entropy',max_depth=6)
    classifier.fit(x_train, y_train)
    tree.export_graphviz(classifier, out_file='tree.dot', feature_names=['refractive index','Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Potassium', 'Calcium', 'Barium', 'Iron'])
    display_score_classifier(classifier, x_train, y_train, x_test, y_test)


def analyze(data, type):
    print(data.shape)
    print(data.info())
    print(data.describe())
    print(data.head())
    print(data[type].value_counts()) #7 classes

    '''
    214 éléments
    9 caractéristiques : ['refractive index','Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Potassium', 'Calcium', 'Barium', 'Iron']
    
    Bases de train et de test  => pour éviter le surapprentissage (= généralisation)
    
    Train score > Test score => il y a surapprentissage
    K plus proche voisins , on rajoute des voisins
    Arbres de décisions => on élague
    
    '''


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


if __name__ == '__main__':
    #tree_barbecue()
    tree_glass()