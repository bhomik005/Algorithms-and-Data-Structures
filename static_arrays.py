# Length is the number of elements in the array
# Capacity is the memory allocated for the fixed size array
# O(1) time
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

# Soft delete - overwriting the last element to 0
# [1, 3, 4, 5]
# [1, 3, 4, 0]
# O(1) time
def removeEnd(arr, length):
    # check if array is not empty
    if length >= 1:
        arr[length - 1] = 0

# [1, 3, 5] (insert 4 at idx 1) -> [1, 4, 3, 5] (shift the elemnts by 1 pos to the right)
# O(n) time
def insertMiddle(arr, i, n, length):
    # shift the elements by 1 pos to the right (length - 1, i)
    for idx in range(length, i, -1):
        arr[idx] = arr[idx - 1]
    # insert the element at ith index
    arr[i] = n

# [1, 3, 5, 6] (remove the element at 2nd pos) -> [1, 3, 6, ?] (shift the elements to the left)
# O(n) time
def removeMiddle(arr, i, length):
    # shift the elements to the left by 1 pos
    for idx in range(i, length - 1):
        arr[idx] = arr[idx + 1]

# O(n) time
def printArr(arr, capacity):
    for i in range(capacity):
        print(arr[i])