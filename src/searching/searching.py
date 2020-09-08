# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) == 0:
        return -1
    middle_index = (start + end) // 2
    middle_value = arr[middle_index]

    if middle_value == target:
        return middle_index
    else:
        if middle_value < target:
            return binary_search(arr, target, middle_index, end)
        if middle_value > target:
            return binary_search(arr, target, start, middle_index)

    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
