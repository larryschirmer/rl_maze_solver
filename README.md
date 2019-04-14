# Maze Solver

## A reinforcement learning demo project

### What is it

A very simple reinforcement learning demo that presents a reward based agent in a 6x6 discrete space maze. The agent can move up, down, left, and right and is rewarded with -1 at each time step. This is the first project in [Reinforcement Learning in Motion](https://www.manning.com/livevideo/reinforcement-learning-in-motion) with a few of my own changes.

#### The Maze

```txt
- - - - - - - - - - - - - - - - - - - - -
R       .       .       .       .       X

.       .       .       .       .       X

.       .       X       X       X       X

.       .       X       .       .       X

.       .       .       .       .       .

X       X       X       X       X       .

- - - - - - - - - - - - - - - - - - - - -
```

where:

- `R` is the robot
- `X` is a wall
- `.` is navigable space

and the bottom right corner `(5, 5)` is the end of the end of the maze.

### Training the agent and running the model

After cloning the project and installing the environmental dependancies (see below), run `python main.py` to start training.

To start, the robot will not know which direction will lead to a higher reward. As seen in the reward map below, all of the navigable space has a random reward between -1 and 1. This reward space in generated when the map is agent is instantiated.

```txt
- - - - - - - - - - - - - - - - - - - - -
k       !       p       d       .

(       }       d       ;       1

$       i

a       c               '       $

I       J       >       '       d       0

                                        [

- - - - - - - - - - - - - - - - - - - - -
```

I know it just looks like random characters around the outline of where the walls should be. What's happening here is the values are being mapped to a dark <-> light ascii character map, so if you squint they should all look to be about the same brightness. It's not impressive, I looks a lot better at the end (and were walking).

The gym is setup to let it make up to 1000 steps to find the end before ending the session because it could just get lost forever in there. After 5000 iterations (its really got it figured out after 2000 though), the agents reward map shows a clear relationship between the navigable space and the most rewarding way to the end.

```txt
- - - - - - - - - - - - - - - - - - - - -
'       $       .       '       '

.       $       '       '       '

'       $

'       $               '       '

'       $       $       $       $       $

                                        $

- - - - - - - - - - - - - - - - - - - - -
```

If you squint, you can see the robots preferred path. Also, `$` signs is the densest character on the [ascii table](http://mewbies.com/geek_fun_files/ascii/ascii_art_light_scale_and_gray_scale_chart.htm). Oh man, I didn't... The most rewarding way to the end of the maze, ah...

What makes the particular machine learning technique special, is that teaching a program to problem does not involve a set of rules. Rather, instead of clearing programed instructions for every case, the program learns on its own to solve the problem by maximizing its reward.

## Install Instructions

1. Clone the project

   Navigate to a nice folder in your favorite terminal and run: `https://github.com/larryschirmer/rl_maze_solver.git`. The change into the new directory: `cd rl_maze_solver`.

1. Install Project Dependancies

   I used [conda](https://docs.conda.io/en/latest/) to manage my environment for this project. To create a new environment for the project run `conda create --name rl_maze_solver --file spec-file.txt`. This should use the `spec-file.txt` file to build the same environment I used to develop the project in. To enter the environment, the command will be different depending on the machine (conda will have instructions). For Mac, run `source activate rl_maze_solver`.

1. Run the Demo

   At this point, the new environment name should be appended to the console:

   ```txt
   (rl_maze_solver) The-MacBook-Pro:rl_maze_solver larryschirmer$
   ```

   run: `python main.py`. Expect to see a five reward maps and an iteration numbers.

1. Cleanup

   To uninstall the environment, run `source deactivate` or for Windows I think its just `deactivate`. This will be in the instructions when the environment is built.

   To remove the newly created environment, run `conda env remove --name rl_maze_solver`

\*\* If I forgot anything related to conda, the [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) has been helpful to me, and may also be helpful to you.
