# Python program to find minimum element
# in a sorted and rotated array

def findMin(arr, low, high):
    # This condition is needed to handle the case when array is not
    # rotated at all
    if high < low:
        return arr[0]

    # If there is only one element left
    if high == low:
        return arr[low]

    # Find mid
    mid = int((low + high) / 2)

    # Check if element (mid+1) is minimum element. Consider
    # the cases like [3, 4, 5, 1, 2]
    if mid < high and arr[mid + 1] < arr[mid]:
        return arr[mid + 1]

    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]

    # Decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return findMin(arr, low, mid - 1)
    return findMin(arr, mid + 1, high)

def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) / 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

def bin_search_rotated_array(ind, arr, x):
    arr_l = arr1[0:ind]
    arr_r = arr1[ind:]
    if x >= arr_l[0]:
        return binarySearch(arr_l, 0, len(arr_l) - 1, x)
    else:
        return len(arr_l) + binarySearch(arr_r, 0, len(arr_r) - 1, x)


# Driver program to test above functions
arr1 = [ 1, 2, 3, 4, 5, 6]
n1 = len(arr1)
pivot = findMin(arr1, 0, n1 - 1)
pivot_ind = arr1.index(pivot)

print("The minimum element is " + str(pivot))
print(bin_search_rotated_array(pivot_ind, arr1, 3))