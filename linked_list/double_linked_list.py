class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        node = self.head
        count = 0
        while node:
            count += 1
            if node.next is None:
                return count
            node = node.next
        return count

    def __str__(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.value)
            if node.next is None:
                break
            node = node.next
        return lst.__str__()

    def traverse(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            if node.next is None:
                break
            node = node.next
        print()

    def reverse_traverse(self):
        node = self.tail
        while node:
            print(node.value, end='')
            node = node.prev
            if node == self.tail:
                break
            else:
                print(' <-> ', end='')

        print()

    def add(self, values = None):
        if values is None:
            values = []
        if values:
            for value in values:
                self.insert(value)

    def insert(self, value, position=None):
        length = len(self)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if position == 1:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif position and position <= length:
                index = 1
                current_node = self.head
                while index < (position - 1):
                    index += 1
                    current_node = current_node.next
                new_node.next = current_node.next
                new_node.prev = current_node
                current_node.next.prev = new_node
                current_node.next = new_node
            elif position is None or (position == length+1):
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                raise IndexError("Index out of range")

    def search(self, value):
        if self.head is None:
            return -1
        else:
            node = self.head
            index = 1
            while node:
                if value == node.value:
                    return index
                index += 1
                node = node.next
            return -1

    def update(self, position, value):
        if self.head is None or position > len(self):
            return False
        else:
            node = self.head
            index = 1
            while index < position:
                index += 1
                node = node.next
            node.value = value
            return True

    def delete(self, position):
        length = len(self)
        if self.head is None:
            return False
        elif  position > length:
            raise IndexError("Index out of range")
        else:
            if position == 1:
                if length == 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head.next.prev = None
                    self.head = self.head.next
            elif position < (length - 1):
                index = 1
                current_node = self.head
                while index < (position - 1):
                    index += 1
                    current_node = current_node.next
                current_node.next = current_node.next.next
                current_node.next.next.prev = current_node
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        return True


linked_list = LinkedList()
#insert
print(linked_list)
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
linked_list.insert(6, 1)
linked_list.insert(7, 4)
linked_list.insert(8, 8)
linked_list.insert(9, 9)
print(linked_list)
#traverse
linked_list.traverse()
print([node.value for node in linked_list])
#search
print(linked_list.search(5))
print(linked_list.search(20))
#update
print(linked_list.update(3, 300))
print(linked_list.update(1, 100))
print(linked_list.update(len(linked_list), 400))
print(linked_list.update(20, 100))
print(linked_list)
#delete
print(linked_list.delete(1))
print(linked_list.delete(3))
print(linked_list.delete(len(linked_list)))
# print(linked_list.delete(100))
print(linked_list)

