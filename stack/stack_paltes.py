class StackPlates:
    def __init__(self, stack_size: int):
        self.stack_size = stack_size
        self.stacks = []

    def push(self, item: any):
        if len(self.stacks) <= 0:
            self.stacks.append([item])
        elif len(self.stacks[-1]) == self.stack_size:
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)
        return item

    def pop(self):
        if len(self.stacks) > 0:
            if len(self.stacks[-1]) == 1:
                last = self.stacks[-1].pop()
                del self.stacks[-1]
                return last
            else:
                return self.stacks[-1].pop()

    def pop_at(self, stack_number: int):
        if len(self.stacks) >= (stack_number-1):
            if len(self.stacks[stack_number]) > 1:
                last = self.stacks[stack_number].pop()
                del self.stacks[stack_number]
                return last
            return self.stacks[stack_number].pop()


stack = StackPlates(2)
for _ in range(10):
    stack.push(_)

assert stack.stacks.__len__() == 5

assert stack.pop() == 9
assert stack.pop() == 8
assert stack.stacks.__len__() == 4

assert stack.pop() == 7
assert stack.stacks.__len__() == 4

assert stack.pop_at(2) == 5







