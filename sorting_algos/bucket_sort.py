import math

from insertion_sort import insertion_sort


def bucket_sort(sequence):
    buckets_count = round(math.sqrt(len(sequence)))
    max_value = max(sequence)
    arr = []

    for _ in range(buckets_count):
        arr.append([])
    for i in sequence:
        bucket_index = math.ceil(i * buckets_count / max_value)
        arr[bucket_index - 1].append(i)
    for j in arr:
        insertion_sort(j)
    k = 0
    for i in range(buckets_count):
        for j in range(len(arr[i])):
            sequence[k] = arr[i][j]
            k += 1
    return sequence


print(bucket_sort([5, 4, 6, 7, 2, 18, 3, 9]))
