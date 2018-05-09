# Eight-Puzzle Generator and Solver
### Author: David Kim

This Python program features a tkinter user interface that allows users to generate random eight-puzzles and solve them with their choice of search algorithm. Once a solution has been found, the program will display statistics such as time elapsed for the search, number of nodes expanded, and number of moves required.

Here is a screenshot of the program:
![alt text](https://github.com/sdkavid/eightPuzzleSearch/src/img/screenshot.png "Screenshot")

As of **5/8/2018**, the following search algorithms have been implemented:  
1. Depth-first Search
2. Breadth-first Search

And the following search algorithms are planned to be added:  
3. Uniform-cost Search
4. Greedy Best-first Search
5. A* Search [Manhattan Distance Heuristic]
6. Recursive Best-first Search

**Some algorithms are inherently slow to find a solution. Please be patient if you choose such algorithms.**

Further notes:  
  * Only solvable eight-puzzles will be generated. This is done with a check on the number of inversions in the input state of the puzzle.
  * The selection of search algorithms is accessible using a dropdown menu.
  * Currently, you can run the program using main.py, but I plan to create a Windows executable in the near future.