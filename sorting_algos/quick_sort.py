# def partition(sub_sequence, low, high):
#     i = low - 1
#     pivot = sub_sequence[high]
#     for j in range(low, high):
#         if sub_sequence[j] <= pivot:
#             i += 1
#             sub_sequence[i], sub_sequence[j] = sub_sequence[j], sub_sequence[i]
#     sub_sequence[i+1], sub_sequence[high] = sub_sequence[high], sub_sequence[i+1]
#     return i+1
#
#
# def quick_sort(sequence, low, high):
#     if low <= high:
#         pi = partition(sequence, low, high)
#         quick_sort(sequence, low, pi-1)
#         quick_sort(sequence, pi+1, high)
#     return sequence
#
#
# print(quick_sort([1, 6, 7, 2, 3, 9, 0, 5], 0, 7))


def partition(sequence, low, high):
    pivot = sequence[low]
    i = low
    j = high
    while i < j:
        while sequence[i] <= pivot:
            i += 1
        while sequence[j] > pivot:
            j -= 1
        if i < j:
            sequence[i], sequence[j] = sequence[j], sequence[i]
    sequence[low], sequence[j] = sequence[j], sequence[low]
    return j


def quick_sort(sequnce, low, high):
    if low < high:
        pi = partition(sequnce, low, high)
        quick_sort(sequnce, low, pi)
        quick_sort(sequnce, pi+1, high)
    return sequnce


print(quick_sort([1, 6, 7, 2, 3, 9, 0, 5], 0, 7))
