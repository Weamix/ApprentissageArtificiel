import numpy as np
import island
import pirate
from collections import defaultdict

GAMMA = 0.9


class Agent():
    def __init__(self, gamma=GAMMA):
        self.gamma = GAMMA
        self.Q = defaultdict(lambda: np.zeros(4))

    def calculate_q(self, state, action: int):
        directions = ["N", "E", "S", "W"]
        r = island.matrix_state_action()

        new_state = island.state_for_action(state, directions[action])

        self.Q[state][action] = r[state][action] + self.gamma * np.argmax(self.Q[new_state])

        return new_state

    def q_learning(self, island):
        new_state = self.calculate_q((0, 0), 1)
        print(new_state)


if __name__ == '__main__':
    island = island.Island()
    # pirate = pirate.Pirate(island)
    print(island.matrix)
    print("tresor position:", island.tresor)
    agent = Agent()
    agent.q_learning(island)
