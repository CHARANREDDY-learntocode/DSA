from linked_list.single_linked_list import LinkedList


def remove_dups(linked_list):
    if linked_list.head is None:
        return []
    else:
        node = linked_list.head
        values = set()
        index = 1
        while node:
            if node.value in values:
                linked_list.delete(index)
            else:
                values.add(node.value)
                index += 1
            node = node.next


def remove_dups_without_buffer(linked_list):
    current_node = linked_list.head
    while current_node:
        runner_node = current_node.next
        while runner_node:
            if runner_node.value == current_node.value:
                runner_node.next = runner_node.next.next
            else:
                runner_node = runner_node.next
        current_node = current_node.next
    return linked_list


def nth_to_last(linked_list, index):
    pointer1 = linked_list.head
    pointer2 = linked_list.head
    for _ in range(index):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1.value


def nth_to_last_using_len_func(linked_list, index):
    length = len(linked_list)
    if index > length:
        return
    location = 1
    node = linked_list.head
    while (length - location) >= index:
        node = node.next
        location += 1
    return node.value


def partition(linked_list, value):
    current_node = linked_list.head
    tail_node = linked_list.head
    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < value:
            current_node.next = linked_list.head
            linked_list.head = current_node
        else:
            tail_node.next = current_node
            tail_node = current_node
        current_node = next_node

    if tail_node.next is not None:
        tail_node.next = None


def sum_lists(list1: LinkedList, list2: LinkedList):
    new_list = LinkedList()
    carry = 0
    node1 = list1.head
    node2 = list2.head
    while node1 or node2:
        digit_sum = carry
        if node1:
            digit_sum += node1.value
            node1 = node1.next
        if node2:
            digit_sum += node2.value
            node2 = node2.next
        new_list.add([int(digit_sum % 10)])
        carry = digit_sum / 10
    return new_list



# linked_list = LinkedList()
# linked_list.add([1, 1, 2, 3, 2, 56, 34, 78, 3, 6, 9, 4, 45])
# remove_dups(linked_list)
# print("With Buffer")
# linked_list.traverse()
# remove_dups_without_buffer(linked_list)
# print("Without Buffer")
# linked_list.traverse()
# print("Last 2nd value")
# print(nth_to_last(linked_list, 2))
# print(nth_to_last_using_len_func(linked_list, 2))
# print("Partition")
# partition(linked_list, 50)
# linked_list.traverse()

list1 = LinkedList()
list1.add([1,2,3])
list2 = LinkedList()
list2.add([1, 2, 3])
sum_lists(list1, list2).traverse()
