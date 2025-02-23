#search.py
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    # Create a stack to hold the states
    stack = util.Stack()
    # Push the start state to the stack
    stack.push((start, []))
    # Create a set to hold the visited states
    visited = set()
    while not stack.isEmpty():
        # Pop the state from the stack
        state, actions = stack.pop()
        # If the state is not in the visited set, add it to the visited set
        if state not in visited:
            visited.add(state)
            # If the state is the goal state, return the actions
            if problem.isGoalState(state):
                return actions
            # Get the successors of the state
            successors = problem.getSuccessors(state)
            # For each successor, push it to the stack
            for successor in successors:
                stack.push((successor[0], actions + [successor[1]]))
    return []

    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    # Create a queue to hold the states
    queue = util.Queue()
    # Push the start state to the queue
    queue.push((start, []))
    # Create a set to hold the visited states
    visited = set()
    while not queue.isEmpty():
        # Pop the state from the queue
        state, actions = queue.pop()
        # If the state is not in the visited set, add it to the visited set
        if state not in visited:
            visited.add(state)
            # If the state is the goal state, return the actions
            if problem.isGoalState(state):
                return actions
            # Get the successors of the state
            successors = problem.getSuccessors(state)
            # For each successor, push it to the queue
            for successor in successors:
                queue.push((successor[0], actions + [successor[1]]))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Create a priority queue to hold the states
    pq = util.PriorityQueue()
    # Push the start state to the priority queue
    pq.push((problem.getStartState(), []), 0)
    # Create a set to hold the visited states
    visited = set()
    while not pq.isEmpty():
        # Pop the state from the priority queue
        state, actions = pq.pop()
        # If the state is not in the visited set, add it to the visited set
        if state not in visited:
            visited.add(state)
            # If the state is the goal state, return the actions
            if problem.isGoalState(state):
                return actions
            # Get the successors of the state
            successors = problem.getSuccessors(state)
            # For each successor, push it to the priority queue
            for successor in successors:
                pq.push((successor[0], actions + [successor[1]]), problem.getCostOfActions(actions + [successor[1]]))
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
  
    start = problem.getStartState()
    # Create a priority queue to hold the states
    pq = util.PriorityQueue()
    # Push the start state to the priority queue
    pq.push((start, []), 0)
    # Create a set to hold the visited states
    visited = set()
    while not pq.isEmpty():
        # Pop the state from the priority queue
        state, actions = pq.pop()
        # If the state is not in the visited set, add it to the visited set
        if state not in visited:
            visited.add(state)
            # If the state is the goal state, return the actions
            if problem.isGoalState(state):
                return actions
            # Get the successors of the state
            successors = problem.getSuccessors(state)
            # For each successor, push it to the priority queue
            for successor in successors:
                pq.push((successor[0], actions + [successor[1]]), problem.getCostOfActions(actions + [successor[1]]) + heuristic(successor[0], problem))
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
