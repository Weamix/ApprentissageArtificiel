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
            while m[r, c] != 10:
                r, c = choose_random_point_in_map()
                m[r, c] = 2
        else:
            m[r, c] = 2


def choose_random_point_in_map():
    random_row = np.random.choice(range(1, MATRIX_SIZE))
    random_column = np.random.choice(range(1, MATRIX_SIZE))
    return random_row, random_column


def e_greedy(matrix, tresor_position):
    starting_position = choose_random_point_in_map()
    print("starting_position : ", starting_position)
    random = np.random.uniform(0, 1)
    number_moved = 0

    current_position = starting_position

    while number_moved != 20:
        neighbors = neighbors_for_position(current_position[0], current_position[1])
        print("neighbors :", neighbors)
        values = values_for_neighbors(matrix, neighbors)
        print("values :", values)
        if random > 0.9:
            # déplacement vers le meilleur des voisins
            maximum = max(values)
            print("maximum :", maximum)
            index = values.index(maximum)
            print("index :", index)
        else:
            # random parmi les voisins possibles
            random_value = np.random.choice(range(len(neighbors)))
            print("random_value :", random_value)
            #print("index :", index)

            index = random_value

        current_position = neighbors[index]
        print("current_position : ", current_position)
        number_moved += 1
        if starting_position == tresor_position:
            print("tresor found")
            break
    print("number_moved : ", number_moved)


# return neighbors index in matrix for a position
def neighbors_for_position(x, y):
    n = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [i for i in n if 0 <= i[0] < MATRIX_SIZE and 0 <= i[1] < MATRIX_SIZE]


# return values of list of positions in matrix
def values_for_neighbors(matrix, v):
    return [matrix[i[0], i[1]] for i in v]


def q_learning():
    pass


def monte_carlo():
    pass


if __name__ == '__main__':
    island = Island()
    print(island.matrix)
    print("tresor position:", island.tresor)
    e_greedy(island.matrix, island.tresor)
