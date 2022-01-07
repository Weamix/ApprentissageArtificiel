import numpy as np


def generate_number_between_0_and_1_in_square(x):
    for i in range(x):
        x = np.random.uniform(0, 1, 2)
        if (x[0] + x[1] - 1) > 0:
            tag = 1
        else:
            tag = -1
        return x[0], x[1], tag


def write_points_in_file(x):
    with open("test.txt", "w") as f:
        for x in range(x):
            x1, y1, tag1 = generate_number_between_0_and_1_in_square(1)
            f.write(str(x1) + " " + str(y1) + " " + str(tag1) + "\n")
    with open("train.txt", "w") as f:
        for x in range(x):
            x2, y2, tag2 = generate_number_between_0_and_1_in_square(1)
            f.write(str(x2) + " " + str(y2) + " " + str(tag2) + "\n")


if __name__ == '__main__':
    write_points_in_file(100)