# battleship
A project to investigate the use of memetic algorithms for playing the game of Battleship. 

## [Project Paper](/Memetic_Battleship_KD.pdf)

For an overview of the study and results please see:
[Project Paper](/Memetic_Battleship_KD.pdf)

## Code used to build the project:

All code was built using Python version 3.8 with the standard library.

### [example.py](/example.py) (How to use code)

The  file shows how to initiate and run 

### board.py and agent.py (Background Files)

Both of these classes facilitate the game of battleship and need to be initialized to run tests.  

_board.py_: Represents a battleship gameboard storing values for each cell. Main function is place_ships which will 
randomly place ships on the board to initialize a game.

_agent.py_: Represents an agent playing the game of battleship. Interacts with the Board class to 
guess at different cells and play the game of battleship.

### test.py

Main class that will run analysis on the games played and  

### 