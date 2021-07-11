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

        # Make a 2D board of input size initializing all values to False for open
        self._board = []
        for row in range(size):
            self._board.append([])
            for col in range(size):
                self._board[row].append(False)
        self.place_ships()

    def place_ships(self):
        ship_order = sample(self._shipList, len(self._shipList))

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
                i = 0
                while valid and i < ship[0]:
                    if row + row_dir*i < 0 or row + row_dir*i >= self._size:
                        valid = False
                    if col + col_dir*i < 0 or col + col_dir*i >= self._size:
                        valid = False
                    i += 1

                # Check if target location is open
                i = 0
                while valid and i < ship[0]:
                    if self._board[row + row_dir * i][col + col_dir * i] != False:
                        valid = False
                    i += 1

                # Place the ship if chosen location and orientation is valid
                if valid:
                    for i in range(ship[0]):
                        self._board[row + row_dir * i][col + col_dir * i] = ship[1]

    def reset(self):

        # Wipe the board
        for i in range(self._size):
            for j in range(self._size):
                self._board[i][j] = False

        # Place ships again
        self.place_ships()


    def get_list(self):
        return self._shipList

    def get_square(self, row, col):
        return self._board[row][col]

    def get_size(self):
        return self._size

    def print_board(self):
        for row in self._board:
            print(row)

