from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        """
        If the key does not exist in this BinarySearchTree,
        adds a new node with given key and value, in the correct position.
        Returns True if the key-value pair was added to the tree, False otherwise.
        """
        u = self._find_eq(key)
        if u is not None:
            return False
        else:
            u = self.Node(key, value)
            if self.r is None:
                self.r = u
            else:
                self._add_child(self._find_last(key), u)
            self.n += 1
            return True

    def find(self, key: object) -> object:
        """
        returns the value corresponding to the given key if the key
        exists in the BinarySearchTree, None otherwise
        """
        u = self._find_eq(key)
        if u is None:
            return None
        else:
            return u.v

    def remove(self, key: object):
        """
        removes the node with given key if it exists in this BinarySearchTree.
        Returns the value corresponding to the removed key, if the key was in the tree.
        If given key does not exist in the tree, ValueError is raised.
        """
        u = self._find_eq(key)
        if u is None:
            raise ValueError("Node with given key does not exist in the tree")
        value = u.v
        self._remove_node(u)
        return value

    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key,
        None otherwise.
        """
        u = self.r
        while u is not None:
            if key == u.k:
                return u
            elif key < u.k:
                u = u.left
            else:
                u = u.right
        return None

    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node
        with the given key, if it existed
        """
        w = None
        u = self.r
        while u is not None:
            if key == u.k:
                return u
            elif key < u.k:
                w = u
                u = u.left
            else:
                w = u
                u = u.right
        return w

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        helper method; adds node u as the child of node p, assuming node p has at most 1 child
        """
        if u.k == p.k:
            p.v = u.v
            return False
        elif u.k < p.k:
            if p.left is None:
                p.insert_left(u)
            else:
                self._add_child(p.left, u)
        else:
            if p.right is None:
                p.insert_right(u)
            else:
                self._add_child(p.right, u)
        return True

    def _splice(self, u: BinaryTree.Node):
        """
        helper method; links the parent of given node u to the child
        of node u, assuming u has at most one child
        """
        p = u.parent
        if u.left is not None:
            c = u.left
        else:
            c = u.right
        if c is not None:
            c.parent = p
        if p is None:
            self.r = c
        elif u == p.left:
            p.left = c
        else:
            p.right = c
        u.left = u.right = u.parent = None

    def _remove_node(self, u: BinaryTree.Node):
        if u.left is None or u.right is None:
            self._splice(u)
        else:
            w = u.right
            while w.left is not None:
                w = w.left
            u.k, u.v = w.k, w.v
            self._splice(w)
        self.n -= 1
        return u.v

    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def r_node(self, key):
        """
        get_node_with_key_or_smallest_larger_key: Returns the node containing the given key if it exists;
        otherwise it returns the node with the smallest key greater than the given key.
        input:
            key: the key to search for
        output:
            Node: the node containing the given key, or the node with the smallest key greater than the given key,
                  or None if no such node exists
        """
        current = self.r
        smallest = None

        while current is not None:
            if key < current.k:
                smallest = current
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current

        return smallest
