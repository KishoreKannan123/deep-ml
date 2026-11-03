def binary_search_closest(arr, target):
    # arr is sorted in non-decreasing order
    # return an integer index (or -1 for empty arr)
    low = 0
    high = len(arr)-1

    while(low<=high):
        if(high - low == 1):
            if(target>=arr[high]):
                return high
            else:
                return low
        mid = (low+high)//2
        if(arr[mid] == target):
            return mid
        elif(arr[mid]<target):
            low = mid
        else:
            high = mid
    
    return -1
        