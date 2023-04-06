'''
This file implements the Heap data structure as a subclass of the BinaryTree.
The book implements Heaps using an *implicit* tree with an *explicit*
vector implementation, so the code in the book is likely to be less helpful
than the code for the other data structures.
The book's implementation is the traditional implementation because it
has a faster constant factor (but the same asymptotics).
This homework is using an explicit tree implementation to help
you get more practice with OOP-style programming and classes.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        self.size = 0
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can
        be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap will have
        a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether
        insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        ret = True
        if node.left:
            ret &= node.value <= node.left.value
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= node.value <= node.right.value
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        '''
        Inserts value into the heap.

        FIXME:
        Implement this function.

        HINT:
        Create a @staticmethod helper function,
        following the same pattern used in the BST and AVLTree insert
        functions.
        '''
        self.size += 1
        binary = bin(self.size)[3:]
        if self.root is None:
            self.root = Node(value)
        else:
            Heap._insert(self.root, value, binary)

    @staticmethod
    def _insert(node, value, binary):
        if binary[0] == '0':
            if len(binary) == 1:
                node.left = Node(value)
            else:
                Heap._insert(node.left, value, binary[1:])
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
        if binary[0] == '1':
            if len(binary) == 1:
                node.right = Node(value)
            else:
                Heap._insert(node.right, value, binary[1:])
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        return self.root.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        The pseudocode is
        1. remove the bottom right node from the tree
        2. replace the root node with what was formerly the bottom right
        3. "trickle down" the root node: recursively swap it with its
        largest child until the heap property is satisfied

        HINT:
        I created two @staticmethod helper functions:
        _remove_bottom_right and _trickle.
        It's possible to do it with only a single helper
        (or no helper at all),
        but I personally found dividing up the code into two made the
        most sense.
        '''
        binary = bin(self.size)
        self.size -= 1
        if len(binary) <= 3:
            self.root = None
            self.size = 0
        else:
            self.root.value = Heap._remove_smallest(self.root, binary[3:])
            Heap._trickle(self.root)

    @staticmethod
    def _remove_smallest(node, binary):
        if binary[0] == '0':
            if len(binary) == 1:
                value = node.left.value
                node.left = None
                return value
            else:
                return Heap._remove_smallest(node.left, binary[1:])
        if binary[0] == '1':
            if len(binary) == 1:
                value = node.right.value
                node.right = None
                return value
            else:
                return Heap._remove_smallest(node.right, binary[1:])

    @staticmethod
    def _trickle(node):
        if node.left and node.right:
            if node.left.value < node.right.value:
                if node.left.value < node.value:
                    node.value, node.left.value = node.left.value, node.value
                    return Heap._trickle(node.left)
            else:
                if node.right.value < node.value:
                    node.value, node.right.value = node.right.value, node.value
                    return Heap._trickle(node.right)
        elif node.left:
            if node.left.value < node.value:
                node.value, node.left.value = node.left.value, node.value
                return Heap._trickle(node.left)
        elif node.right:
            if node.right.value < node.value:
                node.value, node.right.value = node.right.value, node.value
                return Heap._trickle(node.right)
        return
