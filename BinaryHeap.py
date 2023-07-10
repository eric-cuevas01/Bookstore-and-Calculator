import numpy as np
from math import log2, floor
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i - 1) // 2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            raise IndexError("Binary heap is empty")
        min_val = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        if 3 * self.n < len(self.a):
            # self._resize()
            pass
        return min_val

    def depth(self, i) -> int:
        depth = 0
        hat = 0
        while self.a[hat] != i:
            hat += 1
        while self.a[hat] != self.a[0]:
            hat = parent(hat)
            depth += 1
        return depth

    def height(self) -> int:
        return floor(log2(self.n - 1))

    def bf_order(self) -> list:
        return list(self.a[0:self.n])

    def in_order(self) -> list:
        def in_order_in(ind: int):
            nodes = []
            if left(ind) < self.n:
                nodes.extend(in_order_in(left(ind)))
            nodes.append(self.a[ind])
            if right(ind) < self.n:
                nodes.extend(in_order_in(right(ind)))
            return nodes

        return in_order_in(0)

    """def in_order(self) -> list:
        def _in_order(i):
            result = []
            if i >= self.n:
                return result
            result += _in_order(left(i))
            result.append(self.a[i])
            result += _in_order(right(i))
            return result"""

    def post_order(self) -> list:
        def ahh(noo: int):
            nodes = []
            if left(noo) < self.n:
                nodes.extend(ahh(left(noo)))
            if right(noo) < self.n:
                nodes.extend(ahh(right(noo)))
            nodes.append(self.a[noo])
            return nodes

        return ahh(0)

    def pre_order(self) -> list:
        def wtf(born: int):
            nodes = []
            nodes.append(self.a[born])
            if left(born) < self.n:
                nodes.extend(wtf(left(born)))
            if right(born) < self.n:
                nodes.extend(wtf(right(born)))
            return nodes

        return wtf(0)

    """def pre_order(self) -> list:
        def _pre_order(i):
            result = []
            if i >= self.n:
                return result
            result.append(self.a[i])
            result += _pre_order(left(i))
            result += _pre_order(right(i))
            return result"""

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0:
            raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        dude = self.n - 1
        fathomIndexComplex = parent(dude)
        while dude > 0 and self.a[dude] < self.a[fathomIndexComplex]:
            self.a[dude], self.a[fathomIndexComplex] = self.a[fathomIndexComplex], self.a[dude]
            dude = fathomIndexComplex
            fathomIndexComplex = parent(dude)

    def _resize(self):
        g = _new_array(max(1, 2 * self.n))
        for j in range(self.n):
            g[j] = self.a[j]
        self.a = g

    def _trickle_down_root(self):
        him = 0
        js = left(him)
        ab = right(him)
        while him < self.n and js <= self.n and ab <= self.n \
                and (self.a[him] > self.a[js] or self.a[him] > self.a[ab]):
            bomb = {him: self.a[him], js: self.a[js], ab: self.a[ab]}
            dwarf = min(bomb, key=bomb.get)
            self.a[him], self.a[dwarf] = self.a[dwarf], self.a[him]
            him = dwarf
            js = left(him)
            ab = right(him)

    def __str__(self):
        return str(self.a[0:self.n])
