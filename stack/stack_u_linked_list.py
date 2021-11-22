class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.linked_list: LinkedList = LinkedList()

    def __str__(self):
        return '\n'.join([str(node.value) for node in self.linked_list])

    def is_empty(self) -> bool:
        return True if self.linked_list.head is None else False

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):
        if self.is_empty():
            raise IndexError
        else:
            value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return value

    def peek(self):
        if self.linked_list.head:
            return self.linked_list.head.value
        else:
            raise Exception

    def delete(self):
        self.linked_list.head = None


stack = Stack()
assert stack.is_empty() is True
for _ in range(1, 6):
    stack.push(_)
print(stack)
assert stack.is_empty() is False
print(stack.peek())
for _ in range(5):
    stack.pop()
try:
    assert stack.pop()
except IndexError:
    pass
else:
    raise Exception
stack.delete()
