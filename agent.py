# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Class for agent to play the game battleship.

from random import randint, seed

class Agent:
    """
    Represents an agent which plays the game of battleship
    """

    def __init__(self, board, genes=None):
        """

        :param board: Board object to be the environment in which the agent acts.
        :param genes: An array of integers of length 16. #### Fill in more here.
        """
        self._board = board
        self._size = board.get_size()
        self._guessed = []
        self._count = 0
        if genes is None:
            self._genes = [1] * 16      # If no values are passed set all genes to 1
        else:
            self._genes = genes

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

    def rand_guess(self):
        """
        Makes a random guess from available spaces on the board
        :return: Value at the location guessed
        """
        seed()
        row = randint(0, self._size - 1)
        col = randint(0, self._size - 1)
        while self._knownBoard[row][col] != "O":
            row = randint(0, self._size - 1)
            col = randint(0, self._size - 1)

        return self.guess(row, col)

    def reset(self):
        self._count = 0
        self._guessed = []

        # Reset the ship list
        self._shipStatus = {}
        for ship in self._board.get_list():
            self._shipStatus[ship[1]] = [False, ship[0], []]

        # Wipe the known board
        self.wipe_board(self._knownBoard, "O")

        # Wipe the probability board
        self.wipe_board(self._probBoard, "O")

    ################ Work here next #############################
    def update_prob(self):
        self.wipe_board(self._probBoard, 0)
        pass

    def wipe_board(self, board, value):
        # Guard for if board is empty, will do nothing
        if len(board) == 0:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = value

    def calc_fade(self, distance, initial, fade):
        return initial * (1 / distance**(fade/10))

    def update_genes(self, genes):
        for i in len(genes):
            self._genes[i] = genes[i]

    def print_kboard(self):
        for row in self._knownBoard:
            print(row)

    def get_genes(self):
        return self._genes

    def get_count(self):
        return self._count

    def get_guessed(self):
        return self._guessed

