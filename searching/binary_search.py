def binary_search(sequence: list, start_index, last_index, value):
    if start_index > last_index:
        return -1
    else:
        middle = (start_index + last_index) // 2
        if sequence[middle] == value:
            return middle
        elif sequence[middle] < value:
            return binary_search(sequence, middle+1, last_index, value)
        else:
            return binary_search(sequence, start_index, middle-1, value)


print(binary_search([1, 3, 4, 5, 6, 8, 9,10, 11], 0, 7, 10))

