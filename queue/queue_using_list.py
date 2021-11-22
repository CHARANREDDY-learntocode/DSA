class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        return '\n'.join([str(val) for val in self.list])

    def is_empty(self):
        return True if len(self.list) == 0 else False

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.list.pop(0)
        else:
            raise IndexError

    def peek(self):
        if not self.is_empty():
            return self.list[0]

    def delete(self):
        self.list = None


queue = Queue()
assert queue.is_empty() is True
for _ in range(1, 6):
    queue.enqueue(_)
assert queue.is_empty() is False
for _ in range(5):
    queue.dequeue()
try:
    assert queue.dequeue()
except IndexError:
    pass
else:
    raise Exception
queue.delete()


