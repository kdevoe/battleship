# Author: Ken DeVoe
# Date: 7/12/2021
# Description: Class to run agent in the board environment and record / analyze results.

# TODO: Fill in test class.

from random import seed, randint

class Test:
    """
    Facilitates testing and analysis of an agents performance against a board.
    """

    # TODO: Add permanent storage (JSON file) for list of random boards. Also a generator for list of random boards.

    def __init__(self, agent, board):
        self._board = board
        self._agent = agent
        self._gLength = self._agent.get_glength()

    def rand_genes(self, min, max):
        """
        Makes a random set of genes as integers and assigns to the agent.
        :param min: Minimum value for random gene.
        :param max: Maximum value for random gene.
        :return: Set of genes created.
        """
        seed()
        genes = [randint(min, max) for _ in range(self._gLength)]
        self._agent.set_genes(genes)
        return genes

    def run(self, trials=1, style=0):
        """
        Simple run function that runs a single set of genes against a board for a set number of times. Returns a list
        of the guess counts for each run.
        :param trials: Number of trials for the agent to run against the board.
        :param style: Defaults to selecting next move through probability (style=0). Set to 1 for random guessing of
                        next move.
        :return: List of the counts (number of guesses) needed for each run.
        """
        counts = []

        for _ in range(trials):
            self._agent.reset()
            while not self._agent.check_done():
                if style == 0:
                    self._agent.rand_guess()
                elif style == 1:
                    self._agent.prob_guess()
            counts.append(self._agent.get_count())

        else:
            return counts

    def try_rand_genes(self):
    # TODO: Build function for running random genes
        pass

    def mutate(self, genes, p_modify, a_modify):


        new_genes = []
        for gene in genes:
            pass


