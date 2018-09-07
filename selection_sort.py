def selection_sort(arr, n):
    if n>0:
        for i in range(0,n-1):
            min = i
            for j in range(i+1, n):
                if arr[min]>arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr
    else:
        return -1

arr = [5, 8, 3, 9, 2]
print(selection_sort(arr, len(arr)))