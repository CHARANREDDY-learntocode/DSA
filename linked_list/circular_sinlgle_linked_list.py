class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        node = self.head
        length = 0
        while node:
            length += 1
            if node.next == self.head:
                return length
            node = node.next
        return length

    def traverse(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            if node.next == self.head:
                break
            node = node.next
        print()

    def add(self, values = None):
        if values is None:
            values = []
        if values:
            for value in values:
                self.insert(value)

    def insert(self, value, position = None):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            if position == 1:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            else:
                if position and position <= (len(self) + 1):
                    index = 1
                    temp = self.head
                    while index < (position-1):
                        index += 1
                        temp = temp.next
                    new_node.next = temp.next
                    temp.next = new_node
                    if position == (len(self)):
                        self.tail = new_node

                elif position is None:
                    new_node.next = self.tail.next
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                    raise IndexError("Index out of range")

    def search(self, value):
        if self.head is None:
            return -1
        node = self.head
        index = 1
        while node:
            if node.value == value:
                return index
            index += 1
            node = node.next
            if node == self.head:
                return -1

    def delete(self, position):
        if position > self.__len__() or self.head is None:
            raise IndexError("Index out of range")
        else:
            if position == 1:
                self.head = self.head.next
                self.tail = self.head
                node = self.head
                while node.next.next != self.head:
                    node = node.next
                node.next = self.head
                self.tail = node
            else:
                index = 1
                node = self.head
                while index < (position-1):
                    index += 1
                    node = node.next
                node.next = node.next.next
            return True

    def update(self, position, value):
        if position > len(self):
            raise IndexError("Index out of range")
        else:
            index = 1
            node = self.head
            while index != position:
                index += 1
                node = node.next
            node.value = value
            return True


linked_list = LinkedList()

linked_list.insert(1)
linked_list.traverse()
linked_list.insert(2)
linked_list.traverse()
linked_list.insert(3)
linked_list.traverse()
linked_list.insert(4, 2)
linked_list.traverse()
# linked_list.insert(5, 10)
# linked_list.insert(10, 1)
linked_list.traverse()
linked_list.insert(5, 1)
linked_list.traverse()
linked_list.insert(6, 4)
linked_list.traverse()
linked_list.insert(7, 3)
linked_list.traverse()
linked_list.insert(8, 2)
linked_list.traverse()
linked_list.insert(10)
linked_list.insert(9, 1)
linked_list.traverse()
linked_list.insert(11, 1)
linked_list.insert(12, 7)
linked_list.insert(13, 13)
linked_list.traverse()
linked_list.insert(14)
linked_list.traverse()
#search
print(linked_list.search(13))
print(linked_list.search(20))
#update
print(linked_list.update(13, 100))
# print(linked_list.update(20, 5))
#delete
print("Before deleting, length: ", len(linked_list))
print(linked_list.delete(13))
print(linked_list.delete(1))
print(linked_list.delete(len(linked_list)))
# print(linked_list.delete(100))
linked_list.traverse()
print('After deleting, length: ', len(linked_list))