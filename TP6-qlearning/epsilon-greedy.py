import island
import pirate
import numpy as np

EPSILON = 0.9


def epsilon_greedy(island, pirate):
    print("starting position : ", pirate.position)
    random = np.random.uniform(0, 1)
    number_moved = 0

    while number_moved != 20 and not pirate.found_tresor(island):
        if random > EPSILON:
            # déplacement vers le meilleur des voisins
            pirate.move_to_best_action(island)
        else:
            # random parmi les voisins possibles
            pirate.move_to_random_action(island)

        number_moved += 1

    if pirate.found_tresor(island):
        print("\ntresor found !!!")
    print("number_moved : ", number_moved)


if __name__ == '__main__':
    island = island.Island()
    pirate = pirate.Pirate(island)
    print(island.matrix)
    print("tresor position:", island.tresor)
    epsilon_greedy(island, pirate)
