# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    indexA = 0 # current index pointer for arrayA
    indexB = 0 # current index pointer for arrayB
    mergeIndex = 0 # index of our merged arr
          
    # while indexA is less then the length of arrayA and indexB is less than the arrayB (both arrays contain values)
    while indexA < len(arrA) and indexB < len(arrB): 
        if arrA[indexA] < arrB[indexB]: # if the value of arrA at the current indexA is greater than value of arrB at the current indexB
            merged_arr[mergeIndex] = arrA[indexA] # set the current index of the mergeIndex to the current index of A
            indexA += 1 # increment the indexA pointer
        else: # the value of arrB at the current indexB is greater than arrA at the current indexA
            merged_arr[mergeIndex] = arrB[indexB] # set the current index of the mergeIndex to the current index of B
            indexB += 1 # increment the indexB pointer
        mergeIndex += 1 # increment the mergeIndex pointer
    # while arrayB is not empty but arrayB is
    while indexA < len(arrA): 
        # set the current index of the merged_arr to the arrA current index
        merged_arr[mergeIndex] = arrA[indexA]
        # increment the indexes
        indexA += 1
        mergeIndex += 1
    # while arrayB
    while indexB < len(arrB): 
        # set the current index of the merged_arr to the arrB current index
        merged_arr[mergeIndex] = arrB[indexB] 
        # increment the indexes
        indexB += 1
        mergeIndex += 1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # check if arr length is greater than 1
    if len(arr) > 1:
        # set the mid variable to be the arr divided by 2
        middle = len(arr) // 2
        
        # set left ot be everything up to the middle of the arr
        left = arr[:middle]
        
        # set right to be everything from the middle to the end
        right = arr[middle:]

        return merge(merge_sort(left), merge_sort(right))
    print(arr)
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
