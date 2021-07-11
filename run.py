# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Main file to run the battleship program.


from board import Board
from agent import Agent
from random import randint, seed

# Make a shipList (this can be updated per run)
shipList = [(5, "Ca"), (4, "Ba"), (3, "Cr"), (3, "Su"), (2, "De")]


if __name__ == '__main__':
    # Build and print a test board
    board = Board(shipList, 10)

    agent1 = Agent(board)

    for _ in range(1):
        while not agent1.check_done():
            agent1.rand_guess()
            agent1.print_pboard()
            print()
        print(agent1.get_count())
        board.reset()
        agent1.reset()

