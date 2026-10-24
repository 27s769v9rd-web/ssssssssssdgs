

#  File: TestBinaryTree.py

#  Description: Implementation and testing of binary search tree methods

#  Student Name: Jeff Zheng

#  Student UT EID: jrz554

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:54970

#  Date Created: 10/22/26

#  Date Last Modified: 10/23/26

import sys

class Node(object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):
        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        if self.root:
            self.root.print_node(level)

    def get_height(self):
        if not self.root:
            return 0
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.[cite: 2]
    # The range of values equals the maximum value in the binary search tree minus the minimum value.[cite: 2]
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.[cite: 2]
    def range(self):
        if self.root is None:
            return None
        
        curr = self.root
        while curr.lChild is not None:
            curr = curr.lChild
        min_val = curr.data
        
        curr = self.root
        while curr.rChild is not None:
            curr = curr.rChild
        max_val = curr.data
        
        return max_val - min_val

    # Returns a list of nodes at a given level from left to right[cite: 2]
    def get_level(self, level):
        res = []
        self._get_level_helper(self.root, 0, level, res)
        return res

    def _get_level_helper(self, node, current_level, target_level, res):
        if node is None:
            return
        if current_level == target_level:
            res.append(node)
        else:
            self._get_level_helper(node.lChild, current_level + 1, target_level, res)
            self._get_level_helper(node.rChild, current_level + 1, target_level, res)

    # Returns the list of the node that you see from left side[cite: 2]
    # The order of the output should be from top to down[cite: 2]
    def left_side_view(self):
        res = []
        self._left_side_view_helper(self.root, 0, res)
        return res

    def _left_side_view_helper(self, node, level, res):
        if node is None:
            return
        
        if level == len(res):
            res.append(node.data)
            
        self._left_side_view_helper(node.lChild, level + 1, res)
        self._left_side_view_helper(node.rChild, level + 1, res)

    # returns the sum of the value of all leaves.[cite: 2]
    # a leaf node does not have any children.[cite: 2]
    def sum_leaf_nodes(self):
        return self._sum_leaf_nodes_helper(self.root)

    def _sum_leaf_nodes_helper(self, node):
        if node is None:
            return 0
        if node.lChild is None and node.rChild is None:
            return node.data
        return self._sum_leaf_nodes_helper(node.lChild) + self._sum_leaf_nodes_helper(node.rChild)


def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.[cite: 1]
if __name__ == '__main__':
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    if line:
        line = line.strip()
        line = line.split()
        tree1_input = list(map(int, line)) 	# converts elements into ints
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
        tree2_input = list(map(int, line)) 	# converts elements into ints
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
        tree3_input = list(map(int, line)) 	# converts elements into ints
        t3 = make_tree(tree3_input)
        t3.print(t3.get_height())

        print('Tree range is: ',   t3.range())
        print('Tree left side view is: ', t3.left_side_view())
        print('Sum of leaf nodes is: ', t3.sum_leaf_nodes())
        print('##########################')
