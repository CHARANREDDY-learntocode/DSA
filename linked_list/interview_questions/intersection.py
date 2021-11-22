from linked_list.single_linked_list import LinkedList, Node


def add_same_node(list1: LinkedList, list2: LinkedList, value) -> None:
    node = Node(value)
    list1.tail.next = node
    list2.tail.next = node
    list1.tail = node
    list2.tail = node


def intersection(list1: LinkedList, list2: LinkedList) -> (False, Node):
    if list1.tail is not list2.tail:
        return False
    list_1_length = len(list1)
    list_2_length = len(list2)
    diff = list_1_length - list_2_length
    node1 = list1.head
    node2 = list2.head
    if diff > 0:
        diff = abs(diff)
        while diff:
            node1 = node1.next
            diff -= 1
    else:
        diff = abs(diff)
        while diff:
            node2 = node2.next
            diff -= 1
    while node1:
        if node1 == node2:
            return node1
        node1 = node1.next
        node2 = node2.next


list1 = LinkedList()
list1.add([1, 2, 3])
list2 = LinkedList()
list2.add([4, 5, 6])

add_same_node(list1, list2, 10)
result = intersection(list1, list2)
if result:
    print(result.value)
else:
    print("no commom elements")