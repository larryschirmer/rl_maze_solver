import numpy as np


class Agent(object):
    def __init__(self, states, alpha):
        self.stateHistory = None
        self.alpha = alpha
        self.G = {}
        self.initReward(states)

    def initReward(self, states):
        for state in states:
            self.G[state] = np.random.uniform(low=-1.0, high=1.0)

    def learn(self):
        target = 0

        for prev, reward in reversed(self.stateHistory):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward
        
        self.stateHistory = []

    def chooseAction(self):
        pass

    def updateStateHistory(self):
        pass
