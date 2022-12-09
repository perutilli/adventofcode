"""
DAY 5

stacks.txt:
position of crates (identified by a letter) on numbered stacks (identified by a number)
e.g.

[A]
[B] [C]
 1   2

moves.txt:
list of moves in the following format:
move n crates from stack_num to stack_num

We want to know the crates on the highest position of each stack after all the moves

PART 2

in this case when we move multiple crates they are moved in a single operation, so they keep their relative order
"""

import re
from collections import deque

class Move:
    """
    represents a move
    """

    def __init__(self, n_crates: int, from_stack: int, to_stack: int):
        self.n_crates = n_crates
        self.from_stack = from_stack
        self.to_stack = to_stack

def read_stacks(file_in: str) -> list:
    """
    returns a list of stacks
    """
    stacks = []
    with open(file_in, "r") as file_in:
        first = True
        for line in file_in.readlines():
            if line[:2] == " 1":
                break
            stacks = read_stack_line(line, stacks, first)
            first = False
    
    return stacks

def read_stack_line(line: str, stacks: list, first:bool) -> list:
    """
    extracts the letters from the line and prepends them to the stacks
    """
    i = 1
    letters = []
    while i < len(line):
        letters.append(line[i])
        i += 4
    for stack, letter in enumerate(letters):
        if first:
            if letter != " ":
                stacks.append(deque(letter))
            else:
                stacks.append(deque())
        else:
            if letter != " ":
                stacks[stack].appendleft(letter)
    return stacks

def read_moves(file_in: str) -> list:
    """
    returns a list of moves
    """
    moves = []
    with open(file_in, "r") as file_in:
        for line in file_in.readlines():
            match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            if match:
                moves.append(Move(int(match.group(1)), int(match.group(2)), int(match.group(3))))       
            else:
                raise Exception("Invalid move: " + line)
    return moves

def move_crates(moves: list, stacks: list) -> list:
    """
    executes the moves in the moves list and returns the modified stacks
    """
    for move in moves:
        for _ in range(move.n_crates):
            stacks[move.to_stack - 1].append(stacks[move.from_stack - 1].pop())
    return stacks

def move_crates_part_2(moves: list, stacks: list) -> list:
    """
    executes the moves in the moves list and returns the modified stacks
    """
    for move in moves:
        crates = []
        for _ in range(move.n_crates):
            crates.append(stacks[move.from_stack - 1].pop())
        for crate in crates[::-1]:
            stacks[move.to_stack - 1].append(crate)
    return stacks

if __name__ == "__main__":
    stacks = read_stacks("stacks.txt")
    moves = read_moves("moves.txt")
    stacks_part_1 = move_crates(moves, stacks)
    for stack in stacks_part_1:
        try:
            print(stack.pop(), end="")
        except IndexError:
            print(" ", end="")
    print()

    stacks = read_stacks("stacks.txt")
    stacks_part_2 = move_crates_part_2(moves, stacks)
    for stack in stacks_part_2:
        try:
            print(stack.pop(), end="")
        except IndexError:
            print(" ", end="")
    print()
