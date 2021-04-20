def binary_search(arr, item):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None