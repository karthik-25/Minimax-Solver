# Minimax
Implementation of minimax algorithm (2 players with alternate moves)

# Scripts
1. tree.py contains the code for Tree and TreeNode classes. The logic for building a tree,
validating it and running the minimax algorithm can be found here.

2. io_processor.py contains the code for IO_Processor class. It contains the logic for parsing
the user input via CLI

3. minimax.py contains the main function and it is the script to run via CLI.


# Run Scripts
Please run minimax.py as follows:
python minimax.py [-v] [-ab] max/min n input.txt

-v: toggle verbose, optional arugment
-ab: toggle alpha beta pruning, optional arugment
max/min: assigns root player to be max or min. Enter either max or min. Required argument.
n: max-cutoff value. Enter any positive integer. Required argument.
input.txt: input file. Must be a text file with ".txt" extension. Required argument.

Sample commands:
python3 minimax.py -v -ab max 15 input.txt
python3 minimax.py -v min 15 input.txt
python3 minimax.py max 15 input.txt

Notes:
- list of arguments mentioned above (everything after minimax.py) can be entered in any order
- if input file is in the same directory as the scripts, just the filename should suffice. 
  Otherwise, file path or relative path would be required. 
- if there are errors faced in building the tree due to bad input, program will exit and
  print the error accordingly. 


# References
- Textbook
- https://www.geeksforgeeks.org/python-output-formatting/
- https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
