import tkinter as tk

import eightPuzzle
import search
import util

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.algorithm = None
        self.renderCommands()
        self.puzzle = None
        self.newPuzzle()
        self.currentState = 0
        self.solution = None
        self.stateHistory = None

    def renderState(self, puzzle):
        """Create a 3x3 visual table representing the 8-puzzle.
        
        Takes the eightPuzzle.EightPuzzle class object as an argument.
        """
        puzzle = str(puzzle)
        deleted = str.maketrans(dict.fromkeys("[,]"))
        puzzle = puzzle.translate(deleted)
        puzzle = puzzle.split(" ")
        #print(puzzle)
        self.index = 0
        for row in range(3):
            for column in range(3):
                if puzzle[self.index] != "0":
                    cell = tk.Label(self, text=puzzle[self.index],
                                    font=("Arial", 20),
                                    relief="ridge",
                                    padx=10
                                    )
                    cell.grid(row=(row+3), column=(column+8))
                    self.index += 1
                else:
                    cell = tk.Label(self, text="0",
                                    font=("Arial", 20),
                                    relief="ridge",
                                    padx=10,
                                    fg="#f0f0f0"
                                    )
                    cell.grid(row=(row+3), column=(column+8))
                    self.index +=1

    def renderCommands(self):
        """Set up all the UI buttons and menus.

        """
        self.intro = tk.Label(self, text= (
            "Please select a search algorithm to solve this "
            "eight puzzle problem.")
            )
        self.intro.grid(row=1, column=1, columnspan=5, padx=10, pady=10)

        self.intro2 = tk.Label(self, text="Algorithm:")
        self.intro2.grid(row=2, column=1)

        self.options = [
            "Depth-first Search",
            "Breadth-first Search",
            "Uniform-cost Search",
            "Greedy Best-first Search",
            "A* Search [Manhattan Dist.]",
            "Recursive Best-first Search"
            ]
        self.algorithm = tk.StringVar(self)
        self.algorithm.set(self.options[0])  # default value
        self.option = tk.OptionMenu(self, self.algorithm, *self.options)
        self.option.grid(row=2, column=2, columnspan=3,
                         sticky="w")

        self.solve = tk.Button(self, text="Solve",
                               command=self.solve, padx=12)
        self.solve.grid(row=2, column=5)

        self.previous = tk.Button(self, text="Previous",
                                  command=self.previous)
        self.previous.grid(row=11, column=2)

        self.next = tk.Button(self, text="Next",
                              command=self.next, padx=12)
        self.next.grid(row=11, column=3)

        self.new = tk.Button(self, text="New Puzzle",
                             command=self.newPuzzle)
        self.new.grid(row=12, column=2, columnspan=2, pady=10)

        self.border = tk.Label(self, text=" ")
        self.border.grid(row=1, column=12, padx=10)

        self.botBorder = tk.Label(self, text=" ")
        self.botBorder.grid(row=14, column=1, pady=10)

    def clearStats(self):
        """Clear the solution information widgets from the grid.

        """
        for label in self.grid_slaves():
            if (int(label.grid_info()["row"]) > 2):
                if (int(label.grid_info()["row"]) < 6):
                    if (int(label.grid_info()["column"]) == 1):
                        label.grid_forget()

    def clearSteps(self):
        """Clear the current state counter widget from the grid.

        """
        for label in self.grid_slaves():
            if (int(label.grid_info()["row"]) == 13):
                label.grid_forget()

    def previous(self):
        """Render the previous step in the 8-puzzle solution.

        """
        if self.currentState == 0:
            pass
        else:
            self.clearSteps()
            newState = int(self.currentState - 1)
            self.renderState(self.stateHistory[newState])
            self.currentState = newState

            self.counter = tk.Label(self, text="Currently on step %s of %s."
                %(newState, (len(self.solution[0]) - 1))
                )
            self.counter.grid(row=13, column=1, columnspan=5, padx=5, pady=5)


    def next(self):
        """Render the next step in the 8-puzzle solution.
        
        """
        if self.currentState == (len(self.solution[0]) - 1):
            pass
        else:
            self.clearSteps()
            newState = int(self.currentState + 1)
            self.renderState(self.stateHistory[newState])
            self.currentState = newState

            self.counter = tk.Label(self, text="Currently on step %s of %s."
                %(newState, (len(self.solution[0]) - 1))
                )
            self.counter.grid(row=13, column=1, columnspan=5, padx=5, pady=5)

    def newPuzzle(self):
        """Generate a new 8-puzzle, render it, and set as the game's puzzle.
        """
        newPuzzle = eightPuzzle.EightPuzzle()
        if newPuzzle.isSolvable() is False:
            while newPuzzle.isSolvable() is False:
                print("puzzle is not solvable!")
                newPuzzle = eightPuzzle.EightPuzzle()

        self.renderState(newPuzzle)
        self.puzzle = newPuzzle
        self.clearStats()
        self.clearSteps()

    def solve(self):
        """Solve the current 8-puzzle using the selected algorithm.

        """
        self.clearStats()

        self.problem = eightPuzzle.EightPuzzleSearchProblem(self.puzzle)
        searchAlgorithm = self.algorithm.get()
        if searchAlgorithm == "Depth-first Search":
            self.solution = search.depthFirstSearch(self.problem)
            self.stateHistory = self.solution[3]
        elif searchAlgorithm == "Breadth-first Search":
            self.solution = search.breadthFirstSearch(self.problem)
            self.stateHistory = self.solution[3]
            pass
        elif searchAlgorithm == "Uniform-cost Search":
            self.solution = search.uniformCostSearch(self.problem)
            self.stateHistory = self.solution[3]
            pass
        elif searchAlgorithm == "Greedy Best-first Search":
            #self.solution = search.greedyBestFirstSearch(self.problem)
            #self.stateHistory = self.solution[3]
            pass
        elif searchAlgorithm == "A* Search [Manhattan Dist.]":
            #self.solution = search.aStarSearch(self.problem)
            #self.stateHistory = self.solution[3]
            pass
        else:
            #self.solution = search.recursiveBestFirstSearch(self.problem)
            #self.stateHistory = self.solution[3]
            pass

        self.stats = tk.Label(self, text= (
                "A solution was found in %.3f seconds and requires %s moves."
                %(
                    self.solution[2],
                    (len(self.solution[0]) - 1)
                    )
                )
            )
        self.stats.grid(row=3, column=1, columnspan=5)

        self.stats2 = tk.Label(self, text= (
                "%s nodes were expanded during the search."
                %(len(self.solution[1]))
                )
            )
        self.stats2.grid(row=4, column=1, columnspan=5)

        self.stepInfo = tk.Label(self, text= (
            "Use Previous and Next to show the solution moves.")
            )
        self.stepInfo.grid(row=5, column=1, columnspan=5, padx=5, pady=5)



root = tk.Tk()
app = Application(master=root)
app.master.title("Eight Puzzle Search")
app.mainloop()