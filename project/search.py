from time import time

import util

class SearchProblem:
    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


class Node:
    def __init__(self, state=None, parent=None, action=None, cost=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __str__(self):
        return str(self.state)


    def __repr__(self):
        return ("Node: %s" %(str(self.state)))



def depthFirstSearch(problem):
    """Depth-first search algorithm
    Graph implementation - complete.
    """
    startTime = time()
    solution = []
    stateHistory = []

    # node = (xy-coord, parent node, direction from parent to node, cost)
    node = Node(problem.getStartState(), None, None, None)

    fringe = util.Stack()
    fringe.push(node)
    explored = set()

    while True:
        if fringe.isEmpty():
            return
        node = fringe.pop()
        if problem.isGoalState(node.state):
            while node.state != problem.getStartState():
                solution.append(node.action)
                stateHistory.append(node)
                node = node.parent
            solution.reverse()
            stateHistory.reverse()
            endTime = time()
            elapsedTime = endTime - startTime
            return solution, explored, elapsedTime, stateHistory
        explored.add(node.state)
        for neighbor in problem.getSuccessors(node.state):
            child = Node(neighbor[0], node, neighbor[1], neighbor[2])
            if (child.state not in explored):
                fringe.push(child)


def breadthFirstSearch(problem):
    """Breadth-first search algorithm

    """
    startTime = time()
    solution = []
    stateHistory = []

    # node = (xy-coord, parent node, direction from parent to node, cost)
    node = Node(problem.getStartState(), None, None, None)

    fringe = util.Queue()
    fringe.push(node)
    explored = set()

    while True:
        if fringe.isEmpty():
            return
        node = fringe.pop()
        if problem.isGoalState(node.state):
            while node.state != problem.getStartState():
                solution.append(node.action)
                stateHistory.append(node)
                node = node.parent
            solution.reverse()
            stateHistory.reverse()
            endTime = time()
            elapsedTime = endTime - startTime
            return solution, explored, elapsedTime, stateHistory
        explored.add(node.state)
        for neighbor in problem.getSuccessors(node.state):
            child = Node(neighbor[0], node, neighbor[1], neighbor[2])
            if (child.state not in explored):
                fringe.push(child)


def uniformCostSearch(problem):
    """Uniform cost search algorithm

    """
    startTime = time()
    solution = []
    stateHistory = []

    # node = (xy-coord, parent node, direction from parent to node, cost)
    node = Node(problem.getStartState(), None, None, 0)

    fringe = util.PriorityQueue()
    fringe.push(node, 0)
    explored = set()

    while True:
        if fringe.isEmpty():
            return
        node = fringe.pop()
        if problem.isGoalState(node.state):
            while node.state != problem.getStartState():
                solution.append(node.action)
                stateHistory.append(node)
                node = node.parent
            solution.reverse()
            stateHistory.reverse()
            endTime = time()
            elapsedTime = endTime - startTime
            return solution, explored, elapsedTime, stateHistory
        explored.add(node.state)
        for neighbor in problem.getSuccessors(node.state):
            child = Node(neighbor[0], node, neighbor[1], neighbor[2]+node.cost)
            if (child.state not in explored):
                fringe.push(child, child.cost)
            else:
                # if child.state is in fringe with higher path cost
                # replace that fringe node with child
                pass


def greedyBestFirstSearch(problem):
    pass


def aStarSearch(problem):
    pass


def recursiveBestFirstSearch(problem):
    pass