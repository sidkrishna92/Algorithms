def maxmin(arr):
    maximum = minimum = arr[0]
    for i in arr[1:]:
        if i < minimum :
            minimum = i
        else:
            maximum = i
    return (maximum, minimum)

arr1 = [1, 8, 92, 3, 81, 7, 11]
print maxmin(arr1)

