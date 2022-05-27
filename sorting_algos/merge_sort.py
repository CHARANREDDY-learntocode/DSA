def merge(sub_sequence, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left_arr = [0]*n1
    right_arr = [0]*n2

    for i in range(0, n1):
        left_arr[i] = sub_sequence[l+i]
    for j in range(0, n2):
        right_arr[j] = sub_sequence[m+j+1]

    k = l
    i = 0
    j = 0

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            sub_sequence[k] = left_arr[i]
            i += 1
        else:
            sub_sequence[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        sub_sequence[k] = left_arr[i]
        k += 1
        i += 1

    while j < n2:
        sub_sequence[k] = right_arr[j]
        k += 1
        j += 1


def merge_sort(sequence, l, r):
    if l < r:
        m = (l+(r-1))//2
        merge_sort(sequence, l, m)
        merge_sort(sequence, m+1, r)
        merge(sequence, l, m, r)
    return sequence


if __name__ == "__main__":
    print(merge_sort([1,5,6,7,3,2,8,9, 0], 0, 8))
