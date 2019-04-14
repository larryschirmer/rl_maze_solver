import numpy as np
from environment import Maze
from agent import Agent
import matplotlib.pyplot as plt
from constants import maze_configuration

if __name__ == '__main__':
    maze = Maze(maze_configuration)
    robot = Agent(maze.allowed_states, alpha=0.1, exploration_factor=0.25)
    move_history = []
    robot.printRewardMap()

    for episode in range(5000):
        if episode % 1000 == 0:
            print(episode)
            robot.printRewardMap()

        while not maze.isGameOver():
            state, _ = maze.getStateAndReward()
            action = robot.chooseAction(state, maze.allowed_states[state])

            maze.updateMaze(action)

            state, reward = maze.getStateAndReward()
            robot.updateStateHistory(state, reward)
            if maze.steps > 1000:
                maze.robot_position = (5, 5)
            
        robot.learn()
        move_history.append(maze.steps)
        maze = Maze(maze_configuration)
