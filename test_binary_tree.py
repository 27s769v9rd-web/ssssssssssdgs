"""
File: TestBinaryTree.py
Description: Implementation and testing of binary search tree methods
Student Name: Jeff Zheng
Student UT EID: jrz554
Partner Name:
Partner UT EID:
Course Name: CS 313E
Unique Number: 54970
Date Created: 10/22/26
Date Last Modified: 10/23/26
"""
import sys

class Node:
    """A node"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        """Prints the node and its children"""
        if self.lchild is not None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild is not None:
            self.rchild.print_node(level + 1)

    def get_height(self):
        """Returns the height of the tree"""
        if self.lchild is not None and self.rchild is not None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        if self.lchild is not None:
            return 1 + self.lchild.get_height()
        if self.rchild is not None:
            return 1 + self.rchild.get_height()
        return 1


class Tree:
    """A binary search tree"""
    def __init__(self):
        self.root = None

    def print(self, level):
        """Prints"""
        if self.root:
            self.root.print_node(level)

    def get_height(self):
        """Returns the height"""
        if not self.root:
            return 0
        return self.root.get_height()

    def insert(self, data):
        """Inserts data"""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        parent = self.root
        curr = self.root
        while curr is not None:
            parent = curr
            if data < curr.data:
                curr = curr.lchild
            else:
                curr = curr.rchild

        if data < parent.data:
            parent.lchild = new_node
        else:
            parent.rchild = new_node

    def range(self):
        """Returns the maximum value minus the minimum value"""
        if self.root is None:
            return None

        curr = self.root
        while curr.lchild is not None:
            curr = curr.lchild
        min_val = curr.data

        curr = self.root
        while curr.rchild is not None:
            curr = curr.rchild
        max_val = curr.data

        return max_val - min_val

    def get_level(self, level):
        """Returns a list of node values at a given level"""
        res = []
        self._get_level_helper(self.root, 0, level, res)
        return res

    def _get_level_helper(self, node, current_level, target_level, res):
        """Helper method to recursively find nodes at a specific level"""
        if node is None:
            return
        if current_level == target_level:
            res.append(node)
        else:
            self._get_level_helper(node.lchild, current_level + 1, target_level, res)
            self._get_level_helper(node.rchild, current_level + 1, target_level, res)

    def left_side_view(self):
        """Returns the list of node values visible"""
        res = []
        self._left_side_view_helper(self.root, 0, res)
        return res

    def _left_side_view_helper(self, node, level, res):
        """Helper method to construct the left side view of the tree"""
        if node is None:
            return

        if level == len(res):
            res.append(node.data)

        self._left_side_view_helper(node.lchild, level + 1, res)
        self._left_side_view_helper(node.rchild, level + 1, res)

    def sum_leaf_nodes(self):
        """Returns the sum of the values of all leaf nodes"""
        return self._sum_leaf_nodes_helper(self.root)

    def _sum_leaf_nodes_helper(self, node):
        """Helper method to recursively sum the leaf nodes"""
        if node is None:
            return 0
        if node.lchild is None and node.rchild is None:
            return node.data
        return self._sum_leaf_nodes_helper(node.lchild) + self._sum_leaf_nodes_helper(node.rchild)


def make_tree(data):
    """Creates a tree"""
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


if __name__ == '__main__':
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    if line:
        line = line.strip()
        line = line.split()
        tree1_input = list(map(int, line))
        t1 = make_tree(tree1_input)
        t1.print(t1.get_height())

        print('Tree range is: ',   t1.range())
        print('Tree left side view is: ', t1.left_side_view())
        print('Sum of leaf nodes is: ', t1.sum_leaf_nodes())
        print('##########################')

    # Another Tree for test.
    line = sys.stdin.readline()
    if line:
        line = line.strip()
        line = line.split()
        tree2_input = list(map(int, line))
        t2 = make_tree(tree2_input)
        t2.print(t2.get_height())

        print('Tree range is: ',   t2.range())
        print('Tree left side view is: ', t2.left_side_view())
        print('Sum of leaf nodes is: ', t2.sum_leaf_nodes())
        print('##########################')

    # Another Tree
    line = sys.stdin.readline()
    if line:
        line = line.strip()
        line = line.split()
        tree3_input = list(map(int, line))
        t3 = make_tree(tree3_input)
        t3.print(t3.get_height())

        print('Tree range is: ',   t3.range())
        print('Tree left side view is: ', t3.left_side_view())
        print('Sum of leaf nodes is: ', t3.sum_leaf_nodes())
        print('##########################')
