# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Class for agent to play the game battleship.


class Agent:
    """
    Represents an agent which plays the game of battleship
    """

    def __init__(self, board):
        self._guessCount = 0
        # Make an array to hold the status of each ship being searched for
        self._shipStatus = []
        for ship in board.get_list():
            self._shipStatus.append([ship[1], False, [() for _ in range(ship[0])]])

        # Make a probability board initialized to 0
        self._probBoard = []
        for row in range(board.get_size()):
            self._probBoard.append([])
            for col in range(board.get_size()):
                self._probBoard[row].append(0)

        # Make board known by agent of ship locations all initialized to false
        self._knownBoard = []
        for row in range(board.get_size()):
            self._knownBoard.append([])
            for col in range(board.get_size()):
                self._knownBoard[row].append(False)

    def check_done(self):
        """
        Checks if the agent has located all the ships and if the game is complete.
        :return: True or False for if game is complete or not.
        """
        done = True
        for ship in self._shipStatus:
            if not ship[1]:
                done = False
        return done

    def get_guessCount(self):
        return self._guessCount


