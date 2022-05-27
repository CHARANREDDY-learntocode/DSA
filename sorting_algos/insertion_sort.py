def insertion_sort(sequence: list):
    for i in range(1, len(sequence)):
        key = sequence[i]
        j = i - 1
        while j >= 0 and key <= sequence[j]:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = key
    return sequence


if __name__ == "__main__":
    print(insertion_sort([2, 3, 4, 1, 6, 5, 8, 7, 9]))
