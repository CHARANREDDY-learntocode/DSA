class HeapNode:
    def __init__(self, size: int):
        self.custom_list = [None] * (size + 1)
        self.heap_size = 0
        self.max_size = size + 1


def peek_of_heap(root_node: HeapNode):
    if root_node:
        return root_node.custom_list[1]


def size_of_heap(root_node: HeapNode):
    if root_node:
        return root_node.heap_size


def level_order_traversal(root_node: HeapNode):
    if root_node:
        print(root_node.custom_list[1:root_node.heap_size + 1])


def heapify_tree_insert(root_node: HeapNode, index, heap_type):
    parent_index = int(index / 2)
    if index <= 1:
        return
    elif heap_type == "min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == "max":
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)


def insert_node(root_node: HeapNode, node_value, heap_type="min"):
    if root_node.max_size == (root_node.heap_size + 1):
        return "the binary heap is full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)


def heapify_tree_extract(root_node: HeapNode, index, heap_type):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0
    if root_node.heap_size < left_index:
        return
    elif root_node.heap_size == left_index:
        if heap_type == "min":
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                temp = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = root_node.custom_list[index]
                root_node.custom_list[index] = temp
            return
        if heap_type == "max":
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                temp = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = root_node.custom_list[index]
                root_node.custom_list[index] = temp
            return
    else:
        if heap_type == "min":
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp
        else:
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] > root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp
        heapify_tree_extract(root_node, swap_child, heap_type)


def extract_node(root_node: HeapNode, heap_type="min") -> HeapNode:
    if root_node.heap_size:
        _extract_node = root_node.custom_list[1]
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        root_node.custom_list[root_node.heap_size] = None
        root_node.heap_size -= 1
        heapify_tree_extract(root_node, 1, heap_type)
        return _extract_node


def delete_heap(root_node: HeapNode):
    root_node.custom_list = [] * (root_node.heap_size+1)
    root_node.heap_size = 0
    print("deleted successfully")


root_heap = HeapNode(8)
# print(size_of_heap(root_heap))
insert_node(root_heap, 55)
insert_node(root_heap, 95)
insert_node(root_heap, 105)
insert_node(root_heap, 97)
insert_node(root_heap, 98)
insert_node(root_heap, 115)
insert_node(root_heap, 125)
insert_node(root_heap, 61)
level_order_traversal(root_heap)

# # ###########################
# print(extract_node(root_heap))
# level_order_traversal(root_heap)
# print(extract_node(root_heap))
# level_order_traversal(root_heap)
# delete_heap(root_heap)
# level_order_traversal(root_heap)
