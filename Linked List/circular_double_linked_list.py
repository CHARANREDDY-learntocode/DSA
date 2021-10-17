class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head is None:
            return 0
        else:
            node = self.head
            count = 0
            while node:
                count += 1
                if node.next == self.head:
                    return count
                node = node.next
            return count

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def __str__(self):
        lst = list()
        node = self.head
        while node:
            lst.append(node.value)
            if node.next == self.head:
                break
            node = node.next
        return str(lst)

    def traverse(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            if node.next == self.head:
                break
            node = node.next
        print()

    def insert(self, value, position = None):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            length = len(self)
            if position == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.head = new_node
            elif position and position < length:
                index = 1
                current_node = self.head
                while index < (position - 1):
                    index += 1
                    current_node = current_node.next
                next_node = current_node.next
                next_node.prev = new_node
                current_node.next = new_node
                new_node.prev = current_node
                new_node.next = next_node
            elif position is None or position <= length + 1:
                new_node.prev = self.tail
                new_node.next = self.head
                self.tail.next = new_node
                self.head.prev = new_node
                self.tail = new_node

    def search(self, value):
        node = self.head
        index = 1
        while node:
            if node.value == value:
                return index
            index += 1
            if node.next == self.head:
                return -1
            node = node.next
        return -1

    def update(self, value, position):
        length = len(self)
        if position > length:
            return False
        node = self.head
        index = 1
        while index <= position:
            index += 1
            node = node.next
        node.value = value
        return True

    def delete(self, position):
        length = len(self)
        if position > length:
            return False
        else:
            if position == 1 or length == 1:
                if length == 1:
                    self.head = None
                    self.tail = None
                else:
                    first_node = self.head.next
                    self.tail.next = first_node
                    first_node.prev = self.tail
                    self.head = first_node
            elif position < (length - 1):
                index = 1
                current_node = self.head
                while index < (position-1):
                    index += 1
                    current_node = current_node.next
                next_node = current_node.next
                current_node.next = next_node.next
                next_node.next.prev = current_node
            else:
                prev_node = self.tail.prev
                prev_node.next = self.head
                self.head.prev = prev_node
        return True


linked_list = LinkedList()

#insert
linked_list.insert(1)
linked_list.insert(2, 1)
linked_list.insert(3)
linked_list.insert(4, 4)
linked_list.insert(5, 1)
#travese
linked_list.traverse()
#search
print(linked_list.search(5))
print(linked_list.search(10))
#update
print(linked_list.update(100, 2))
print(linked_list.update(200, 10))
#delete
print(linked_list.delete(2))
print(linked_list.delete(10))
print(linked_list)


