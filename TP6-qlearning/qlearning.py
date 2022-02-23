import numpy as np
from itertools import product, starmap, islice

MATRIX_SIZE = 5
NUMBER_RHUM = 5


class Island:

    def __init__(self, matrix_size=MATRIX_SIZE):
        # 0 = case vide, 2 = rhum et 10 = tresor
        m = generate_matrix(matrix_size)
        self.matrix = m
        self.tresor = np.where(m == 10)


def generate_matrix(matrix_size):
    dimension = (matrix_size, matrix_size)
    m = np.zeros(dimension)
    adding_tresor_in_map(m)
    adding_rhums_in_map(m)
    return m


def adding_tresor_in_map(m):
    r, c = choose_random_point_in_map()
    m[r, c] = 10


def adding_rhums_in_map(m):
    for i in range(NUMBER_RHUM):
        r, c = choose_random_point_in_map()
        if m[r, c] == 10:
            r, c = choose_random_point_in_map()
        else:
            m[r, c] = 2


def choose_random_point_in_map():
    random_row = np.random.choice(range(1, MATRIX_SIZE))
    random_column = np.random.choice(range(1, MATRIX_SIZE))
    return random_row, random_column


def e_greedy(matrix, tresor_position):
    starting_position = choose_random_point_in_map()
    print("starting_position", starting_position)
    n = np.random.uniform(0, 1)
    number_moved = 0

    while number_moved != 1:
        if n < 0.9:
            # déplacement vers le meilleur des voisins
            v = list(find_neighbors(matrix, starting_position[0], starting_position[1]))
            print("neighbors : ", v)
        else:
            pass
            # random parmi les voisins possibles

        number_moved = number_moved + 1
        if starting_position == tresor_position:
            break


def find_neighbors(matrix, x, y):
    xi = (0, -1, 1) if 0 < x < len(matrix) - 1 else ((0, -1) if x > 0 else (0, 1))
    yi = (0, -1, 1) if 0 < y < len(matrix[0]) - 1 else ((0, -1) if y > 0 else (0, 1))
    return islice(starmap((lambda a, b: matrix[x + a][y + b]), product(xi, yi)), 1, None)


def q_learning():
    pass


def monte_carlo():
    pass


if __name__ == '__main__':
    island = Island()
    print(island.matrix)
    print("tresor position:", island.tresor)
    e_greedy(island.matrix, island.tresor)
