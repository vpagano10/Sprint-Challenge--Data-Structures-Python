from doubly_linked_list import DoublyLinkedList
'''
Node params:
- prev item
- next item

dll params:
- head
- tail
- length

dll methods:
- add_to_head
- remove_from_head
- add_to_tail
- remove_from_tail
- move_to_front
- move_to_end
- delete
- get_max
'''


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # similar to LRU append
    def append(self, item):
        # if there's room, add the item to the front, return
        storage = self.storage
        capacity = self.capacity
        if storage.length < capacity:
            storage.add_to_head(item)
            return
        # if no more room
        if storage.length == capacity:
            # cannot display None, so it current == None, set it to the tail node
            if self.current == None:
                self.current = storage.tail
            # if current value given a value != None, passed by item being appended
            self.current.value = item
            # if there is an item before the new current, set current = prev and move prev to the end
            #
            if self.current.prev:
                self.current = self.current.prev
            else:
                self.current = storage.tail
            #

    # similar to LRU get
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        selected_node = self.storage.tail
        while selected_node:
            # cannot return vales == None
            if selected_node.value != None:
                list_buffer_contents.append(selected_node.value)
            selected_node = selected_node.prev
        return list_buffer_contents


# ----------------Stretch Goal-------------------
class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
