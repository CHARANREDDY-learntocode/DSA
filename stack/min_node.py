class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.min_node: Node = None

    def get_min_node(self):
        if self.min_node:
            return self.min_node.value
        raise Exception

    def push(self, item):
        node = Node(item)
        if self.top:
            if self.min_node.value < item:
                self.top.next = node
                self.top = node
            else:
                self.top.next = node
                self.top = node
                self.min_node = node
        else:
            self.min_node = node
            self.top = node

    def pop(self):
        



