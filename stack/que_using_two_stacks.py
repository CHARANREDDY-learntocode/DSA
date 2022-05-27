class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, item: any):
        return self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        return self.in_stack.push(item)

    def dequeue(self):
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        item = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return item


queue = Queue()
queue.enqueue(123)
queue.enqueue(34)
queue.enqueue(7889)
assert queue.dequeue() == 123
assert queue.dequeue() == 34
