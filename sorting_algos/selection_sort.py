def selection_sort(sequence: list):
    for i in range(len(sequence)):
        min_index = i
        for j in range(i + 1, len(sequence)):
            if sequence[min_index] > sequence[j]:
                min_index = j
        sequence[i], sequence[min_index] = sequence[min_index], sequence[i]
    return sequence


print(selection_sort([1, 4, 5, 8, 3, 2, 7, 6]))
