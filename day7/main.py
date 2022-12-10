"""
DAY 7

Part 1:

input.txt contains a series of commands and their outputs.
e.g.
$ cd /
$ ls
dir brdsppd
dir dnjqmzgg
126880 fmftdzrp.fwt
173625 hhfqgzfj.qvt

The commands are:
- cd <dir> - change directory
    <dir> can be a subdirectory of the current directory or .. (parent directory) or / (home directory)
- ls - list directory contents
Commands start with a $.

The output of ls is a list of directories and files:
- dir <dir> - a directory
- <number> <file> - a file of size <number>

The home directory is /.

The goal is to find the sizes of all directories of size less than 100000 and sum them up.

Part 2:

We need to find the smallest directory such that if we delete it, the size of '/' will be at most 40,000,000.
"""

from treelib import Node, Tree
from enum import Enum

class NodeType(Enum):
    DIR = 1
    FILE = 2

class NodeData:
    def __init__(self, size: int, type: NodeType):
        self.size = size
        self.type = type

def parse_input(file_name: str, tree: Tree):
    """
    Parse the input file and create a tree of directories and files.
    """
    with open(file_name, 'r') as f:
        current_path = '/'
        for line in f.readlines():
            line = line.strip()
            if line.startswith('$'):
                if line.startswith('$ cd'):
                    if (line.split('$ cd ')[1] == '/'):
                        current_path = '/'
                    elif (line.split('$ cd ')[1] == '..'):
                        current_path = '/'.join(current_path.split('/')[:-1])
                    else:
                        current_path = current_path + '/' + line.split('$ cd ')[1]
                else:
                    assert(line.startswith('$ ls'))
            else:
                if line.startswith('dir'):
                    # add the directory to the tree with default size 0
                    tree.create_node(line.split('dir ')[1], current_path + '/' + line.split('dir ')[1], parent=current_path, data = NodeData(size = 0, type = NodeType.DIR))
                else:
                    # add the file size to the current directory in the tree
                    tree.create_node(line.split(' ')[1], current_path + '/' + line.split(' ')[1], parent=current_path, data = NodeData(size = int(line.split(' ')[0]), type = NodeType.FILE))

def calculate_dir_sizes(node: Node, tree: Tree) -> None:
    """
    Calculate the sizes of all directories in the tree.
    """
    for n in tree.children(node.identifier):
        if (n.data.type == NodeType.DIR):
            calculate_dir_sizes(n, tree)
        node.data.size += n.data.size

def sum_dir_sizes_threashold(tree: Tree, sum: int, threashold: int) -> int:
    """
    Sum the sizes of all directories in the tree that are smaller than the threashold.
    """
    for n in tree.all_nodes():
        if (n.data.type == NodeType.DIR and n.data.size < threashold):
            sum += n.data.size
    return sum  

def find_smallest_dir(tree: Tree, minimum_size: int) -> int:
    """
    Find the smallest directory bigger than minimum_size
    """
    smallest_dir = None
    for n in tree.all_nodes():
        if (n.data.type == NodeType.DIR and n.data.size > minimum_size):
            if smallest_dir is None or n.data.size < smallest_dir.data.size:
                smallest_dir = n
    return smallest_dir

if __name__ == '__main__':
    tree = Tree()
    tree.create_node('', '/', data = NodeData(size = 0, type = NodeType.DIR))
    parse_input('input.txt', tree)
    calculate_dir_sizes(tree.get_node('/'), tree)
    print(sum_dir_sizes_threashold(tree, 0, 100000))
    minimum_size = tree.get_node('/').data.size - 40000000
    print(tree.get_node('/').data.size, minimum_size)
    smallest_dir = find_smallest_dir(tree, minimum_size)
    print(smallest_dir.data.size)