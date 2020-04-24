class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # base for recursion: current node is none
        if node == None:
            return
        # another base for recursion, we are at the last node to be reversed
        # if the current node's next is none, that is the last item and becomes the new head
        if node.next_node == None:
            self.head = node
            node.next_node = prev
            return
        # none of the ifs above are true, so must go again recursively,
        # swap the values like the previous ex, where current and previous are not passed as parameters and are incremented by passing their new values in as the new params
        # increase current node to its next
        new_node = node.next_node
        # next node becomes the prev
        node.next_node = prev
        self.reverse_list(new_node, node)

        # current = self.head
        # prev = None
        # while current is not None:
        #     next_node = current.next_node
        #     current.next_node = prev
        #     prev = current
        #     current = next_node
        # self.head = prev
