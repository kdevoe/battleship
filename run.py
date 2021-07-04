# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Main file to run the battleship program.


from board import Board
from agent import Agent

# Make a shipList
shipList = [(5, "Ca"), (4, "Ba"), (3, "Cr"), (3, "Su"), (2, "De")]


if __name__ == '__main__':
    # Build and print a test board
    board = Board(shipList, 10)
    board.place_ships()
    board.print_board()

    agent1 = Agent(board)
    print(agent1.check_done())

