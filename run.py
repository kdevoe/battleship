# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Main file to run the battleship program.


from board import Board
from agent import Agent
from test import Test
from random import randint, seed

# Make a shipList (this can be updated per run)
shipList = [(5, "Ca"), (4, "Ba"), (3, "Cr"), (3, "Su"), (2, "De")]


if __name__ == '__main__':
    # Build and print a test board
    board = Board(shipList, 10)

    agent1 = Agent(board)

    test = Test(agent1, board)

    randBoards = test.rand_boards(10)

    prefix = 2
    runs = 10000

    set1 = []

    file1 = "set{}-1.json".format(prefix)

    for i in range(runs):
        test.rand_genes(-10, 10)
        test.run_set(randBoards, set1)

        if i % 19 == 0:
            test.append_file(set1, file1)
            set1 = []
            print((i / runs) * 100, "% complete")

    for run in range(1, 5):
        infile = "set{}-{}.json".format(prefix, 1 + (run-1) * 2)
        outfile = "set{}-{}.json".format(prefix, 2 + (run-1) * 2)
        test.do_mutate(randBoards, infile, outfile)

        infile = "set{}-{}.json".format(prefix, 2 + (run-1) * 2)
        outfile = "set{}-{}.json".format(prefix, 3 + (run-1) * 2)
        test.do_cross(randBoards, infile, outfile)


    # # Run mutations on the best 50 from random selection
    # best1 = test.get_file("set1.json")
    # best1.sort()
    #
    #
    #
    # set2 = []
    # for i in range(50):
    #     agent1.set_genes(best1[i][2])
    #     current = test.mutations(randBoards, -10, 10)
    #     set2.append(current)
    #
    #     print(i, current)
    #
    #     if i % 19 == 0:
    #         test.append_file(set2, "set2.json")
    #         set2 = []
    #
    # if set2 is not None:
    #     test.append_file(set2, "set2.json")



    # Get top values from mutation run
    # Perform cross_mutation and generate set3 as best set

    # best2 = test.get_file("set2.json")
    # best2.sort()
    #
    # best2_genes = []
    # for i in range(8):
    #     best2_genes.append(best2[i][2])
    #
    # set3_genes = test.cross_genes(best2_genes)
    #
    # set3 = []
    # for i in range(len(set3_genes)):
    #     test.run_set(randBoards, set3, set3_genes[i])
    #
    #     if i % 19 == 0:
    #         test.append_file(set3, "set3.json")
    #         set3 = []
    #         print((i / len(set3_genes)) * 100, "% complete")
    #
    # if set3 is not None:
    #     test.append_file(set3, "set3.json")

    # Perform mutations to generate set4

    # best3 = test.get_file("set3.json")
    # best3.sort()
    #
    # set4 = []
    # for i in range(100):
    #     agent1.set_genes(best3[i][2])
    #     current = test.mutations(randBoards, -10, 10)
    #     set4.append(current)
    #
    #     print(i, current)
    #
    #     if i % 19 == 0:
    #         test.append_file(set4, "set4.json")
    #         set4 = []
    #
    # if set4 is not None:
    #     test.append_file(set4, "set4.json")



    # Get top values from mutation run
    # Perform cross_mutation and generate set5 as best set

    # best4 = test.get_file("set4.json")
    # best4.sort()
    #
    # best4_genes = []
    # for i in range(8):
    #     best4_genes.append(best4[i][2])
    #
    # set5_genes = test.cross_genes(best4_genes)
    #
    # set5 = []
    # for i in range(len(set5_genes)):
    #     test.run_set(randBoards, set5, set5_genes[i])
    #
    #     if i % 19 == 0:
    #         test.append_file(set5, "set5.json")
    #         set5 = []
    #         print((i / len(set5_genes)) * 100, "% complete")
    #
    # if set5 is not None:
    #     test.append_file(set5, "set5.json")


    # Perform mutations to generate set6

    # best5 = test.get_file("set5.json")
    # best5.sort()
    #
    # set6 = []
    # for i in range(100):
    #     print(i, best5[i])
    #     agent1.set_genes(best5[i][2])
    #     current = test.mutations(randBoards, -10, 10)
    #     set6.append(current)
    #
    #     print(i, current)
    #
    #     if i % 19 == 0:
    #         test.append_file(set6, "set6.json")
    #         set6 = []
    #
    # if set6 is not None:
    #     test.append_file(set6, "set6.json")


    # Get top values from mutation run
    # Perform cross_mutation and generate set7 as best set

    # best6 = test.get_file("set6.json")
    # best6.sort()
    #
    # best6_genes = []
    # for i in range(8):
    #     best6_genes.append(best6[i][2])
    #
    # set7_genes = test.cross_genes(best6_genes)
    #
    # set7 = []
    # for i in range(len(set7_genes)):
    #     test.run_set(randBoards, set7, set7_genes[i])
    #
    #     if i % 19 == 0:
    #         test.append_file(set7, "set7.json")
    #         set7 = []
    #         print((i / len(set7_genes)) * 100, "% complete")
    #
    # if set7 is not None:
    #     test.append_file(set7, "set7.json")


    # Perform mutations to generate set8

    # best7 = test.get_file("set7.json")
    # best7.sort()
    #
    # set8 = []
    # for i in range(100):
    #     print(i, best7[i])
    #     agent1.set_genes(best7[i][2])
    #     current = test.mutations(randBoards, -10, 10)
    #     set8.append(current)
    #
    #     print(i, current)
    #
    #     if i % 19 == 0:
    #         test.append_file(set8, "set8.json")
    #         set8 = []
    #
    # if set8 is not None:
    #     test.append_file(set8, "set8.json")
