class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, _id: str):
        self.queue.insert(0, _id)

    def dequeue_cat(self):
        for index, _id in enumerate(self.queue):
            if _id.startswith("CAT"):
                return self.queue.pop(index)

    def dequeue_dog(self):
        for index, _id in enumerate(self.queue):
            if _id.startswith("DOG"):
                return self.queue.pop(index)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)


q = Queue()

q.enqueue("CAT001")
q.enqueue("CAT005")
q.enqueue("DOG789")
q.enqueue("DOG456")
assert q.dequeue() == "DOG456"
assert q.dequeue_cat() == "CAT005"
assert q.dequeue_dog() == "DOG789"
assert len(q.queue) == 1
