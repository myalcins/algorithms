# calculate the sum of a list of numbers
def list_sum(arr):
    if len(arr) == 1:
        return arr.pop()
    else:
        return arr.pop() + list_sum(arr)


# write a program to converting an integer to a string in any base.
def to_string(num, base):
    base_string = "0123456789ABCDEF"
    if num < base:
        return base_string[num]
    else:
        return to_string(num // base, base) + base_string[num % base]

# Write a recursive function to count the number of items in a list.
def number_of_item(arr, counter=0):
    if len(arr) == 0:
        return counter
    else:
        counter += 1
        return number_of_item(arr[1:], counter)

# Find the maximum number in a list.
def find_max(arr, max_num=0):
    if len(arr) == 0:
        return max_num
    else:
        num = arr.pop()
        if num > max_num:
            max_num = num
        return find_max(arr, max_num)

# binary search
def binary_search_contains(arr, item):
    if len(arr) == 1:
        return True if arr[0] == item else False
    else:
        mid = len(arr) // 2
        guess = arr[mid]
        if guess == item:
            return True
        else:
            if guess > item:
                return binary_search(arr[:mid], item)
            else:
                return binary_search(arr[mid:], item)

def binary_search(arr, item, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return binary_search(arr, item, mid+1, high)
        elif arr[mid] > item:
            return binary_search(arr, item, low, mid-1)
    return None      

# quicksort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr if x < pivot]
        greater = [ x for x in arr if x > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

