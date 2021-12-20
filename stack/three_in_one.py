class MultiStack:
    def __init__(self, stack_size, num_of_stacks):
        self.stack_size = stack_size
        self.num_of_stacks = num_of_stacks
        self.stack_list = [None]*(stack_size*num_of_stacks)
        self.sizes = [0] * num_of_stacks

    def is_full(self, stack_number):
        if self.sizes[stack_number] == self.stack_size:
            return True
        return False

    def is_empty(self, stack_number):
        if self.sizes[stack_number] == 0:
            return True
        return False

    def push(self, stack_number, value):
        if not self.is_full(stack_number):
            self.sizes[stack_number] += 1
            self.stack_list[stack_number*self.stack_size + self.sizes[stack_number] - 1] = value

    def pop(self, stack_number):
        if not self.is_empty(stack_number):
            self.sizes[stack_number] -= 1

    def peek(self, stack_nummber):
        return self.stack_list[stack_nummber*self.stack_size + ((self.sizes[stack_nummber]) - 1)]


customStack = MultiStack(3, 6)
print(customStack.is_full(0))
print(customStack.is_empty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.pop(0))