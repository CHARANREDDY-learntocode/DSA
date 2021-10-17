import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
arr_1 = np.insert(arr, 1, [[77, 88, 99], [44, 55, 66]], axis=0)
print(arr_1)
arr_2 = np.append(arr, [[1, 2, 3]], axis=0)
print(arr_2)


# Accessing elements
def access_elements(array, row, col):
    if row > len(array) or col > len(array[0]):
        print("Inavalid index")
    else:
        print(array[row][col])


access_elements(arr_1, row=2, col=2)


#Traverse elements
def traverse_array(array):
    for row in range(len(array)):
        for col in range(len(array[0])):
            print(array[row][col])


traverse_array(arr)


#Search an element
def search_array(array, value):
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == value:
                print(f'Value located at row {row} col {col}')
                return
    print(f'{value} not found')
search_array(arr, 8)
print(arr)
arr = np.delete(arr, 1, axis=0)
print(arr)
