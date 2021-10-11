# Memetic Algorithms for Battleship
A project to investigate the use of memetic algorithms for playing the board game Battleship. 

## [Project Paper](/Memetic_Battleship_KD.pdf)

Main report for this project. Contains the details of tests performed and results.

## Code used to build the project:

All code was built using Python 3.8. Only the standard library was used so no 
additional library installations are required.

### [example.py](/example.py) (How to use project code)

Use this file for an example of how to initiate and run tests on the battleship program. This file works as a template 
for starting your own tests.

### [board.py](/board.py) and [agent.py](/agent.py) (Background Files)

Both of these classes facilitate the game of battleship and need to be initialized before starting testing.  

_board.py_: Represents a battleship gameboard storing values for each cell. Main function is place_ships which will 
randomly place ships on the board to initialize a game.

_agent.py_: Represents an agent playing the game of battleship. Interacts with the Board class to 
guess at different cells and play the game of battleship. Main functions are prob_guess and update_prob which control 
agents logic for selecting the next cell to guess.

### [test.py](/test.py)

Main class that that is used to run analysis on the games played and also carry out memetic algorithm functions. 
Connected to board and agent classes through a 'has-a' relationship.

### [Data Files](/Data)
Contains raw data from the runs that generated the results reported in the project paper. All data is saved as json 
files.    

cross/seed data format: Test results and gene sequence: [[Avg, Stdev, Min, Max], [10 test scores],[16 character genetic sequence]]  
mut_genes data format: List of genetic sequences from after mutation.  
train / test boards: List of game boards used to perform training and final testing.
