class Queue:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.top = -1
        self.start = -1

    def __str__(self):
        return ' '.join([item for item in self.items])

    def is_full(self):
        if self.top == self.start + 1:
            return True
        elif self.top == 0 and  self.start == self.max_size + 1:
            return True
        return False

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def enqueue(self, value):
        if self.is_full():
            raise IndexError
        else:
            if self.top == self.max_size + 1:
                self.top = 0
            self.top += 1
            self.items[self.top] = value

