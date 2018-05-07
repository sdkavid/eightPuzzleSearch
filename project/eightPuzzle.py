from random import shuffle

import search

class EightPuzzle:

    def __init__(self, numbers=None):
        self.cells = []
        if numbers == None:
            numbers = list(range(0,9))
            shuffle(numbers)
        else:
            numbers = numbers[:]
        for row in range(3):
            self.cells.append([])
            for col in range(3):
                self.cells[row].append(numbers.pop())
                if self.cells[row][col] == 0:
                    self.blankCell = row, col

    def __str__(self):
        return str(self.cells)


    def __repr__(self):
        return ("EightPuzzle: %s" %(str(self.cells)))


    def __eq__(self, other):
        for row in range(3):
            if self.cells[row] != other.cells[row]:
                return False
        return True

    def __hash__(self):
        """Need to make EightPuzzle hashable for search
        algorithm implementations.
        """
        return hash(str(self.cells))

    def isSolvable(self):
        """Checks if the 8-puzzle is actually solvable, by
        checking the number of inversions in the input state.
        """
        array = str(self)
        deleted = str.maketrans(dict.fromkeys("[,]"))
        array = array.translate(deleted)
        array = array.split(" ")
        array = [int(num) for num in array]
        print(array)

        inversions = 0
        x = 0
        while x < 8:
            if (array[x] != 0):
                y = x+1
                while y < 9:
                    if (array[y] != 0):
                        if (array[x] > array[y]):
                            inversions += 1
                    y += 1
            x += 1

        if (inversions % 2) == 1:
            print(inversions)
            return False
        else:
            print(inversions)
            return True

    def isGoal(self):
        cell = 0
        for row in range(3):
            for col in range(3):
                if cell != self.cells[row][col]:
                    return False
                cell += 1
        return True

    def legalMoves(self):
        moves = []
        row, col = self.blankCell
        if row != 0:
            moves.append("up")
        if row != 2:
            moves.append("down")
        if col != 0:
            moves.append("left")
        if col != 2:
            moves.append("right")
        return moves

    def successor(self, move):
        row, col = self.blankCell
        if move == "up":
            newrow = row - 1
            newcol = col
        elif move == "down":
            newrow = row + 1
            newcol = col
        elif move == "left":
            newrow = row
            newcol = col - 1
        else:
            newrow = row
            newcol = col+1

        newPuzzle = EightPuzzle([0, 0, 0, 0, 0, 0, 0, 0, 0])
        newPuzzle.cells = [values[:] for values in self.cells]

        newPuzzle.cells[row][col] = self.cells[newrow][newcol]
        newPuzzle.cells[newrow][newcol] = self.cells[row][col]
        newPuzzle.blankCell = newrow, newcol

        return newPuzzle


class EightPuzzleSearchProblem(search.SearchProblem):

    def __init__(self, puzzle):
        self.state = puzzle

    def getStartState(self):
        return self.state

    def isGoalState(self, state):
        return state.isGoal()

    def getSuccessors(self, state):
        successors = []
        for move in state.legalMoves():
            successors.append((state.successor(move), move, 1))
        return successors

    def getCostOfActions(self, actions):
        return len(actions)