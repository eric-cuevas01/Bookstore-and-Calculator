"""Implementations of some sorting"""
import random

from ArrayList import ArrayList
from Interfaces import List


def linear_search(a: List, x):
    for i in range(a.size()):
        if a.get(i) == x:
            return i
    return None


def binary_search(a: List, x):
    lo = 0
    hi = a.size() - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a.get(mid) == x:
            return mid
        elif a.get(mid) < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def _merge(a0: List, a1: List, a: List):
    i = 0
    j = 0
    while i < a0.size() and j < a1.size():
        if a0.get(i) < a1.get(j):
            a.set(i + j, a0.get(i))
            i += 1
        else:
            a.set(i + j, a1.get(j))
            j += 1
    while i < a0.size():
        a.set(i + j, a0.get(i))
        i += 1
    while j < a1.size():
        a.set(i + j, a1.get(j))
        j += 1


def merge_sort(a: List):
    n = a.size()
    if n > 1:
        mid = n // 2
        left = ArrayList()
        right = ArrayList()
        for i in range(mid):
            left.add(i, a.get(i))
        for i in range(mid, n):
            right.add(i - mid, a.get(i))
        merge_sort(left)
        merge_sort(right)
        _merge(left, right, a)


def _quick_sort_f(a: List, start, end):
    if start < end:
        pivot = start
        i = start + 1
        j = end
        while i <= j:
            if a.get(i) <= a.get(pivot):
                i += 1
            elif a.get(j) > a.get(pivot):
                j -= 1
            else:
                a.set(i, a.set(j, a.get(i)))
        a.set(pivot, a.set(j, a.get(pivot)))
        _quick_sort_f(a, start, j - 1)
        _quick_sort_f(a, j + 1, end)


def _quick_sort_r(a: List, start, end):
    if start < end:
        pivot = random.randint(start, end)
        a.set(start, a.set(pivot, a.get(start)))
        i = start + 1
        j = end
        while i <= j:
            if a.get(i) <= a.get(start):
                i += 1
            elif a.get(j) > a.get(start):
                j -= 1
            else:
                a.set(i, a.set(j, a.get(i)))
                i += 1
                j -= 1
        a.set(start, a.set(j, a.get(start)))
        _quick_sort_r(a, start, j - 1)
        _quick_sort_r(a, j + 1, end)


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)
