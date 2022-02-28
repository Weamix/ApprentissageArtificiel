import numpy as np

MATRIX_SIZE = 3
NUMBER_RHUM = 5


class Island:

    def __init__(self, matrix_size=MATRIX_SIZE):
        # 0 = case vide, 2 = rhum et 10 = tresor
        m = self.generate_matrix(matrix_size)
        self.matrix = m
        self.tresor = np.where(m == 10)
        self.number_rhum = NUMBER_RHUM

    def generate_matrix(self,matrix_size):
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

    # return neighbors index in matrix for a position
    def neighbors_for_position(self, x, y):
        n = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [i for i in n if 0 <= i[0] < MATRIX_SIZE and 0 <= i[1] < MATRIX_SIZE]

    # return values of list of positions in matrix
    def values_for_neighbors(self, matrix, v):
        return [matrix[i[0], i[1]] for i in v]

