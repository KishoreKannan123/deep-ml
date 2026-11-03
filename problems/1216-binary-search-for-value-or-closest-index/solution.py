def binary_search_closest(arr, target):
    """
    Find the index of the element in a sorted array closest to target.
    Returns an integer index, or -1 if the array is empty.
    """
    if not arr:
        return -1

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # After the loop, low and high have crossed. 
    # Check bounds and return the index of the element with the minimum absolute difference.
    if high < 0:
        return low
    if low >= len(arr):
        return high

    if abs(arr[high] - target) <= abs(arr[low] - target):
        return high
    else:
        return low