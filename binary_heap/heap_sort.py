def heapify(custom_list: list, n: int, i: int):
    smallest = i
    left_child = 2 * i
    right_child = 2 * i + 1

    if left_child < n and custom_list[left_child] < custom_list[smallest]:
        smallest = left_child

    if right_child < n and custom_list[right_child] < custom_list[smallest]:
        smallest = right_child

    if smallest != i:
        custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
        heapify(custom_list, n, smallest)


def heap_sort(custom_list: list):
    n = len(custom_list)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(custom_list, n, i)
    for i in range(n-1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heapify(custom_list, i, 0)
    print(custom_list)


heap_sort([1, 4, 3, 7, 8, 9, 2, 0])
