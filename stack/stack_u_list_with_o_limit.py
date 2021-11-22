class Stack:
    def __init__(self):
        self.list: list = []

    def __str__(self) -> str:
        return '\n'.join([str(x) for x in self.list])

    def is_empty(self) -> bool:
        return True if self.list == [] else False

    def push(self, value) -> bool:
        self.list.append(value)
        return True

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


stack = Stack()
assert stack.is_empty() is True
for _ in range(1, 6):
    assert stack.push(_) is True
print(stack)
assert stack.is_empty() is False
for _ in range(5):
    assert stack.pop()
try:
    assert stack.pop()
except IndexError:
    pass
else:
    raise Exception
stack.delete()
