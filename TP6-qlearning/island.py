import numpy as np
from itertools import product, starmap, islice

MATRIX_SIZE = 3
NUMBER_RHUM = 5


class Island:

    def __init__(self, matrix_size=MATRIX_SIZE):
        # 0 = case vide, 2 = rhum et 10 = tresor
        m = self.generate_matrix(matrix_size)
        self.matrix = m
        self.tresor = np.where(m == 10)
        self.matrix_size = MATRIX_SIZE
        self.number_rhum = NUMBER_RHUM

    def choose_random_point_in_map(self):
        random_row = np.random.choice(range(1, MATRIX_SIZE))
        random_column = np.random.choice(range(1, MATRIX_SIZE))
        return random_row, random_column

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
            if m[r, c] == 10:
                while m[r, c] != 10:
                    r, c = self.choose_random_point_in_map()
                    m[r, c] = 2
            else:
                m[r, c] = 2
