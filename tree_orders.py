# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not(self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

class TreeOrders:
    def __init__(self):
        self.root = None
        self.n = None
        self.key = None
        self.left = None
        self.right = None
        self.result = None
        self.build_array = None


    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c


    def in_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result


    def pre_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result


    def post_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result


def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.in_order()))
	print(" ".join(str(x) for x in tree.pre_order()))
	print(" ".join(str(x) for x in tree.post_order()))

threading.Thread(target=main).start()
