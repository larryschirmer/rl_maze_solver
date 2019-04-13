import numpy as np
from constants import big_number, action_space


class Agent(object):
    def __init__(self, states, alpha=0.15, exploration_factor=0.2):
        self.stateHistory = [((0, 0), 0)]
        self.alpha = alpha
        self.exploration_factor = exploration_factor
        self.G = {}
        self.initReward(states)

    def initReward(self, states):
        for state in states:
            self.G[state] = np.random.uniform(low=-1.0, high=1.0)

    def chooseAction(self, state, allowedMoves):
        max_g = -big_number
        next_move = None
        random_n = np.random.random()

        if random_n < self.exploration_factor:
            next_move = np.random.choice(allowedMoves)
        else:
            for action in action_space:
                new_state = tuple([sum(x)
                                   for x in zip(state, action_space[action])])

                if self.G[new_state] >= max_g:
                    next_move = action
                    max_g = self.G[new_state]

        return next_move

    def updateStateHistory(self, state, reward):
        self.stateHistory.append((state, reward))

    def learn(self):
        target = 0

        for prev, reward in reversed(self.stateHistory):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward

        # slowly decrease the agents preference to explore
        self.exploration_factor -= big_number
        # reset the state history
        self.stateHistory = []
