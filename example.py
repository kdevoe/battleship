# Author: Ken DeVoe
# Date: 10/4/2021
# Description: Example file for how to run population generation and mutation on genetic sequences for battleship.


from board import Board  # Needed to initialize both Agent and Test classes
from agent import Agent  # Needed for the test class
from test import Test  # Contains majority of functions for testing


def example():
    """
    An example method to show process of initiating a seed population, mutating the top performing genetic sequences
    and writing the results to a csv file.
    """

    # Initiate a list of ships. As shown these are tuples of number representing the length and character to represent
    # the ship type. Any combination of ships can be used as long as they can fit on the board.
    shipList = [(5, "Ca"), (4, "Ba"), (3, "Cr"), (3, "Su"), (2, "De")]

    board = Board(shipList)  # Build a gameboard and place ships on it
    agent = Agent(board)  # Build an agent which operates on the board
    test = Test(agent, board)  # Build an object to run testing

    # -------------------------------------------------------------------------------------------
    # Example 1: Generating a random population of 200 genes with scores and saving to json file
    # -------------------------------------------------------------------------------------------

    population = 20
    train_boards = test.rand_boards(10)
    gene_results = []

    # Call the run_set function to test a random gene sequence against the training board set, results stored in
    # gene_results list
    print("Generating random population...")
    for i in range(population):
        test.run_set(train_boards, gene_results, test.rand_genes())
        if i % 10 == 0:
            print("Population {}% complete.".format(round((i / population) * 100, 2)))
    print("Random population generation complete.")

    # Save results to a json file
    test.write_json(gene_results, "Example1.json")

    # -------------------------------------------------------------------------------------------
    # Example 2: Running 50 generations of mutations on top 100 genes generated in Example 1
    # -------------------------------------------------------------------------------------------

    # Mutate the top 100 genes from Example1.json and store in Example2.json. Default is Top 100, change size = 2 and
    # generations = 50. However these are optional parameters for do_mutate function.
    print("Starting mutations...")
    test.do_mutate(train_boards, "Example1.json", "Example2.json", 10, 10)

    # -------------------------------------------------------------------------------------------
    # Example 3: Writing the top 100 scores before and after mutation to a csv file and printing to console.
    # -------------------------------------------------------------------------------------------

    example1 = test.get_json("Example1.json")
    example2 = test.get_json("Example2.json")

    example1.sort()

    # Make the outfile with a header row which will become a csv file
    output = [["Gene", "Before", "After"]]
    print("Gene Before After")
    for i in range(len(example2)):
        output.append([i+1, example1[i][0][0], example2[i][0][0]])
        print(" {}   {}  {} ".format(i+1, example1[i][0][0], example2[i][0][0]))

    # Write result to a csv file
    test.write_csv(output, "Example3.csv")


if __name__ == '__main__':
    example()
