# Author: Ken DeVoe
# Date: 7/4/2021
# Description: Main file to run the battleship program.


from board import Board
from agent import Agent
from test import Test
import copy
import numpy as np
import csv
from random import randint, seed

# Make a shipList (this can be updated per run)
shipList = [(5, "Ca"), (4, "Ba"), (3, "Cr"), (3, "Su"), (2, "De")]


if __name__ == '__main__':
    # Build and print a test board
    board = Board(shipList, 10)

    agent1 = Agent(board)

    test = Test(agent1, board)

    file = test.get_file("Data/cross_2.json")
    print(file)


    # for num in [2, 4, 8]:
    #     cross = test.get_file("cross_{}.json".format(num))
    #     output = []
    #     for line in cross:
    #         output.append([line[0][0]])
    #
    #     test.write_csv(output, "cross_{}.csv".format(num))


    # train_boards = test.get_file("train_boards.json")[0:10]
    #
    # test.do_cross(train_boards, "mut_genes_6.json", "cross_2.json", 5, 2)
    #
    # test.do_cross(train_boards, "mut_genes_6.json", "cross_4.json", 5, 4)
    #
    # test.do_cross(train_boards, "mut_genes_6.json", "cross_8.json", 3, 8)

    # seed_32K = test.get_file("seed_32000.json")
    #
    # cur_data = copy.deepcopy(seed_32K)
    # cur_data = sorted(cur_data[0:5000])
    #
    # best_6 = test.get_file("mut_genes_6.json")
    # output = []
    # for i in range(100):
    #     output.append([i+1, test.run_set(train_boards, None, cur_data[i][2])[0][0],
    #                    test.run_set(train_boards, None, best_6[i])[0][0]])
    #     print(i)
    #
    # test.write_csv(output, "best_6_comp.csv")

    # # Data for mutations
    # genes = []
    # for i in range(100):
    #     genes.append(cur_data[i][2])
    #
    # change = 6
    # mini = -10
    # maxi = 10
    #
    # avgs = []
    # stdevs = []
    # diverses = []
    #
    # runs = 100
    #
    # output = []
    #
    # for i in range(runs):
    #     # First record results
    #     results = []
    #     curr_avg = []
    #     for j in range(100):
    #         results.append(test.run_set(train_boards, None, genes[j]))
    #         curr_avg.append(results[j][0][0])
    #
    #     output.append([i, np.mean(curr_avg), np.std(curr_avg), test.diversity(genes, mini, maxi)])
    #
    #     # Next perform a round of mutation, update if there is improvement
    #     for j in range(100):
    #         curr_score = curr_avg[j]
    #         agent1.set_genes(genes[j])
    #         test_genes = test.mutate(mini, maxi, change)
    #         new_score = test.run_set(train_boards, None, test_genes)
    #
    #         if new_score[0][0] < curr_score:
    #             genes[j] = test_genes
    #
    #     print(output)
    #     test.write_csv(output, "mutations_6.csv")
    #     test.write_file(genes, "mut_genes_6.json")
    #
    #
    # genes = []
    # for i in range(100):
    #     genes.append(cur_data[i][2])
    #
    # change = 1
    # mini = -10
    # maxi = 10
    #
    # avgs = []
    # stdevs = []
    # diverses = []
    #
    # runs = 100
    #
    # output = []
    #
    # for i in range(runs):
    #     # First record results
    #     results = []
    #     curr_avg = []
    #     for j in range(100):
    #         results.append(test.run_set(train_boards, None, genes[j]))
    #         curr_avg.append(results[j][0][0])
    #
    #     output.append([i, np.mean(curr_avg), np.std(curr_avg), test.diversity(genes, mini, maxi)])
    #
    #     # Next perform a round of mutation, update if there is improvement
    #     for j in range(100):
    #         curr_score = curr_avg[j]
    #         agent1.set_genes(genes[j])
    #         test_genes = test.mutate(mini, maxi, change)
    #         new_score = test.run_set(train_boards, None, test_genes)
    #
    #         if new_score[0][0] < curr_score:
    #             genes[j] = test_genes
    #
    #     print(output)
    #     test.write_csv(output, "mutations_1.csv")
    #     test.write_file(genes, "mut_genes_1.json")
    #
    #
    # genes = []
    # for i in range(100):
    #     genes.append(cur_data[i][2])
    #
    # change = 10
    # mini = -10
    # maxi = 10
    #
    # avgs = []
    # stdevs = []
    # diverses = []
    #
    # runs = 100
    #
    # output = []
    #
    # for i in range(runs):
    #     # First record results
    #     results = []
    #     curr_avg = []
    #     for j in range(100):
    #         results.append(test.run_set(train_boards, None, genes[j]))
    #         curr_avg.append(results[j][0][0])
    #
    #     output.append([i, np.mean(curr_avg), np.std(curr_avg), test.diversity(genes, mini, maxi)])
    #
    #     # Next perform a round of mutation, update if there is improvement
    #     for j in range(100):
    #         curr_score = curr_avg[j]
    #         agent1.set_genes(genes[j])
    #         test_genes = test.mutate(mini, maxi, change)
    #         new_score = test.run_set(train_boards, None, test_genes)
    #
    #         if new_score[0][0] < curr_score:
    #             genes[j] = test_genes
    #
    #     print(output)
    #     test.write_csv(output, "mutations_10.csv")
    #     test.write_file(genes, "mut_genes_10.json")

    # # Data for first 100 values
    # seed_32K = test.get_file("seed_32000.json")
    #
    # cur_data = copy.deepcopy(seed_32K)
    # cur_data = sorted(cur_data[0:100])
    # averages = []
    # genes = []

    # for j in range(100):
    #     averages.append(cur_data[j][0][0])
    #     genes.append(cur_data[j][2])
    #
    # print(np.mean(averages), np.std(averages), test.diversity(genes, -10, 10))

    # # Seed test data
    # seed_data = []
    #
    # seed_32K = test.get_file("seed_32000.json")
    #
    # for i in range(1, 33):
    #     amount = i * 1000
    #     cur_data = copy.deepcopy(seed_32K)
    #     cur_data = sorted(cur_data[0:amount])
    #     averages = []
    #     genes = []
    #     for j in range(100):
    #         averages.append(cur_data[j][0][0])
    #
    #         genes.append(cur_data[j][2])
    #     average = np.mean(averages)
    #     diversity = test.diversity(genes, -10, 10)
    #
    #     seed_data.append([amount, average, np.std(averages), diversity])
    #
    # test.write_csv(seed_data, "seed.csv")



    # train_boards = test.get_file("train_boards.json")[0:10]
    #
    # # Creating seed files
    # name = "seed"
    # prefix = 2
    #
    # for runs in [100, 500, 1000, 2000, 4000, 8000, 16000, 32000]:
    #
    #     set1 = []
    #
    #     file1 = "{}_{}.json".format(name, runs)
    #
    #     for i in range(runs):
    #         test.rand_genes(-10, 10)
    #         test.run_set(train_boards, set1)
    #
    #         if i % 19 == 0:
    #             test.append_file(set1, file1)
    #             set1 = []
    #             print("Seed {}, {} % complete".format(runs, (i/runs)*100))
    #
    #     if set1 is not None:
    #         test.append_file(set1, file1)
#
#     for run in range(1, 5):
#         infile = "set{}-{}.json".format(prefix, 1 + (run-1) * 2)
#         outfile = "set{}-{}.json".format(prefix, 2 + (run-1) * 2)
#         test.do_mutate(randBoards, infile, outfile)
#
#         infile = "set{}-{}.json".format(prefix, 2 + (run-1) * 2)
#         outfile = "set{}-{}.json".format(prefix, 3 + (run-1) * 2)
#         test.do_cross(randBoards, infile, outfile)


