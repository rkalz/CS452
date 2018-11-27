import os

RED = 0
BLACK = 1


class RedBlackTree:
    class RedBlackTreeNode:
        def __init__(self, key):
            self.key = key
            self.color = RED
            self.left = None
            self.right = None
            self.parent = None

        def __repr__(self):
            return str(self.key)

    def __init__(self):
        self.root = None

    def insert(self, key):
        z = RedBlackTree.RedBlackTreeNode(key)
        self._insert(z)

    def search(self, key):
        node = self.root
        while node is not None:
            if node.key == key:
                return True
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return False

    def _insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self._insert_fixup(z)

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def _insert_fixup(self, z):
        while z is not self.root and z.parent.color == RED:
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y and y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y and y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)

        self.root.color = BLACK


def get_numbers(filename):
    with open(os.path.dirname(os.path.realpath(__file__)) + "/" + filename) as f:
        lines = f.readlines()

    numbers = []
    lines = [line.strip() for line in lines]
    for line in lines:
        nums = line.split(' ')
        for num in nums:
            numbers.append(int(num))

    return numbers


if __name__ == "__main__":
    numbers_to_insert = get_numbers("Q5.txt")
    tree = RedBlackTree()
    for num in numbers_to_insert:
        tree.insert(num)

    numbers_to_find = get_numbers("search.txt")
    for num in numbers_to_find:
        if tree.search(num):
            print("found", str(num))
        else:
            print("did not find", str(num))
