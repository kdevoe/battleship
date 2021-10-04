# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Class for agent to play the game battleship. Utilizes a has-a relationship with the Board class.

from random import randint, seed

class Agent:
    """
    Represents an agent which plays the game of battleship.
    """

    def __init__(self, board, genes=None):
        """

        :param board: Board object to be the environment in which the agent acts.
        :param genes: An array of integers of length 16. (See attached paper for description of genetic sequence) Takes
                        the form of a list of integers, one for each marker. Initializes to all 1 if not passed in.
        """
        self._board = board
        self._size = board.get_size()
        self._guessed = []  # Locations that have already been guessed by the agent
        self._count = 0  # Number of guesses made by the agent
        # Dictionary of cell character to value pairs. Open, hit, miss and sunk all take different values. All ships
        # default to the same value of 2 representing hit.
        self._code = {'O': 0, 'M': 1, "Ca": 2, "Ba": 2, "Cr": 2, "Su": 3, "De": 2, 'S': 3}

        # If no genes are passed in set to all 1, otherwise use values passed in
        if genes is None:
            self._genes = [1] * 16
        else:
            self._genes = genes.copy()

        # Make an array to hold the status of each ship being searched for
        self._shipStatus = {}
        for ship in board.get_list():
            self._shipStatus[ship[1]] = [False, ship[0], []]

        # Make a probability board initialized to all 0
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
        # Default to done for the game. If one ship still is not sunk then will return not done.
        done = True
        for ship in self._shipStatus:
            if not self._shipStatus[ship][0]:
                done = False
        return done

    def hit_ship(self, ship_name, row, col):
        """
        Handles the case where a guess hits a ship. Will update that ships status as to how many hits it has and
        whether it is sunk or not.
        :param ship_name: Character representing ship type.
        :param row: Row hit is at.
        :param col: Column hit is at.
        :return: T/F boolean for if ship has been sunk or not.
        """
        sunk = False

        # Add the hit location to the ships list of hits.
        ship = self._shipStatus[ship_name]
        ship[2].append((row, col))

        # If the number of hits equals the length of the ship set it as sunk.
        if ship[1] <= len(ship[2]):
            ship[0] = True
            sunk = True

        return sunk

    def guess(self, row, col):
        """
        Make a guess on the game board for a position. Assumes the input row and column are valid open spaces.
        :param row: Row of guess
        :param col: Column of guess
        :return: Value of the board at the guess location
        """
        self._count += 1  # Increment the counter for guesses made by the agent
        self._guessed.append((row, col))  # Add guessed cell to locations guessed by agent
        current = self._board.get_square(row, col)  # Get the value at the guessed cell

        # Case for a miss
        if current == False:
            self._knownBoard[row][col] = 'M'

        # Case for a hit
        else:
            self._knownBoard[row][col] = current
        if current in self._shipStatus:
            self.hit_ship(current, row, col)
        self.update_prob()
        return self._knownBoard[row][col]

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

    def prob_guess(self):

        prob_list = []
        for row in range(self._size):
            for col in range(self._size):
                prob_list.append((self._probBoard[row][col], row, col))

        prob_list.sort(reverse=True)

        # Iterate through the probability list until an location that hasn't been guessed is selected
        cur = 0
        while (prob_list[cur][1], prob_list[cur][2]) in self._guessed:
            cur += 1

        return self.guess(prob_list[cur][1], prob_list[cur][2])

    def reset(self):

        # Reset the total guess count and locations guessed
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

    def update_prob(self):
        """
        Updates the probability board given the information in the known board.
        Note: This is the most expensive part of the program, operating in O(N^3) time.
        :return:
        """
        self.wipe_board(self._probBoard, 0)

        # Array for movement (Up, Up Right, Right, Down Right, Down, Down Left, Left, Up Left)
        dir_array = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for cur_row in range(self._size):
            for cur_col in range(self._size):
                cur_val = self._code[self._knownBoard[cur_row][cur_col]]
                for dir in range(8):
                    sel_row = cur_row + dir_array[dir][0]
                    sel_col = cur_col + dir_array[dir][1]

                    horzVert = (dir % 2)
                    initial = self._genes[cur_val*4 + horzVert*2]
                    fade = self._genes[cur_val*4 + horzVert*2 + 1]
                    distance = 1
                    # Check that the position being updated is still on the board
                    while (0 <= sel_row < self._size) and (0 <= sel_col < self._size):

                        self._probBoard[sel_row][sel_col] += self.calc_fade(distance, initial, fade)

                        distance += 1
                        sel_row += dir_array[dir][0]
                        sel_col += dir_array[dir][1]

    def wipe_board(self, board, value):
        # Guard for if board is empty, will do nothing
        if len(board) == 0:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = value

    def calc_fade(self, distance, initial, fade):
        return initial * (1 / distance**(fade/5))

    def print_kboard(self):
        for row in self._knownBoard:
            print(row)

    def print_pboard(self):
        for row in self._probBoard:
            print([round(x) for x in row])

    def set_genes(self, genes):
        self._genes = genes.copy()

    def get_genes(self):
        return self._genes

    def get_glength(self):
        return len(self._genes)

    def get_count(self):
        return self._count

    def get_guessed(self):
        return self._guessed

