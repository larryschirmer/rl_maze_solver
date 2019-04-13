import numpy as np

maze_configuration = np.array([
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
])


class Maze(object):
    def __init__(self, maze_configuration):
        self.maze = maze_configuration
        self.robot_position = (0, 0)

    def printMaze(self):
        pass

    def isAllowedMove(self, state, action):
        pass

    def updateMaze(self, action):
        pass

    def isGameOver(self):
        pass

    def getState(self):
        pass

    def giveReward(self):
        pass
