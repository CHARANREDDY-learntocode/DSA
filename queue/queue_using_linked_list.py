from linked_list.single_linked_list import LinkedList


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self):
        self.items: LinkedList = LinkedList()

    def __str__(self):
        return " ".join([str(item.value) for item in self.items])

    def enqueue(self, value):
        self.items.insert(value)

    def dequeue(self):
        if not self.is_empty():
            self.items.delete(len(self.items))
        else:
            print("The queue is empty")

    def is_empty(self):
        if self.items.head:
            return False
        return True

    def peek(self):
        if self.items.head:
            return self.items.head.value
        raise IndexError("The Queue is empty")

    def delete(self):
        self.items.head = None
        self.items.tail = None


queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
print(queue.peek())
queue.enqueue(15)
queue.dequeue()
queue.enqueue(20)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue)