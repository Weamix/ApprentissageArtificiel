import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def load_data():
    x = np.array([[6], [8], [10], [14], [18]])
    y = [7, 9, 13, 17.5, 18]
    return x, y


def load_data_test():
    x = np.array([[8], [9], [11], [16], [12]])
    y = [11, 8.5, 15, 18, 11]
    return x, y


def learning_linear_regression(x, y):
    reg = LinearRegression().fit(x, y)
    return reg


def rss(model, x, y):
    # ce que ça fait : pour tous les points, somme de l'écart en vraies valeurs (y) et valeurs prédites (f(x)) au carré
    print('Residual sum of squares : %.2f' % np.sum((y - model.predict(x)) ** 2))
    return np.sum((model.predict(x) - y) ** 2)


def show_data(model, x, y, points_x):
    f, ax = plt.subplots(1)
    ax.scatter(x, y, color="k")
    ax.set_ylim(ymin=0)
    ax.set_xlim(xmin=0)
    plt.xlim(0, 25)
    plt.ylim(0, 25)
    ax.grid(True)
    plt.title("Pizza prices plotted against sizes")
    plt.xlabel("Prices in euros")
    plt.ylabel("Sizes in cms")

    plt.plot(points_x, model.predict(points_x))

    plt.show()


if __name__ == '__main__':
    # JAMAIS FIT (apprendre) AVEC DES DONNEES DE TEST
    x_train, y_train = load_data()
    x_test, y_test = load_data_test()

    points_x = np.arange(0.0, 25.0, 0.1).reshape(-1, 1)
    model = learning_linear_regression(x_train, y_train)
    show_data(model, x_train, y_train, points_x)

    print("RSS x_train / y_train :")
    rss(model, x_train, y_train)

    print("RSS x_test / y_test :")
    rss(model, x_test, y_test)
    # erreur en généralisaiton, à quel point on est bon dans le monde réel.

    # biais : modèle trop simple -> il faudrait avoir d'autres params comme le type d'ingrédient
