

import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        if value is not None:
            self.storage.add_to_tail(value)
             
     

    def dequeue(self):
        if self.storage.head is not None:
            return self.storage.remove_from_head()
     

    def len(self):
        length = self.storage.__len__()
        return length
