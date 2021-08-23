import array
from array import *
import logging

logging.basicConfig(level=logging.INFO)

#1 Create an arry and traverse
print('#1 Create an arry and traverse')
arr = array('i', [1,2,3,4,5]) 
for num in arr:
    print(num)

#2 Access individual elements through index
print("#2 Access individual elements through index")
print(arr[0])
print(arr[1])

#3 append any value to the array using append method
print("#3 append any value to the array using append method")
arr.append(5)
print(arr)

#4 insert an element into the array using insert method
print("#4 insert an element into the array using insert method")
arr.insert(5, 10)
arr.insert(10, 20)
arr.insert(0, 5)
print(arr)

#5 extend python array using extend method
print("#5 extend python array using extend method")
arr.extend(array('i', [33, 44, 55]))
print(arr)

#6 add items from list into array using fromlist() method
print('#6 add items from list into array using fromlist() method')
arr.extend([2, 3, 445, 5, 5])
print(arr)

#7 Remove any array element using remove() method
print('#7 Remove any array element using remove() method')
arr.remove(445)
print(arr)

#8 Remove last array element using pop() method
print('#8 Remove any array element using pop method')
arr.pop()
print(arr)

#9 Fetch ana element through its index usiing index() method
print('#9 Fetch an element through its index usiing index() method')
print(arr[arr.index(55)])

#10 reverse a python arrray using reverse method
print('#10 reverse a python arrray using reverse method')
arr.reverse()
print(arr)

#11 Get array buffer information through buffer_info() method
print('#11 Get array buffer information through buffer_info() method')
print(arr.buffer_info())

#12 Check for number of occurences of an element using count method
print('#12 Check for number of occurences of an element using count method')
print(arr.count(5))

#13 Convert an arry to string using tostring() method
print('#13 Conver an arry to string using tostraing() method')
print(arr.tostring())

#14 Convert an arry to string using fromstring() method
print('#14 Conver an arry to string using fromstring() method')
str_ints = arr.tostring()
x = array('i')
x = x.fromstring(str_ints)
print(x)

#15 Convert array to a python list with same elements using tolist() method
print('#15 Convert array to a python list with same elements using tolist() method')
print(arr.tolist())

#16 Slicing of an array
print('#16 Slicing of an array')
print(arr[1:5])
