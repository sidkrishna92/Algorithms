# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while i > 0 and key < arr[i-1]:
            arr[i] = arr[i-1]
            i = i-1
        arr[i] = key

    return arr

arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))