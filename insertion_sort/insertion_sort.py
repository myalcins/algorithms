def insertion_sort(arr):
    for j in range(1, len(arr)):
        val = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > val:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = val

    return arr

