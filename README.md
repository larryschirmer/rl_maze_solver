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

and the bottom right corner `(5, 5)` is the end of the maze.

### Training the agent and running the model

After cloning the project and installing the environmental dependancies (see below), run `python main.py` to start training.

To start, the robot will not know which direction will lead to a higher reward. As seen in the reward map below, all of the navigable space has a random reward between -1 and 1. This reward space in generated when the agent is instantiated.

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

I know it just looks like random characters around the outline of where the walls should be. What's happening here is the values are being mapped to a dark <-> light ascii character map, so if you squint they should all look to be about the same brightness. It's not impressive, it looks a lot better after the robot has had some time with the environment.

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

What makes this particular machine learning technique special is that teaching a program to solve a problem does not involve a set of rules. Rather, instead of clearly programed instructions for every case, the program learns on its own to solve the problem by maximizing its reward.

## Install Instructions

1. Clone the project

   Navigate to a nice folder in your favorite terminal and run:

   ```txt
    https://github.com/larryschirmer/rl_maze_solver.git
   ```

   Then change into the new directory:

   ```txt
   cd rl_maze_solver
   ```

1. Install Project Dependancies

   I used [conda](https://docs.conda.io/en/latest/) to manage my environment for this project. To create a new environment for the project run:

   ```txt
    conda create --name rl_maze_solver --file spec-file.txt
   ```

   This should use the `spec-file.txt` file to build the same environment I used to develop the project in. To enter the environment, the command will be different depending on the machine (conda will have instructions). For Mac, run:

   ```txt
    source activate rl_maze_solver
   ```

1. Run the Demo

   At this point, the new environment name should be appended to the console:

   ```txt
   (rl_maze_solver) <Computer-Name>:rl_maze_solver username$
   ```

   To start the program, run:

   ```txt
    python main.py
   ```

   Expect to see the five reward maps appear in the console. The whole process is very fast, and should be done in a couple of seconds.

1. Cleanup

   To uninstall the environment, run:

   ```txt
    source deactivate
   ```

   or for Windows I think its just `deactivate`. This will be in the instructions when the environment is built.

   To remove the newly created environment, run:

   ```txt
    conda env remove --name rl_maze_solver
   ```

\*\* If I forgot anything related to conda, the [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) has been helpful to me, and may also be helpful to you.
