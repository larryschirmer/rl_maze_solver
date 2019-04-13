import numpy as np

big_number = 10e15

action_space = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, 1),
    'R': (0, 1)
}

maze_configuration = np.array([
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
])
