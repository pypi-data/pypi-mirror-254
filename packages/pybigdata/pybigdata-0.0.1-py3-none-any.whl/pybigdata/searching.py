# Linear Search algorithm
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


# Binary Search algorithm
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Jump Search algorithm
def jump_search(arr, target):
    n = len(arr)
    step = int(n**0.5)
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)

        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1


# Interpolation Search algorithm
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# Exponential Search algorithm
def exponential_search(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return binary_search(arr[: min(i, n)], target)
