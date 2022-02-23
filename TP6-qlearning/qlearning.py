import numpy as np

MATRIX_SIZE = 5
NUMBER_RHUM = 5


class Island:

    def __init__(self, matrix_size=MATRIX_SIZE):
        # 0 = case vide, 2 = rhum et 10 = tresor
        dimension = (matrix_size, matrix_size)
        m = np.zeros(dimension)

        adding_tresor_in_map(m)
        adding_rhums_in_map(m)

        self.matrix = m

        for value in self.matrix:
            #print(value)
            pass


def adding_tresor_in_map(m):
    r, c = choose_random_point_in_map()
    m[r, c] = 10


def adding_rhums_in_map(m):
    for i in range(NUMBER_RHUM):
        r, c = choose_random_point_in_map()
        m[r, c] = 2

def choose_random_point_in_map():
    random_row = np.random.choice(range(1,MATRIX_SIZE))
    random_column = np.random.choice(range(1,MATRIX_SIZE))
    return random_row,random_column

if __name__ == '__main__':
    island = Island()
    print(island.matrix)
