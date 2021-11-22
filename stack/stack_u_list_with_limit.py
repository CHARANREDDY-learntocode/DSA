class Stack:
    def __init__(self, max_size: int):
        self.list: list = []
        self.max_size = max_size

    def __str__(self) -> str:
        return '\n'.join([str(x) for x in self.list])

    def is_empty(self) -> bool:
        return True if self.list == [] else False

    def is_full(self) -> bool:
        if self.list.__len__() == self.max_size:
            return True
        return False

    def push(self, value):
        if not self.is_full():
            self.list.append(value)
        else:
            raise IndexError

    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        raise IndexError

    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        return IndexError

    def delete(self) -> bool:
        self.list = None
        return True


stack = Stack(10)
assert stack.is_empty() is True
count = 0
for value in range(1, 11):
    count += 1
    stack.push(value)
print(stack)
try:
    stack.push(11)
except IndexError:
    pass
else:
    raise Exception
assert stack.is_empty() is False
for _ in range(10):
    assert stack.pop()
try:
    assert stack.pop()
except IndexError:
    pass
else:
    raise Exception
stack.delete()
