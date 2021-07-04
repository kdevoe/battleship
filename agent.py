# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Class for agent to play the game battleship.


class Agent:
    """
    Represents an agent which plays the game of battleship
    """

    def __init__(self, board):
        self._board = board
        self._guessed = []
        self._count = 0

        # Make an array to hold the status of each ship being searched for
        self._shipStatus = {}
        for ship in board.get_list():
            self._shipStatus[ship[1]] = [False, ship[0], []]

        # Make a probability board initialized to 0
        self._probBoard = []
        for row in range(board.get_size()):
            self._probBoard.append([])
            for col in range(board.get_size()):
                self._probBoard[row].append(0)

        # Make board known by agent of ship locations all initialized to open
        self._knownBoard = []
        for row in range(board.get_size()):
            self._knownBoard.append([])
            for col in range(board.get_size()):
                self._knownBoard[row].append("O")

    def check_done(self):
        """
        Checks if the agent has located all the ships and if the game is complete.
        :return: True or False for if game is complete or not.
        """
        done = True
        for ship in self._shipStatus:
            if not self._shipStatus[ship][0]:
                done = False
        return done

    def hit_ship(self, ship_name, row, col):
        sunk = False
        ship = self._shipStatus[ship_name]
        ship[2].append((row, col))
        if ship[1] <= len(ship[2]):
            ship[0] = True
            sunk = True

        return sunk

    def guess(self, row, col):
        """
        Make a guess on the game board for a position.
        :param row: Row of guess
        :param col: Column of guess
        :return: Value of the board at the guess location
        """
        self._count += 1
        self._guessed.append((row, col))
        current = self._board.get_square(row, col)
        self._knownBoard[row][col] = current
        if current in self._shipStatus:
            self.hit_ship(current, row, col)

        return self._board.get_square(row, col)

    def reset(self):
        self._count = 0
        self._guessed = []

        # Reset the ship list
        self._shipStatus = {}
        for ship in self._board.get_list():
            self._shipStatus[ship[1]] = [False, ship[0], []]

        # Wipe the known board
        size = self._board.get_size()
        for i in range(size):
            for j in range(size):
                self._knownBoard[i][j] = 0

        # Wipe the probability board
        size = self._board.get_size()
        for i in range(size):
            for j in range(size):
                self._probBoard[i][j] = 0

    def print_kboard(self):
        for row in self._knownBoard:
            print(row)

    def get_count(self):
        return self._count

    def get_guessed(self):
        return self._guessed

