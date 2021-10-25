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


def show_data(x, y):
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

    reg = LinearRegression().fit(x, y)
    points_x = np.arange(0.0, 25.0, 0.1).reshape(-1, 1)
    plt.plot(points_x, reg.predict(points_x))

    print(reg.score(x, y))
    print(reg.coef_)
    print(reg.intercept_)

    plt.show()


if __name__ == '__main__':
    x, y = load_data()
    x_test, y_test = load_data_test()
    show_data(x, y)
    #show_data(x_test, y_test)

