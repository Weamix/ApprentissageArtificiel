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

    def generate_matrix(self, matrix_size):
        dimension = (matrix_size, matrix_size)
        m = np.zeros(dimension)
        self.add_rhums_in_map(m)
        self.adding_tresor_in_map(m)
        return m

    def add_rhums_in_map(self, m):
        for i in range(NUMBER_RHUM):
            r, c = self.choose_random_point_in_map()
            m[r, c] = 2

    def adding_tresor_in_map(self, m):
        r, c = self.choose_random_point_in_map()
        m[r, c] = 10

    def choose_random_point_in_map(self):
        random_row = np.random.choice(range(0, MATRIX_SIZE))
        random_column = np.random.choice(range(0, MATRIX_SIZE))
        return random_column, random_row

    # return neighbors index in matrix for a position = actions for a state
    def actions_for_state(self, x, y):
        # [(N),(S),(E),(O)]
        return [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

    def sort_neighbours_exclude_elements_out_map(self, neighbors):
        return [i for i in neighbors if MATRIX_SIZE > i[0] >= 0 and MATRIX_SIZE > i[1] >= 0]

    def choose_random_action_in_neighbours(self, neighbors):
        return np.random.choice(range(len(neighbors)))

    def get_all_positions(self):
        positions = []
        for i in range(MATRIX_SIZE):
            for j in range(MATRIX_SIZE):
                positions.append((i, j))
        return positions

    # return values of list of positions in matrix
    def values_for_neighbours_with_negative_elements_out_map(self, matrix, v):
        values = []
        for i in v:
            if 0 <= i[0] < MATRIX_SIZE and 0 <= i[1] < MATRIX_SIZE:
                values.append(matrix[i[0], i[1]])
            else:
                values.append(-1)
        return values

    def matrix_state_action(self):
        states = self.get_all_positions()
        # print("states:", states)
        m = defaultdict(lambda: np.zeros(4))

        for state in states:
            x, y = state
            neighbours = self.actions_for_state(x, y)
            #print("neigbours:", neighbours)
            values_for_neighbours = self.values_for_neighbours_with_negative_elements_out_map(self.matrix, neighbours)
            #print("values_for_neighbours:", values_for_neighbours)
            m[state] = values_for_neighbours

        print("matrice_state_action", m)
        return m

    def state_for_action(self, state, action):
        # "à partir de la position et d'une direction tu renvoies la case d'arrivée"
        if action == "N":
            return state[0], state[1] - 1
        elif action == "S":
            return state[0], state[1] + 1
        elif action == "E":
            return state[0] - 1, state[1]
        elif action == "O":
            return state[0] + 1, state[1]
        else:
            return "Action non valide"
