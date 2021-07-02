# Author: Ken DeVoe
# Date: 7/2/2021
# Description: Class that represents the game board of battleship.

from random import sample, randint, choice

class Board:
    """
    Represents a battleship board. Defaults to a 10 x 10 board size unless input otherwise.
    """

    def __init__(self, shipList, size=10):
        self._shipList = shipList
        self._size = size

        # Make a 2D board of input size initializing all values to false for empty
        self._board = []
        for row in size:
            self._board.append([])
            for col in size:
                self._board[row].append(False)

    def place_ships(self):
        ship_order = sample(self._shipList)

        for ship in ship_order:
            valid = False
            while not valid:
                valid = True

                # Initialize start location and ship direction randomly
                row = randint(0, self._size - 1)
                col = randint(0, self._size - 1)
                row_dir = randint(-1, 1)
                if row_dir != 0:
                    col_dir = 0
                else:
                    col_dir = choice([-1, 1])

                # Check if ship would fit on the board
                for i in ship[0]:
                    if row + row_dir*i < 0 or row + row_dir*i >= self._size:
                        valid = False
                    if col + col_dir*i < 0 or col + col_dir*i >= self._size:
                        valid = False

                # Check if target location is open
                i = 0
                while valid and i < ship[0]:
                    if row + row_dir * i :
                            valid = False
                        if col + col_dir * i < 0 or col + col_dir * i >= self._size:
                            valid = False
                    i += 1

        pass

    def get_square(self, row, col):
        return self._board[row][col]


    def print_board(self):
        for row in self._board:
            print(row)

