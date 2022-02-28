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

    def episode(self, pirate):
        print("initial state : ", pirate.position)
        initial_action = np.random.randint(0, 4)
        print("initial action : ", initial_action)

        if not pirate.found_tresor(island):
            new_state = self.calculate_q(pirate.position, initial_action)

        while not pirate.found_tresor(island):
            initial_action = np.random.randint(0, 4)
            self.calculate_q(new_state, initial_action)

    def episodes(self, pirate):
        pass

    def q_learning(self, island, pirate):
        new_state = self.calculate_q((0, 0), 1)
        print("new_state", new_state)
        self.episode(pirate)


if __name__ == '__main__':
    island = island.Island()
    pirate = pirate.Pirate(island)
    print(island.matrix)
    print("tresor position:", island.tresor)
    agent = Agent()
    agent.q_learning(island, pirate)
