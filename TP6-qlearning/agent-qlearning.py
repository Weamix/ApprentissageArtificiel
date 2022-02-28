import numpy as np
import island
import pirate
from collections import defaultdict

GAMMA = 0.9


class Agent():
    def __init__(self, gamma=GAMMA):
        self.gamma = GAMMA
        self.Q = defaultdict(lambda: np.zeros(4))


def q_learning(island):
    island.matrice_state_action()


if __name__ == '__main__':
    island = island.Island()
    #pirate = pirate.Pirate(island)
    print(island.matrix)
    print("tresor position:", island.tresor)
    q_learning(island)
