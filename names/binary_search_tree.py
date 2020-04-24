# from dll_queue import Queue
# from dll_stack import Stack

from collections import deque


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self.value
        if value < node:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value, and False if it does not
    def contains(self, target):
        node = self.value
        if node == target:
            return True
        if target < node:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        node = self.value
        if self.right:
            return self.right.get_max()
        else:
            return node

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def depth_first_iterative_for_each(self, cb):
        stack = []
        stack.append(self.value)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_first_iterative_for_each(self, cb):
        queue = deque()
        queue.append(self.value)
        while len(queue) > 0:
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # create queue (imported)
    #     # add root to queue
    #     queue = Queue()
    #     queue.enqueue(node)
    #     # while queue not empty
    #     while queue.size > 0:
    #         # node = head of queue
    #         popped = queue.dequeue()
    #         # print node / return node if search value = target
    #         print(popped.value)
    #         # add children of node to queue
    #         if popped.left:
    #             queue.enqueue(popped.left)
    #         if popped.right:
    #             queue.enqueue(popped.right)
    #     return

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # create stack (imported)
    #     # add root to stack
    #     stack = Stack()
    #     stack.push(node)
    #     # while stack not empty
    #     while stack.size > 0:
    #         # node = pop head of stack
    #         popped = stack.pop()
    #         # print node / return node if search value = target
    #         print(popped.value)
    #         # add children of node to stack
    #         if popped.left:
    #             stack.push(popped.left)
    #         if popped.right:
    #             stack.push(popped.right)
    #     return

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     if node:
    #         print(node.value)
    #         node.pre_order_dft(node.left)
    #         node.pre_order_dft(node.right)

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     if node:
    #         node.post_order_dft(node.left)
    #         node.post_order_dft(node.right)
    #         print(node.value)


#
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.value = key


# def print_in_order(node):
#     if node:
#         print_in_order(node.left)
#         print(node.value)
#         print_in_order(node.right)


# def post_order(node):
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         print(node.value)


# def pre_oder(node):
#     if node:
#         print(node.value)
#         pre_oder(node.left)
#         pre_oder(node.right)
