# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                has_swapped = True

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# space complexity is 0(n)
# time complexity is 0(n)

def counting_sort(arr, maximum=None):
    # Your code here

    if len(arr) > 0:
        # check for negative numbers:
        foundNegative = False
        index = 0
        while not foundNegative or index < len(arr):
            if arr[index] < 0:
                foundNegative = True
                return "Error, negative numbers not allowed in Count Sort"
            index += 1

        # if negative numbers were not found, counting sort can be applied
        buckets = [0] * (len(arr)+ 1)

        for i in arr:
            buckets[i] += 1

        i = 0
        for a in range(len(arr)+ 1):
            temp = buckets[a]
            buckets[a] = i
            i += temp

        result = [None] * len(arr)

        for index in arr:
            result[buckets[index]] = index
            buckets[index] += 1

        return result
    else: #if size is 0, return an empty array
        return []
