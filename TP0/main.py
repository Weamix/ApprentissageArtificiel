import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([[6], [8], [10], [14], [18]])
y = [7, 9, 13, 17.5, 18]

if __name__ == '__main__':
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

    plt.show()
