def bubble_sort(sequence: list, reverse=False):
    for i in range(len(sequence) - 1):
        swapped = False
        for j in range(len(sequence) - i - 1):
            if reverse:
                if sequence[j] < sequence[j + 1]:
                    print("here")
                    sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
            else:
                if sequence[j] > sequence[j + 1]:
                    print("here1")
                    sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
        if not swapped:
            return sequence
    return sequence


def recursive_bubble_sort(sequence: list, n, reverse=False):
    if n == 1:
        return sequence
    for i in range(len(sequence)-1):
        if reverse:
            if sequence[i] < sequence[i+1]:
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
        else:
            if sequence[i] > sequence[i+1]:
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
    return recursive_bubble_sort(sequence, n-1, reverse=reverse)


print(bubble_sort([10, 20, 40, 30 , 50]))
# print(recursive_bubble_sort([1, 4, 5, 3, 7, 8, 6, 9], 8, reverse=True))
