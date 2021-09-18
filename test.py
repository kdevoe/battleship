# Author: Ken DeVoe
# Date: 7/12/2021
# Description: Class to run agent in the board environment and record / analyze results.


from random import seed, randint
import json
import numpy as np
import os

class Test:
    """
    Facilitates testing and analysis of an agents performance against a board.
    """

    def __init__(self, agent, board):
        self._board = board
        self._agent = agent
        self._gLength = self._agent.get_glength()

    def write_file(self, item, filename):
        with open(filename, 'w') as outfile:
            json.dump(item, outfile)

    def get_file(self, filename):
        with open(filename, 'r') as infile:
            item = json.load(infile)

        return item

    def append_file(self, item, filename):
        """
        Appends data provided in as item into the specified json data file.
        :param item: New data to add to the json file.
        :param filename: Json file to add the data to.
        :return: No return value.
        """

        # Guard for if file is either empty or does not exist
        try:
            if os.stat(filename).st_size == 0:
                with open(filename, 'w') as outfile:
                    json.dump([], outfile)

        except FileNotFoundError:
            with open(filename, 'w') as outfile:
                json.dump([], outfile)

        with open(filename, 'r') as infile:
            values = json.load(infile)

        for line in item:
            values.append(line)

        with open(filename, 'w') as outfile:
            json.dump(values, outfile)


    def rand_boards(self, qty=100):

        boards = []
        for _ in range(qty):
            self._board.reset()
            boards.append(self._board.get_board())

        return boards


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


    def mutate(self, min, max, change=2):
        """

        :param genes:
        :param min:
        :param max:
        :return:
        """
        genes = self._agent.get_genes()

        seed()

        # Select random gene to mutate
        gene = randint(0, self._gLength - 1)

        # Select random direction to mutate gene (plus or minus)
        if randint(0, 1):
            change *= -1

        # Attempt to modify the gene, if modification puts values outsize max or min
        # then reverses the direction and cuts modification amount in half
        modified = False

        while not modified:
            new_gene = genes[gene] + change
            if min <= new_gene <= max:
                genes[gene] = new_gene
                modified = True
            else:
                change *= -1
                # change = change // 2

        #### Taking out the option to automatically update genes for now
        #self._agent.set_genes(genes)

        return genes

    def mutations(self, boards, min, max, change=2, trials=50):

        best_result = self.run_set(boards)
        current = best_result[0][0]

        for _ in range(trials):
            genes = self._agent.get_genes()
            new_genes = self.mutate(min, max, change)
            run_result = self.run_set(boards, None, new_genes)
            new_count = run_result[0][0]

            # If new_genes are equal or better then reset current count and keep new_gene configuration
            if new_count <= current:
                current = new_count
                best_result = run_result
                # Commenting out line for reporting intermediate results
                #print(_, best_result)

            # If new_genes are not better than set genes back to the original set
            else:
                self._agent.set_genes(genes)

        return best_result

    def run(self, style=1):
        """
        Function that runs a single set of genes against a single board. Returns a list of the guess counts for each
        run.
        :param trials: Number of trials for the agent to run against the board.
        :param style: Defaults to selecting next move through probability (style=0). Set to 1 for random guessing of
                        next move.
        :return: Count (number of guesses) needed for the run.
        """

        self._agent.reset()
        while not self._agent.check_done():
            if style == 0:
                self._agent.rand_guess()
            elif style == 1:
                self._agent.prob_guess()

            # Adding in board print
            # self._agent.print_kboard()
            # print()
            # self._agent.print_pboard()
            # print()

        else:
            return self._agent.get_count()

    def run_set(self, boards, save_list=None, new_genes=None):
        """
        Calls the run function against each board supplied in the boards input parameter.
        :param boards: A list of boards to be run against.
        :param save_list: List to store data generated from run_set.
        :param new_genes: Genes to test against
        :return: A list consisting of a list of counts for moves from each run and the genes used for the test set.
        """
        # Initiate genes to the input values if provided. Otherwise default genes already loaded in Test classes agent
        # will be used.
        if new_genes is not None:
            self._agent.set_genes(new_genes)

        counts = []
        for board in boards:
            self._board.set_board(board)
            counts.append(self.run())

        if save_list is not None:
            save_list.append([self.stats(counts), counts, self._agent.get_genes()])

        return [self.stats(counts), counts, self._agent.get_genes()]

    def cross_genes(self, gene_list, divisions=4):
        """
        Generates a list of new genes by mixing individual divisions of each of the genes in the gene_list. For example
        a newly generated gene may consist of 4 parts each from a separate original gene.
        :param gene_list:
        :param divisions:
        :return:
        """

        new_list = [gene_list[0]]  # Make a new list and add first original gene to it

        gene_len = len(gene_list[0])

        offset = gene_len // divisions

        sequence = [0] * divisions  # list of gene to take from for each section

        # Run through each permutation of values for possible gene combinations
        end = False

        while not end:
            incremented = False
            index = 0

            while not incremented:

                # If current index has reached its maximum value then carry over to next index
                if sequence[index] == len(gene_list) - 1:
                    sequence[index] = 0
                    index += 1

                    # If out of indexes to increment then maximum permutation reached, end loops
                    if index >= divisions:
                        incremented = True
                        end = True

                # Otherwise simply add 1 to the current index and add this new permutation to the new_list
                else:
                    sequence[index] = sequence[index] + 1
                    incremented = True

                    # Make and add new gene to the new_list
                    new_gene = []
                    for section in range(divisions):
                        new_gene += gene_list[sequence[section]][section*offset:section*offset + offset]
                    new_list.append(new_gene.copy())

        return new_list

    def do_cross(self, boards, infile, outfile, select=8):
        best = self.get_file(infile)
        best.sort()

        seed_genes = []
        for i in range(select):
            seed_genes.append(best[i][2])

        new_genes = self.cross_genes(seed_genes)

        new_set = []
        for i in range(len(new_genes)):
            self.run_set(boards, new_set, new_genes[i])

            if i % 19 == 0:
                self.append_file(new_set, outfile)
                new_set = []
                print((i / len(new_genes)) * 100, "% complete")

        if new_set is not None:
            self.append_file(new_set, outfile)

    def do_mutate(self, boards, infile, outfile, min=-10, max=10, select=100):

        best = self.get_file(infile)
        best.sort()

        new_set = []
        for i in range(select):
            self._agent.set_genes(best[i][2])
            current = self.mutations(boards, min, max)
            new_set.append(current)

            print(i, current)

            if i % 19 == 0:
                self.append_file(new_set, outfile)
                new_set = []

        if new_set is not None:
            self.append_file(new_set, outfile)



    def stats(self, values):
        return [np.mean(values).item(), np.std(values).item(), np.min(values).item(), np.max(values).item()]

    def try_rand_genes(self):
    # TODO: Build function for running random genes
        pass


