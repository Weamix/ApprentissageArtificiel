import island
import numpy as np

GAMMA = 0.9


def e_greedy(matrix, tresor_position):
    starting_position = island.choose_random_point_in_map()
    print("starting_position : ", starting_position)
    random = np.random.uniform(0, 1)
    number_moved = 0
    current_position = starting_position

    while number_moved != 20:
        n = island.neighbors_for_position(current_position[0], current_position[1])
        print("n :", n)
        neighbors = island.sort_neighbors_exclude_elements_out_map(n)
        print("neighbors sorted:", neighbors)
        values = island.values_for_neighbors(matrix, neighbors)
        print("values :", values)
        if random > 0.9:
            # déplacement vers le meilleur des voisins
            maximum = max(values)
            print("maximum :", maximum)
            index = values.index(maximum)
            print("index best :", index)
        else:
            # random parmi les voisins possibles
            random_value = island.choose_random_action_in_neigbors(neighbors)
            print("random_value :", random_value)
            index = random_value
            print("index random :", index)

        current_position = neighbors[index]
        print("current_position : ", current_position)
        number_moved += 1

        if starting_position == tresor_position:
            print("tresor found")
            break

    print("number_moved : ", number_moved)


def q_learning():
    island.matrice_state_action()


def monte_carlo():
    pass


if __name__ == '__main__':
    island = island.Island()
    print(island.matrix)
    print("tresor position:", island.tresor)
    #e_greedy(island.matrix, island.tresor)
    q_learning()

