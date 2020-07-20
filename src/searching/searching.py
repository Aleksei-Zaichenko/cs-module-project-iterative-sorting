def linear_search(arr, target):
    # Your code here
    result = (-1)

    for i in range(0, len(arr)):
        if arr[i] == target:
            result = i

    return result   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0
    last = len(arr) -1
    found = False
    index = (-1)

    while first <= last and not found:
        mid = (first  + last) //2
        if arr[mid] == target:
            found = True
            index = mid
        else:
            if arr[mid] < target:
                first = mid + 1
            else:
                last = mid - 1

    return index
