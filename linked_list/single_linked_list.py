class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        node = self.head
        while node.next is not None:
            yield node
            node = node.next

    def insert(self, value, location=None):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if location == 1:
                if len(self) == 1:
                    self.tail = node
                    node.next = self.head
                    self.head = node
                else:
                    node.next = self.head
                    self.head = node
            else:
                temp = self.head
                index = 0
                if location and location <= len(self):
                    while index < (location - 1):
                        index += 1
                        temp = temp.next
                    next_node = temp.next
                    temp.next = node
                    node.next = next_node
                else:
                    self.tail.next = node
                    self.tail = node

    def add(self, values = None):
        if values is None:
            values = []
        if values:
            for value in values:
                self.insert(value)

    def traverse(self):
        node = self.head
        while node is not None:
            if node.next is not None:
                print(node.value, sep='', end='->')
            else:
                print(node.value)
            node = node.next

    def search(self, value):
        node = self.head
        location = 1
        while node.next is not None:
            if node.value == value:
                return location
            node = node.next
            location += 1
        return -1

    def update(self, location, value):
        if location > len(self):
            return False
        node = self.head
        index = 1
        while index < location:
            node = node.next
            index += 1
        node.value = value
        return True

    def delete(self, location):
        length = len(self)
        if location > length:
            return False
        node = self.head
        if location == 1:
            if length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif location == length:
            if length == 1:
                self.tail = None
                self.head = None
            else:
                node = self.head
                while node.next.next is not None:
                    node = node.next
                node.next = None
                self.tail = node
        else:
            index = 1
            while index < (location - 1):
                node = node.next
                index += 1
            node.next = node.next.next
        return True

    def delete_sll(self):
        self.head = None
        self.tail = None

if __name__ == "__main__":
    linked_list = LinkedList()

    # insert without any elements
    linked_list.insert(1)
    # insert at end
    linked_list.insert(2)
    # insert at high index
    linked_list.insert(3, 5)
    linked_list.insert(4)
    # insert at location specified
    linked_list.insert(5, 3)
    linked_list.insert(6, 4)
    linked_list.insert(8, 1)
    linked_list.insert(9, 1)
    linked_list.insert(10)
    linked_list.insert(11, 1)
    linked_list.insert(12, 40)

    # print values in linkedlist
    print("linked_list: ", end=" ")
    linked_list.traverse()
    print("Length of Linked List: ", len(linked_list))
    print("10 found at location ", linked_list.search(10))
    print("8 at location 3 update to 15: ", linked_list.update(3, 15))
    linked_list.traverse()
    linked_list.delete(1)
    linked_list.delete(100)
    linked_list.delete(5)
    linked_list.traverse()
    linked_list.delete(9)
    linked_list.traverse()
    linked_list.delete_sll()
    linked_list.traverse()
