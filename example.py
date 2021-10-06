# Author: Ken DeVoe
# Date: 10/4/2021
# Description: Example file for how to run population generation and mutation on genetic sequences for battleship.


from board import Board     # Used to initialize both Agent and Test classes
from agent import Agent     # Used to initialize the test class
from test import Test       # Contains majority of functions for testing


def example():
    """
    An example method to show process of initiating a seed population, mutating the top performing genetic sequences
    and writing the results to a csv file.
    Feel free to modify values such as population size, number of training boards, select for down-selection and
    generations to customize the test.
    """

    # Initiate a list of ships. As shown these are tuples of number representing the length and character to represent
    # the ship type. Any combination of ships can be used as long as they can fit on the board.
    shipList = [(5, "Ca"), (4, "Ba"), (3, "Cr"), (3, "Su"), (2, "De")]

    board = Board(shipList)  # Build a gameboard and place ships on it
    agent = Agent(board)  # Build an agent which operates on the board
    test = Test(agent, board)  # Build an object to run testing

    # ---------------------------------------------------------------------------------------------------------
    # Example 1: Generating a random population of 20 genes with scores and saving to json file
    # ---------------------------------------------------------------------------------------------------------

    population = 20         # Size of population to create
    train_size = 10         # Number of random boards in the training set

    train_boards = test.rand_boards(train_size)
    gene_results = []

    # Call the run_set function to test a random gene sequence against the training board set, results stored in
    # gene_results list
    print("Generating random population...")
    for i in range(population):
        test.run_set(train_boards, gene_results, test.rand_genes())
        # Give periodic output every 10 genes on progress in creating the population
        if i % 10 == 0:
            print("Population {}% complete.".format(round((i / population) * 100, 2)))
    print("Random population generation complete.")

    # Save results to a json file
    test.write_json(gene_results, "Example1.json")

    # ---------------------------------------------------------------------------------------------------------
    # Example 2: Running 50 generations of mutations on top 10 genes generated in Example 1
    # ---------------------------------------------------------------------------------------------------------

    # Mutate the top 100 genes from Example1.json and store in Example2.json. Default is Top 100, change size = 2 and
    # generations = 50. However these are optional parameters for do_mutate function.

    select = 10         # Number of top genes to select from initial population, needs to be <= to population size
    generations = 10    # Number of generations to train each gene for
    change = 2          # Amount a gene marker is changed for each mutations

    print("Starting mutations...")
    test.do_mutate(train_boards, "Example1.json", "Example2.json", select, generations, change)

    # -------------------------------------------------------------------------------------------------------
    # Example 3: Writing the top gene scores before and after mutation to a csv file and printing to console.
    # -------------------------------------------------------------------------------------------------------

    example1 = test.get_json("Example1.json")
    example2 = test.get_json("Example2.json")

    example1.sort()

    output = [["Gene", "Before", "After"]]  # Make the outfile with a header row which will become a csv file
    print("Gene Before After")              # Print the header row to the console

    # Store and print the gene number and average score before and after mutation
    for i in range(len(example2)):
        output.append([i+1, example1[i][0][0], example2[i][0][0]])
        print(" {}   {}  {} ".format(i+1, example1[i][0][0], example2[i][0][0]))

    # Write result to a csv file
    test.write_csv(output, "Example3.csv")


if __name__ == '__main__':
    example()
