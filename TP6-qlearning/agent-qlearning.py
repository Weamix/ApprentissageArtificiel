import numpy as np
import island
import pirate
from collections import defaultdict

GAMMA = 0.9
EPISODES = 100


class Agent:
    def __init__(self, gamma=GAMMA):
        self.gamma = GAMMA
        self.Q = defaultdict(lambda: np.zeros(4))

    def calculate_q(self, state, action: int):
        r = island.matrix_state_action()

        new_state = island.state_for_action(state, action)

        self.Q[state][action] = r[state][action] + self.gamma * np.argmax(self.Q[new_state])

        return new_state

    def episode(self, pirate):
        print("initial state : ", pirate.position)
        initial_action = np.random.randint(0, 4)
        print("initial action : ", initial_action)

        while not pirate.found_tresor(island):
            self.calculate_q(pirate.position, initial_action)

    def episodes(self, pirate):
        for episode in range(EPISODES):
            print("Epsiode n°", episode)
            self.episode(pirate)

    def q_learning(self, island, pirate):
        """
        print("initial state : ", pirate.position)
        initial_action = np.random.randint(0, 4)
        print("initial action : ", initial_action)
        new_state = self.calculate_q(pirate.position, initial_action)
        print("new state : ", new_state)"""

        self.episodes(pirate)

        while not pirate.found_tresor(island):
            max_action = np.argmax(self.Q[pirate.position])
            pirate.move_to_state(max_action)

        if pirate.found_tresor(island):
            print("\ntresor found !!!")


if __name__ == '__main__':
    island = island.Island()
    pirate = pirate.Pirate(island)
    print(island.matrix)
    print("tresor position:", island.tresor)
    agent = Agent()
    agent.q_learning(island, pirate)
