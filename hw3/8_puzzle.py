from search import *

# Initial state of the puzzle as a tuple
initial_state = (1, 2, 3,
                 5, 7, 4,
                 8, 6, 0)

eight_puzzle = EightPuzzle(initial_state)

if __name__ == '__main__':
    print(breadth_first_graph_search(eight_puzzle).solution())
