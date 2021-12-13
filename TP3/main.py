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


if __name__ == '__main__':
    tree_barbecue()