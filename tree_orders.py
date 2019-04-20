# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeNode:
    def __init__(self, data=None, l_child=None, r_child=None):
        self.data = data
        self.left_child = l_child
        self.right_child = r_child
        self.parent = None


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
        self.build_array = [None] * self.n
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

            new_node = self.create_node(self.key[i], self.left[i], self.right[i])
            self.build_tree(i, new_node)

    def create_node(self, key, l_ind, r_ind):
        if l_ind == -1:
            l_ind = None
        if r_ind == -1:
            r_ind = None
        temp_node = TreeNode(key, l_ind, r_ind)
        return temp_node

    def build_tree(self, cur_ind, new_node):
        if cur_ind == 0:
            self.root = new_node
            self.build_array[cur_ind] = new_node
        elif 0 < cur_ind < self.n:
            is_a_child_of = self.build_array[cur_ind]
            if is_a_child_of is None:
                self.build_array[cur_ind] = new_node
            else:
                my_parent = self.build_array[is_a_child_of]
                if my_parent.left_child == cur_ind:
                    my_parent.left_child = new_node
                elif my_parent.right_child == cur_ind:
                    my_parent.right_child = new_node

                new_node.parent = my_parent
                self.build_array[cur_ind] = new_node

        if new_node.left_child is not None:
            if new_node.left_child < cur_ind:
                my_left_child = self.build_array[new_node.left_child]
                new_node.left_child = my_left_child
            else:
                self.build_array[new_node.left_child] = cur_ind

        if new_node.right_child is not None:
            if new_node.right_child < cur_ind:
                my_right_child = self.build_array[new_node.right_child]
                new_node.right_child = my_right_child
            else:
                self.build_array[new_node.right_child] = cur_ind

    def in_order(self):
        self.result = []
        if self.root:
            self._inorder(self.root)
        return self.result

    def _inorder(self, cur_node):
        if cur_node:
            if cur_node.left_child:
                self._inorder(cur_node.left_child)
            self.result.append(cur_node.data)
            if cur_node.right_child:
                self._inorder(cur_node.right_child)

    def pre_order(self):
        self.result = []
        if self.root:
            self._preorder(self.root)

        return self.result

    def _preorder(self, cur_node):
        if cur_node:
            self.result.append(cur_node.data)
            if cur_node.left_child:
                self._preorder(cur_node.left_child)
            if cur_node.right_child:
                self._preorder(cur_node.right_child)

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

