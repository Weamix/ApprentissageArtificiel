import numpy as np
from collections import defaultdict

MATRIX_SIZE = 3
NUMBER_RHUM = 5


class Island:

    def __init__(self, matrix_size=MATRIX_SIZE):
        # 0 = case vide, 2 = rhum et 10 = tresor
        m = self.generate_matrix(matrix_size)
        self.matrix = m
        self.tresor = np.where(m == 10)
        self.number_rhum = NUMBER_RHUM

    def generate_matrix(self, matrix_size):
        dimension = (matrix_size, matrix_size)
        m = np.zeros(dimension)
        self.adding_tresor_in_map(m)
        self.adding_rhums_in_map(m)
        return m

    def adding_tresor_in_map(self, m):
        r, c = self.choose_random_point_in_map()
        m[r, c] = 10

    def adding_rhums_in_map(self, m):
        for i in range(NUMBER_RHUM):
            r, c = self.choose_random_point_in_map()
            while m[r, c] == 10:
                r, c = self.choose_random_point_in_map()
            m[r, c] = 2

    def choose_random_point_in_map(self):
        random_row = np.random.choice(range(1, MATRIX_SIZE))
        random_column = np.random.choice(range(1, MATRIX_SIZE))
        return random_row, random_column

    # return neighbors index in matrix for a position = actions for an state
    def neighbors_for_position(self, x, y):
        # n= [(N),(S),(E),(O)]
        n = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
        return n

    def sort_neighbors_exclude_elements_out_map(self, neighbors):
        return [i for i in neighbors if 0 <= i[0] < MATRIX_SIZE and 0 <= i[1] < MATRIX_SIZE]

    def choose_random_action_in_neigbors(self, neighbors):
        return np.random.choice(range(len(neighbors)))

    # return values of list of positions in matrix
    def values_for_neighbors(self, matrix, v):
        return [matrix[i[0], i[1]] for i in v]

    def get_all_positions(self):
        positions = []
        for i in range(MATRIX_SIZE):
            for j in range(MATRIX_SIZE):
                positions.append((i, j))
        return positions

    # return values of list of positions in matrix
    def values_for_neighbors_with_negative_elements_out_map(self, matrix, v):
        values = []
        for i in v:
            if 0 <= i[0] < MATRIX_SIZE and 0 <= i[1] < MATRIX_SIZE:
                values.append(matrix[i[0], i[1]])
            else:
                values.append(-1)
        return values

    def matrice_state_action(self):
        states = self.get_all_positions()
        #print("states:", states)
        m = defaultdict(lambda: np.zeros(4))

        for state in states:
            x, y = state
            neighbors = self.neighbors_for_position(x, y)
            #print("neigbors:", neighbors)
            values_for_neighbors = self.values_for_neighbors_with_negative_elements_out_map(self.matrix, neighbors)
            #print("values_for_neighbors:", values_for_neighbors)
            m[state] = values_for_neighbors

        print("matrice_state_action", m)
        return m
