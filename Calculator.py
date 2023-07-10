import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator
import re


def matched_expression(s: str) -> bool:
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0


class Calculator:
    def __init__(self):
        self.u = None
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def _build_parse_tree(self, exp: str) -> BinaryTree:
        """
        if exp is not matched, raise Error
        Let t be a binary tree
        Let the temp variable current be the root
        For every token in the expression
            If token is '(' then
                Add a left child to current and update current = current.left
            If token is either '+, -, /, *' then
                current.set_value(token)
                current.set_key(token)
                Add a right child to current and update current = current.right
            If token is a variable then
                current.set_key(token)
                current.set_val(dict.find(token))
                update current = current.parent
            If token is ')' then
                update current = current.parent
        return t
        """
        if not matched_expression(exp):
            raise ValueError
        exp = re.findall('[-+*/()]|\w+|\W+', exp)
        t = BinaryTree.BinaryTree()
        t.r = t.Node()
        current = t.r

        for token in exp:
            node = t.Node()
            if token == "(":
                current = current.insert_left(node)
            elif token == "+" or token == "-" or token == "/" or token == "*":
                current.set_val(token)
                current.set_key(token)
                current = current.insert_right(node)
            elif token.isalnum():
                current.set_val(self.dict.find(token))

                current.set_key(token)
                current = current.parent
            elif token == ")":
                current = current.parent
        return t

    def _evaluate(self, u):
        """
        op = { '+': operator.add, '-':operator.sub, '+':operator.mul, '/':operator.truediv}

        if u.left is not None and u.right is not None:
            fn = op[u.k]
            return fn(self._evaluate(u.left), self._evaluate(u.right))

        elif u.left is None and u.right is None:

            if u.v is not None:
                return u.v
            raise ValueError(f"Missing value for variable (u.k)")

        elif u.left is not None:
            return self._evaluate(u.left)

        else:
            return self._evaluate(u.right)
        """
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        if u.left is not None and u.right is not None:
            fn = op[u.k]

            return fn(self._evaluate(u.left), self._evaluate(u.right))

        elif u.left is None and u.right is None:
            if u.v is not None:
                return u.v
            raise ValueError(f"Missing value for variable {u.k}")

        elif u.left is not None:
            return self._evaluate(u.left)

        else:
            return self._evaluate(u.right)

    def evaluate(self, exp: str) -> None:
        """
        Evaluates the given expression and returns the result.
        """
        print(f'Evaluating expression: ', end='')
        self.print_expression(exp)
        return self._evaluate(self._build_parse_tree(exp).r)
        # parse_tree = self._build_parse_tree(exp)
        # return self._evaluate(parse_tree.r)

    def print_expression(self, exp: str):
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        non_variables = re.split('\w+', exp)
        new_expression = ""
        for i in range(0, len(non_variables)):
            new_expression += non_variables[i]
            if i <= len(variables) - 1:
                x = self.dict.find(variables[i])
                if x is None:
                    new_expression += variables[i]
                else:
                    new_expression += str(x)
        print(new_expression)

    def matched_expression(self: str) -> bool:
        count = 0
        for c in self:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0


def set_variable(self, k: str, v: float):
    self.dict.add(k, v)


def print_expression(self, exp: str) -> str:
    variables = [x for x in re.split('\W+', exp) if x.isalnum()]
    non_variables = re.split('\w+', exp)
    new_expression = ""
    for i in range(0, len(non_variables)):
        new_expression += non_variables[i]
        if i <= len(variables) - 1:
            x = self.dict.find(variables[i])
            if x is None:
                new_expression += variables[i]
            else:
                new_expression += str(x)
    print(new_expression)


def evaluate(self, exp: str) -> None:
    """
    Evaluates the given expression and returns the result.
    """
    parse_tree = self._build_parse_tree(exp)
    return self._evaluate(parse_tree.r)
