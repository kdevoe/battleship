# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Main file to run the battleship program.


from board import Board
from agent import Agent
from test import Test
from random import randint, seed

# Make a shipList (this can be updated per run)
shipList = [(5, "Ca"), (4, "Ba"), (3, "Cr"), (3, "Su"), (2, "De")]


if __name__ == '__main__':
    # Build and print a test board
    board = Board(shipList, 10)

    agent1 = Agent(board)

    test = Test(agent1, board)

    print(test.rand_genes(-10, 10))
    print(test.run(1, 1))
