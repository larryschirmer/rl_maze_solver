import numpy as np
from constants import action_space, maze_configuration


class Maze(object):
    def __init__(self, maze_configuration):
        self.maze = maze_configuration
        self.robot_position = (0, 0)
        self.allowed_states = {}
        self.steps = 0
        self.constructAllowedStates()

    def printMaze(self):
        print('- - - - - - - - - - - - - - - - - - - - -')
        for row in self.maze:
            for col in row:
                if col == 0:
                    print('.', end='\t')
                elif col == 1:
                    print('X', end='\t')
                elif col == 2:
                    print('R', end='\t')

            print('\n')
        print('- - - - - - - - - - - - - - - - - - - - -')

    def isAllowedMove(self, state, action):
        y, x = state
        y += action_space[action][0]
        x += action_space[action][1]

        if y < 0 or x < 0 or y > 5 or x > 5:
            return False

        if self.maze[y, x] == 0 or self.maze[y, x] == 2:
            return True
        else:
            return False

    def constructAllowedStates(self):
        allowed_states = {}

        for y, row in enumerate(self.maze):
            for x, _col in enumerate(row):
                if self.maze[(y, x)] != 1:
                    allowed_states[(y, x)] = []

                    for action in action_space:
                        if self.isAllowedMove((y, x), action):
                            allowed_states[(y, x)].append(action)

        self.allowed_states = allowed_states

    def updateMaze(self, action):
        y, x = self.robot_position
        self.maze[y, x] = 0
        y += action_space[action][0]
        x += action_space[action][1]
        self.robot_position = (y, x)
        self.maze[y, x] = 2
        self.steps += 1

    def isGameOver(self):
        if self.robot_position == (5, 5):
            return True
        else:
            return False

    def getStateAndReward(self):
        reward = self.giveReward()
        return self.robot_position, reward

    def giveReward(self):
        if self.robot_position == (5, 5):
            return 0
        else:
            return -1
