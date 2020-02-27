import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BinarySearchTree(value)
        if value < self.value and self.left is None:
            self.left = new_node
        elif value < self.value:
            self.left.insert(value)
        elif value >= self.value and self.right is None:
            self.right = new_node
        elif value >= self.value:
            self.right.insert(value)
        else:
            return None
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        else:
            return False
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        node.in_order_print(node.left)
        print(node.value)
        node.in_order_print(node.right)
        

        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bft_queue = Queue()
        bft_queue.enqueue(node)
        while bft_queue.len() > 0:
            value = bft_queue.dequeue()
            print(value.value)
            if value.left is not None:
                bft_queue.enqueue(value.left)
            if value.right is not None:
                bft_queue.enqueue(value.right)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        dft_stack = Stack()
        dft_stack.push(node)
        while dft_stack.len() > 0:
            value = dft_stack.pop()
            print(value.value)
            if value.right is not None:
                dft_stack.push(value.right)
            if value.left is not None:
                dft_stack.push(value.left)

        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


Test_bst = BinarySearchTree(1)
Test_bst.insert(8)
Test_bst.insert(5)
Test_bst.insert(7)
Test_bst.insert(6)
Test_bst.insert(3)
Test_bst.insert(4)
Test_bst.insert(2)

# Test_bst.in_order_print(Test_bst)
# Test_bst.bft_print(Test_bst)
Test_bst.dft_print(Test_bst)