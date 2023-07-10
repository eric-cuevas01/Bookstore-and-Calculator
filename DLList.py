from Interfaces import List
import numpy as np


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, data):
        new_node = Node(data, None, self.head)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = Node(data, self.tail, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        return data

    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def find(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def remove(self, node):
        if node.prev is None:
            self.remove_first()
        elif node.next is None:
            self.remove_last()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node.data

    def get_size(self):
        return self.size

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + " "
            current = current.next
        return result.strip()
