from search import *

# Puzzle as a tuple
initial_state = (1, 2, 3, 5, 7, 4, 8, 6, 0)

# Create the puzzle problem instance
eight_puzzle = EightPuzzle(initial_state)

# Solve using A* (without a heuristic) and display expanded nodes
print(astar_search(eight_puzzle, h=None, display=True).solution())
