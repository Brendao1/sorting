def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(i-1, i)
                swapped = True
    return arr

arr = [6, 4, 5, 2, 1]
print(bubble_sort(arr))

