# y = ax² + bx + c (polynome second degre)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures


def load_data_train(nb):
    bruit = np.random.normal(0, 1, nb)
    x = [np.random.uniform(-3.0, 10.0) for i in range(nb)]
    x = np.sort(x)
    y = 10 * np.sin(x) / x + bruit
    x = x.reshape(-1, 1)
    return x, y


def training(degrees, x, y):
    # genere un tableau des polynomes
    models = [make_pipeline(PolynomialFeatures(degree), Ridge()) for degree in degrees]
    for model in models:
        model.fit(x, y)
    return models


def reshape(x):
    x = x.reshape(-1, 1)
    return x


def show_data(nb, models, degrees, x, y):
    f, ax = plt.subplots(1)
    plt.xlim(-5, 12)
    plt.ylim(-4, 16)
    ax.scatter(x, y, color="k")
    plt.title("Plot of our datsets")
    plt.xlabel("x")
    plt.ylabel("f(x)=10*sin(x)/x + gaussian")
    ax.grid(True)

    count = 0
    for degree in degrees:
        y_pred = models[count].predict(x)
        plt.plot(x, y_pred, linewidth=2)
        count += 1
    plt.show()


def show_polynomes(models, degrees, x, y):
    colors = ['green', 'red', 'blue', 'orange', 'brown', 'yellow', 'black']
    plt.figure()
    plt.title('Plot all models')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(x, y, color='black', s=50, marker='o', label='Training points')
    plt.axis([-4, 12, -5, 15])
    count = 0
    for degree in degrees:
        y_pred = models[count].predict(x)
        plt.plot(x, y_pred, color=colors[count], linewidth=2, label="degree %d" % degree)
        count += 1
    plt.grid(True)
    plt.legend()
    plt.show()

#Min square error (équart moyen au carré)
def compute_errors(models, degrees, x, y):
    count = 0
    for model in models:
        prediction = model.predict(x)
        print('Degree %.2f : Residual sum of squares : %.2f' % \
              (degrees[count], np.mean((prediction - y) ** 2)))
        count += 1

if __name__ == '__main__':
    x_train, y_train = load_data_train(15)
    degrees = [1, 3, 6, 9, 12]
    models = training(degrees, x_train, y_train)

    # correction :
    show_polynomes(models,degrees,x_train,y_train)
    #show_data(15, models, degrees, x_train, y_train)

    x_test, y_test = load_data_train(50)
    #show_data(50, models, degrees, x_test, y_test)
    show_polynomes(models, degrees, x_test, y_test)

    print("RSS x_test / y_test :")
    compute_errors(models, degrees, x_test, y_test)
    print("RSS x_train / y_train :")
    compute_errors(models, degrees,  x_train, y_train)

