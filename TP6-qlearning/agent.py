import numpy as np

GAMMA = 0.9


class Agent:
    def __init__(self, gamma=GAMMA):
        self.gamma = GAMMA
        self.Q = np.zeros()
