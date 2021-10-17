import numpy as np

# Missing Number
total = sum(range(1, 50)) + sum(range(51, 101))
actual_total = 100 * (101) / 2
print(actual_total - total)


# Two Sum
def pair_sum(numbers, value):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] == numbers[j]:
                continue
            elif numbers[i] + numbers[j] == value:
                print(i, j)


pair_sum([1, 2, 3, 4, 4, 5, 8, 6, 4, 3, 7, 9], 10)


# rotate by 90
def rotate_matrix(array):
    n = len(array)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top element
            top = array[layer][i]
            # move left to top
            array[layer][i] = array[-i - 1][layer]
            # move bottom to left
            array[-i - 1][layer] = array[-layer - 1][-i - 1]
            # move right to bottom
            array[-layer - 1][-i - 1] = array[i][-layer - 1]
            # move top to right
            array[i][-layer - 1] = top
    return array


array = np.array([
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11]
])
print(rotate_matrix(array))


# middle function
def middle(lst):
    n = len(lst)
    if n % 2:
        return lst[n // 2]
    else:
        return lst[n // 2 - 1], lst[n // 2]


print(middle([1, 2, 3, 4]))


# diagonal sum of 2D
def diagonal_sum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i][i]
    return sum


print(diagonal_sum([
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11]
]))

def missingNumber(myList, totalCount):
    total = (totalCount*(totalCount+1))/2
    mis_total = sum(myList)
    return total - mis_total


def pairSum(myList, sum):
    matches = []
    for i in range(len(myList)):
        for j in range(i, len(myList)):
            if myList[i] == myList[j]:
                continue
            else:
                if myList[i] + myList[j] == sum:
                    if (myList[i], myList[j]) not in matches and (myList[j], myList[i]) not in matches:
                        matches.append((myList[i], myList[j]))

    return matches


# def numtowords(number):
