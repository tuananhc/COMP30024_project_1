"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

from collections import defaultdict
import sys
import json

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import print_board, print_coordinate

def main():
    print(sys.argv[1])
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).
    print(data)
    board_dict = defaultdict(str)
    for item in data['board']:
        board_dict[tuple([item[1], item[2]])] = item[0]
    board_dict[tuple(data['start'])] = 'start'
    board_dict[tuple(data['goal'])] = 'goal'
    
    print(board_dict)

    print_board(data['n'], board_dict)
    print_coordinate(1, 2)
