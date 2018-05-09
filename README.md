# Eight-Puzzle Generator and Solver
### Author: David Kim

This Python program features a tkinter user interface that allows users to generate random eight-puzzles and solve them with their choice of search algorithm. Once a solution has been found, the program will display statistics such as time elapsed for the search, number of nodes expanded, and number of moves required.

Here is a screenshot of the program:

![alt text](https://raw.githubusercontent.com/sdkavid/eightPuzzleSearch/master/src/img/screenshot.png "Screenshot")

As of **5/8/2018**, the following search algorithms have been implemented:  
1. Depth-first Search
2. Breadth-first Search

And the following search algorithms are planned to be added:  
* Uniform-cost Search
* Greedy Best-first Search
* A* Search [Manhattan Distance Heuristic]
* Recursive Best-first Search

**Some algorithms are inherently slow to find a solution. Please be patient if you choose such algorithms.**

Further notes:  
  * Only solvable eight-puzzles will be generated. This is done with a check on the number of inversions in the input state of the puzzle.
  * The selection of search algorithms is accessible using a dropdown menu.
  * Currently, you can run the program using main.py, but I plan to create a Windows executable in the near future.