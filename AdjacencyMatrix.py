from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np

"""An implementation of the adjacency list representation of a graph"""


class AdjacencyMatrix(Graph):

    def __init__(self, n: int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i: int, j: int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError("Invalid index")
        self.adj[i][j] = 1

    def remove_edge(self, i: int, j: int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError("Invalid index")
        if self.adj[i][j] == 1:
            self.adj[i][j] = 0
            return True
        return False

    def has_edge(self, i: int, j: int) -> bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError("Invalid index")
        return self.adj[i][j] == 1

    def out_edges(self, i) -> List:
        if i < 0 or i >= self.n:
            raise IndexError("Invalid index")
        out = ArrayList.ArrayList()
        for j in range(self.n):
            if self.adj[i][j] == 1:
                out.append(j)
        return out

    def in_edges(self, j) -> List:
        if j < 0 or j >= self.n:
            raise IndexError("Invalid index")
        inn = ArrayList.ArrayList()
        for i in range(self.n):
            if self.adj[i][j] == 1:
                inn.append(i)
        return inn

    def size(self):
        return self.n

    def bfs(self, r: int):
        traversal = []
        seen = [False] * self.n
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while q.n != 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for j in range(self.n):
                if self.adj[current][j] != 0:
                    neighbors.append(j)
            for j in neighbors:
                if not seen[j]:
                    q.add(j)
                    traversal.append(j)
                    seen[j] = True
        return traversal

    def dfs(self, r: int):
        traversal = []
        s = ArrayStack.ArrayStack()
        seen = []
        for n in range(self.n):
            seen.append(False)
        s.push(r)
        while s.n != 0:
            current = s.pop()
            if not seen[current]:
                traversal.append(current)
                seen[current] = True
            neighbors = []
            for n in range(self.n):
                if self.has_edge(current, n):
                    neighbors.append(n)
            for neighbor in neighbors[::-1]:
                if not seen[neighbor]:
                    s.push(neighbor)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s
