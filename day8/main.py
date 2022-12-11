"""
DAY 8

Part 1:
Input file contains a rectangle of trees, the number indicates how tall each tree is (0-9)
A tree is visible if it is visible from the top or the bottom or the left or right side (or a combination of these)
A tree is visible from one side if all trees are shorter than it between it and the side
The number of visible trees is the answer

Part 2:
Scenic score = product of the nubmer of visible trees for each tree
Find the maximum scenic score

"""
from typing import List, Tuple

def is_visible_from_top(tree: Tuple[int, int], trees:List[List[int]]) -> bool:
    tree_height = trees[tree[0]][tree[1]]
    for i in range(tree[0]):
        if trees[i][tree[1]] >= tree_height:
            return False
    return True

def is_visible_from_bottom(tree: Tuple[int, int], trees:List[List[int]]) -> bool:
    tree_height = trees[tree[0]][tree[1]]
    for i in range(tree[0]+1, len(trees)):
        if trees[i][tree[1]] >= tree_height:
            return False
    return True

def is_visible_from_left(tree: Tuple[int, int], trees:List[List[int]]) -> bool:
    tree_height = trees[tree[0]][tree[1]]
    for i in range(tree[1]):
        if trees[tree[0]][i] >= tree_height:
            return False
    return True

def is_visible_from_right(tree: Tuple[int, int], trees:List[List[int]]) -> bool:
    tree_height = trees[tree[0]][tree[1]]
    for i in range(tree[1]+1, len(trees[0])):
        if trees[tree[0]][i] >= tree_height:
            return False
    return True

def is_visible(tree: Tuple[int, int], trees:List[List[int]]) -> bool:
    return is_visible_from_top(tree, trees) or is_visible_from_bottom(tree, trees) or is_visible_from_left(tree, trees) or is_visible_from_right(tree, trees)

def get_scenic_score(tree: Tuple[int, int], trees:List[List[int]]) -> int:
    """
    returns the scenic score for a given tree
    """
    # trees visible on the top
    top_trees = 0
    for i in range(tree[0] - 1, -1, -1):
        top_trees += 1
        if trees[i][tree[1]] >= trees[tree[0]][tree[1]]:
            break
    # trees visible on the bottom
    bottom_trees = 0
    for i in range(tree[0] + 1, len(trees)):
        bottom_trees += 1
        if trees[i][tree[1]] >= trees[tree[0]][tree[1]]:
            break
    # trees visible on the left
    left_trees = 0
    for i in range(tree[1] - 1, -1, -1):
        left_trees += 1
        if trees[tree[0]][i] >= trees[tree[0]][tree[1]]:
            break
    # trees visible on the right
    right_trees = 0
    for i in range(tree[1] + 1, len(trees[0])):
        right_trees += 1
        if trees[tree[0]][i] >= trees[tree[0]][tree[1]]:
            break
    return top_trees * bottom_trees * left_trees * right_trees

def get_max_scenic_score(trees:List[List[int]]) -> int:
    max_score = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            score = get_scenic_score((i, j), trees)
            if score > max_score:
                max_score = score
    return max_score

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        trees = [[int(x) for x in line.strip()] for line in f.readlines()]
    visible_trees = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            if is_visible((i, j), trees):
                visible_trees += 1
    print(visible_trees)
    print(get_max_scenic_score(trees))
