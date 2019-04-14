import numpy as np

big_number = 10e15

action_space = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, 1),
    'R': (0, 1)
}

maze_configuration = np.array([
    [2, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
])

ascii_pixel = {
    0: '.',
    2: "'",
    4: '`',
    6: '^',
    8: ',',
    10: ':',
    12: ';',
    14: 'I',
    16: '!',
    18: 'i',
    20: '>',
    22: '<',
    24: '+',
    26: '_',
    28: '-',
    30: '[',
    32: '}',
    34: '{',
    36: '1',
    38: '(',
    40: '|',
    42: '\\',
    44: 'f',
    46: 'j',
    48: 'r',
    50: 'x',
    52: 'u',
    54: 'v',
    56: 'c',
    58: 'Y',
    60: 'U',
    62: 'J',
    64: 'C',
    66: 'Q',
    68: '0',
    70: 'O',
    72: 'w',
    74: 'q',
    76: 'p',
    78: 'd',
    80: 'k',
    82: 'h',
    84: 'a',
    86: '#',
    88: 'M',
    90: 'W',
    92: '&',
    94: '%',
    96: 'B',
    98: '@',
    100: '$',
}


class AsciiPixel(object):
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def getPixel(self, value):
        rank = round(((value - self.min) / (self.max - self.min)) * 100)
        rank = rank + 1 if rank % 2 else rank
        return ascii_pixel[rank]
