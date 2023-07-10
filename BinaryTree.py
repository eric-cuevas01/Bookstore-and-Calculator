from SLLQueue import SLLQueue
from Interfaces import Tree


class BinaryTree(Tree):
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val

        def set_key(self, x):
            self.k = x

        def set_val(self, v):
            self.v = v

        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left

        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right

        def __str__(self):
            return f"({self.k}, {self.v})"

    def __init__(self):
        self.root = None
        self.r = None

    def depth(self, u: Node) -> int:
        if u is None:
            return -1
        else:
            return 1 + self.depth(u.parent)

    def height(self) -> int:
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        if u is None:
            return -1
        else:
            return 1 + max(self._height(u.left), self._height(u.right))

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        if u is None:
            return 0
        else:
            return 1 + self._size(u.left) + self._size(u.right)

    def bf_order(self):
        if self.r is None:
            return []
        q = SLLQueue()
        q.add(self.r)
        res = []
        while q.size() > 0:
            u = q.remove()
            res.append(u)
            if u.left is not None:
                q.add(u.left)
            if u.right is not None:
                q.add(u.right)
        return res

    def in_order(self) -> list:
        return self._in_order(self.r)

    def _in_order(self, u: Node) -> list:
        nodes = []
        if u:
            nodes.extend(self._in_order(u.left))
            nodes.append(u)
            nodes.extend(self._in_order(u.right))
        return nodes

    def post_order(self) -> list:
        return self._post_order(self.r)

    def _post_order(self, u: Node):
        nodes = []
        if u:
            nodes.extend(self._post_order(u.left))
            nodes.extend(self._post_order(u.right))
            nodes.append(u)
        return nodes

    def pre_order(self) -> list:
        return self._pre_order(self.r)

    def _pre_order(self, u: Node):
        nodes = []
        if u:
            nodes.append(u)
            nodes.extend(self._pre_order(u.left))
            nodes.extend(self._pre_order(u.right))
        return nodes

    def __str__(self):
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)

    def searchSmallestGreaterThanOrEqual(self, prefix):
        """Searches for the smallest node with a key greater than or equal to the given prefix."""
        if self.root is None:
            return None  # If the tree is empty, return None

        curr = self.root  # Start from the root of the tree
        result = None  # Variable to store the result

        while curr is not None:
            if curr.k >= prefix:
                # If the current node's key is greater than or equal to the prefix,
                # update the result and move to the left subtree
                result = curr
                curr = curr.left
            else:
                # If the current node's key is less than the prefix,
                # move to the right subtree
                curr = curr.right

        return result  # Return the result node
