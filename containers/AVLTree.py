'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions
in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()
        if xs:
            for e in xs:
                self.insert(e)

#        while not self.is_avl_satisfied():
#            AVLTree._rebalance(self.root)

        # i think there should be a rotation here

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a
        balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        res = []
        if node is not None:
            res.append(AVLTree._balance_factor(node))
            res.append(AVLTree._balance_factor(node.left))
            res.append(AVLTree._balance_factor(node.right))
        ls = [factor in [-1, 0, 1] for factor in res]
        if False in ls:
            return False
        return True

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        pivot = node.right
        if pivot.left:
            left = pivot.left
        else:
            left = None
        og_value = node.value
        node.value = pivot.value
        node.right = pivot.right
        pivot = node.left
        node.left = Node(og_value, pivot, left)
        return node

    @staticmethod
    def _right_rotate(node):

        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        pivot = node.left
        if pivot.right:
            right = pivot.right
        else:
            right = None
        og_value = node.value
        node.value = pivot.value
        node.left = pivot.left
        pivot = node.right
        node.right = Node(og_value, right, pivot)
        return node

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to
        insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert
        function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            AVLTree._insert(self.root, value)
            while not self.is_avl_satisfied:
                AVLTree._rebalance(self.root)
        else:
            self.root = Node(value)
        return

    @staticmethod
    def _insert(node, value):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                AVLTree._insert(node.left, value)

        elif value > node.value:
            if not node.right and value > node.value:
                node.right = Node(value)
            else:
                AVLTree._insert(node.right, value)

        while not AVLTree._is_avl_satisfied(node):
            AVLTree._rebalance(node)
        return

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                AVLTree._right_rotate(node)
