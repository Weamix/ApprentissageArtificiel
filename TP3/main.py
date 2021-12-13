import pandas as pd
from sklearn import tree
import graphviz


def tree_barbecue():
    data = pd.read_csv("barbecue.csv")
    print(data)
    print(data['barbecue'])
    x_train = data
    y_train = data['barbecue']
    del x_train['barbecue']
    classifier = tree.DecisionTreeClassifier(criterion='entropy')
    classifier.fit(x_train, y_train)
    tree.export_graphviz(classifier, out_file='tree.dot', feature_names=['Meteo', 'Amis', 'Vent', 'Jour'])


def tree_glass():
    data = pd.read_csv("glass-data.csv")
    print(data)
    del data['Id']
    del data['refractive index']


    x_train = data
    y_train = data["Type"]
    del x_train['Type']
    classifier = tree.DecisionTreeClassifier(criterion='entropy')
    classifier.fit(x_train, y_train)
    tree.export_graphviz(classifier, out_file='tree.dot', feature_names=['Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Potassium', 'Calcium', 'Barium', 'Iron'])


if __name__ == '__main__':
    #tree_barbecue()
    tree_glass()